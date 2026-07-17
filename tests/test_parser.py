from app.parser import parse_pdf

nodes = parse_pdf("data/ct200_manual.pdf")

print(f"Total nodes: {len(nodes)}")

for node in nodes[:10]:
    print(
        f"{node.id} | "
        f"{node.title} | "
        f"Level={node.level} | "
        f"Parent={node.parent} | "
        f"Page={node.page}"
    )