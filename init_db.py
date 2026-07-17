from app.database import Base, engine
from app.models import Document, DocumentVersion, Node

Base.metadata.create_all(bind=engine)

print("Database created successfully!")