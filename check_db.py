from app.database import SessionLocal
from app.models import Document, DocumentVersion, Node

db = SessionLocal()

print("Documents :", db.query(Document).count())
print("Versions  :", db.query(DocumentVersion).count())
print("Nodes     :", db.query(Node).count())

doc = db.query(Document).first()
print("\nDocument:", doc.name)

version = db.query(DocumentVersion).first()
print("Version :", version.version)

print("\nFirst 5 Nodes:")
nodes = db.query(Node).limit(5).all()

for n in nodes:
    print(
        f"ID={n.id}, "
        f"Title={n.title}, "
        f"Level={n.level}, "
        f"Page={n.page}"
    )

db.close()