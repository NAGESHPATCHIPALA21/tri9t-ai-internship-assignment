from pydantic import BaseModel
from typing import List, Optional


class Node(BaseModel):
    id: int
    title: str
    level: int
    body: str
    page: int
    parent: Optional[int]
    children: List[int]
    content_hash: str