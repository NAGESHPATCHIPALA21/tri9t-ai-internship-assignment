from app.database import SessionLocal
from app.models import Document, DocumentVersion, Node
from app.parser import parse_pdf


def ingest_pdf(file_path: str, version: str):
    db = SessionLocal()

    document = db.query(Document).filter_by(name="CT-200").first()

    if document is None:
        document = Document(name="CT-200")
        db.add(document)
        db.commit()
        db.refresh(document)

    doc_version = DocumentVersion(
        document_id=document.id,
        version=version,
        file_name=file_path
    )

    db.add(doc_version)
    db.commit()
    db.refresh(doc_version)

    nodes = parse_pdf(file_path)

    for n in nodes:
        db.add(
            Node(
                version_id=doc_version.id,
                title=n.title,
                level=n.level,
                body=n.body,
                page=n.page,
                parent_id=n.parent,
                content_hash=n.content_hash,
            )
        )

    db.commit()
    db.close()

    print(f"Ingested {len(nodes)} nodes successfully.")