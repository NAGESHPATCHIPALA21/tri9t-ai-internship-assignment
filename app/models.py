from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app.database import Base
class Selection(Base):
    __tablename__ = "selections"

    id = Column(Integer, primary_key=True)

    version_id = Column(Integer, ForeignKey("document_versions.id"))

    node_id = Column(Integer, ForeignKey("nodes.id"))


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    versions = relationship("DocumentVersion", back_populates="document")


class DocumentVersion(Base):
    __tablename__ = "document_versions"

    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey("documents.id"))
    version = Column(String)
    file_name = Column(String)

    document = relationship("Document", back_populates="versions")
    nodes = relationship("Node", back_populates="version")


class Node(Base):
    __tablename__ = "nodes"

    id = Column(Integer, primary_key=True)

    version_id = Column(Integer, ForeignKey("document_versions.id"))

    title = Column(String)
    level = Column(Integer)

    body = Column(Text)

    page = Column(Integer)

    parent_id = Column(Integer)

    content_hash = Column(String)

    version = relationship("DocumentVersion", back_populates="nodes")
    