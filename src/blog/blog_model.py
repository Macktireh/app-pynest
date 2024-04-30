from datetime import datetime

from pydantic import BaseModel


class BlogIn(BaseModel):
    title: str
    content: str


class BlogOut(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    updated_at: datetime

