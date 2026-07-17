from pathlib import Path
import fitz

from app.schemas import Node
from app.utils import compute_hash, heading_level, is_heading

BASE_DIR = Path(__file__).resolve().parent.parent


def parse_pdf(relative_path: str):
    pdf_path = BASE_DIR / relative_path
    doc = fitz.open(pdf_path)

    nodes = []
    stack = []
    current = None
    node_id = 1

    for page_no, page in enumerate(doc, start=1):
        lines = page.get_text().splitlines()

        for line in lines:
            line = line.strip()

            if not line:
                continue

            if is_heading(line):

                level = heading_level(line)

                while stack and stack[-1].level >= level:
                    stack.pop()

                parent = stack[-1].id if stack else None

                node = Node(
                    id=node_id,
                    title=line,
                    level=level,
                    body="",
                    page=page_no,
                    parent=parent,
                    children=[],
                    content_hash=""
                )

                if stack:
                    stack[-1].children.append(node_id)

                nodes.append(node)
                stack.append(node)
                current = node
                node_id += 1

            elif current:
                current.body += line + "\n"

    for node in nodes:
        node.content_hash = compute_hash(node.body)

    return nodes