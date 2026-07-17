import hashlib


def compute_hash(text: str) -> str:
    """Generate SHA256 hash for node content."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def heading_level(title: str) -> int:
    """
    Determine heading depth from numbering.

    Examples:
    1 -> level 1
    2.1 -> level 2
    2.1.1.1 -> level 4
    """
    first = title.split()[0]

    if "." not in first:
        return 1

    return first.count(".") + 1