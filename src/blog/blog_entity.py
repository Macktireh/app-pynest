from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text

from config import config


class BlogEntity(config.Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True)
    content = Column(Text, nullable=False)
    published = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "published": self.published,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
