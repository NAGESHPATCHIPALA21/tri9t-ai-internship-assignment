import hashlib
import re


def compute_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


HEADING_REGEX = re.compile(r"^\d+(\.\d+)*\.?\s+.+$")


def is_heading(text: str) -> bool:
    return bool(HEADING_REGEX.match(text.strip()))


def heading_level(title: str) -> int:
    number = title.split()[0].rstrip(".")
    return number.count(".") + 1