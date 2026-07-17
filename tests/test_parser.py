from app.parser import parse_pdf

nodes = parse_pdf("data/ct200_manual.pdf")

for n in nodes:
    print(
        n["id"],
        n["title"],
        n["parent"],
        n["page"]
    )