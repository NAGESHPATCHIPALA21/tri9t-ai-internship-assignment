from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.models import Node
from app.schemas import GenerateRequest
from app.ai import generate_test_cases

router = APIRouter()

@router.post("/generate")
def generate(request: GenerateRequest):
    db = SessionLocal()

    nodes = (
        db.query(Node)
        .filter(Node.id.in_(request.node_ids))
        .all()
    )

    db.close()

    if not nodes:
        raise HTTPException(status_code=404, detail="No matching nodes found.")

    context = "\n\n".join(
        f"{node.title}\n{node.body}"
        for node in nodes
    )

    result = generate_test_cases(context)

    return {
        "generated_test_cases": result
    }