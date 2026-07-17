from app.database import SessionLocal
from app.models import DocumentVersion, Node


def compare_versions(version1: str, version2: str):
    db = SessionLocal()

    v1 = (
        db.query(DocumentVersion)
        .filter_by(version=version1)
        .first()
    )

    v2 = (
        db.query(DocumentVersion)
        .filter_by(version=version2)
        .first()
    )

    if not v1 or not v2:
        db.close()
        return {"error": "Version not found"}

    nodes1 = {
        n.title: n
        for n in db.query(Node).filter_by(version_id=v1.id).all()
    }

    nodes2 = {
        n.title: n
        for n in db.query(Node).filter_by(version_id=v2.id).all()
    }

    added = []
    removed = []
    modified = []
    unchanged = []

    all_titles = set(nodes1.keys()) | set(nodes2.keys())

    for title in sorted(all_titles):
        if title not in nodes1:
            added.append(title)

        elif title not in nodes2:
            removed.append(title)

        elif nodes1[title].content_hash == nodes2[title].content_hash:
            unchanged.append(title)

        else:
            modified.append(title)

    db.close()

    return {
        "added": added,
        "removed": removed,
        "modified": modified,
        "unchanged": unchanged,
    }