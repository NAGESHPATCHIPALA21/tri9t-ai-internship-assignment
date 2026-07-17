import fitz
import re

from app.utils import compute_hash, heading_level


HEADING_PATTERN = re.compile(r"^\d+(\.\d+)*\s+.+$")


def is_heading(text: str):
    return bool(HEADING_PATTERN.match(text.strip()))


def parse_pdf(path):
    doc = fitz.open(path)

    nodes = []

    stack = []

    node_id = 1

    for page_num, page in enumerate(doc, start=1):

        text = page.get_text()

        current = None

        for line in text.split("\n"):

            line = line.strip()

            if not line:
                continue

            if is_heading(line):

                level = heading_level(line)

                while stack and stack[-1]["level"] >= level:
                    stack.pop()

                parent = stack[-1]["id"] if stack else None

                node = {
                    "id": node_id,
                    "title": line,
                    "level": level,
                    "body": "",
                    "page": page_num,
                    "parent": parent,
                    "children": [],
                    "hash": ""
                }

                if stack:
                    stack[-1]["children"].append(node_id)

                nodes.append(node)

                stack.append(node)

                current = node

                node_id += 1

            else:

                if current:
                    current["body"] += line + "\n"

    for node in nodes:
        node["hash"] = compute_hash(node["body"])

    return nodes