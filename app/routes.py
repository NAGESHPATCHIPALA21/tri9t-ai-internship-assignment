from fastapi import APIRouter
from sqlalchemy import or_

from app.database import SessionLocal
from app.models import Document, DocumentVersion, Node
from app.version_compare import compare_versions

router = APIRouter()
from pydantic import BaseModel

class SelectionRequest(BaseModel):
    version_id: int
    node_ids: list[int]


@router.get("/documents")
def get_documents():
    db = SessionLocal()

    docs = db.query(Document).all()

    result = [
        {
            "id": d.id,
            "name": d.name,
        }
        for d in docs
    ]

    db.close()

    return result


@router.get("/versions")
def get_versions():
    db = SessionLocal()

    versions = db.query(DocumentVersion).all()

    result = [
        {
            "id": v.id,
            "document_id": v.document_id,
            "version": v.version,
            "file_name": v.file_name,
        }
        for v in versions
    ]

    db.close()

    return result


@router.get("/nodes")
def get_nodes():
    db = SessionLocal()

    nodes = db.query(Node).all()

    result = [
        {
            "id": n.id,
            "title": n.title,
            "level": n.level,
            "page": n.page,
            "parent_id": n.parent_id,
        }
        for n in nodes
    ]

    db.close()

    return result


@router.get("/nodes/{node_id}")
def get_node(node_id: int):
    db = SessionLocal()

    node = db.query(Node).filter(Node.id == node_id).first()

    db.close()

    if node is None:
        return {"error": "Node not found"}

    return {
        "id": node.id,
        "title": node.title,
        "body": node.body,
        "page": node.page,
        "level": node.level,
        "parent_id": node.parent_id,
    }


@router.get("/search")
def search(q: str):
    db = SessionLocal()

    nodes = (
        db.query(Node)
        .filter(
            or_(
                Node.title.contains(q),
                Node.body.contains(q),
            )
        )
        .all()
    )

    db.close()

    return [
        {
            "id": n.id,
            "title": n.title,
            "page": n.page,
        }
        for n in nodes
    ]
@router.get("/compare")
def compare(v1: str, v2: str):
    return compare_versions(v1, v2)
from app.models import Selection


@router.post("/selection")
def create_selection(req: SelectionRequest):
    db = SessionLocal()

    for node_id in req.node_ids:
        db.add(
            Selection(
                version_id=req.version_id,
                node_id=node_id,
            )
        )

    db.commit()
    db.close()

    return {"message": "Selection saved"}