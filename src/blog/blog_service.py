from nest.core import Injectable
from nest.core.decorators.database import db_request_handler

from src.blog.blog_entity import Blog as BlogEntity
from src.blog.blog_model import BlogIn, BlogOut
from src.config import config


@Injectable
class BlogService:

    def __init__(self):
        self.config = config
        self.session = self.config.get_db()
    
    @db_request_handler
    def add_blog(self, payload: BlogIn):
        new_blog = BlogEntity(
            **payload.dict()
        )
        self.session.add(new_blog)
        self.session.commit()
        return BlogOut(**new_blog.to_dict())

    @db_request_handler
    def get_blog(self):
        blogs = self.session.query(BlogEntity).all()
        return [BlogOut(**blog.to_dict()) for blog in blogs]
    
    @db_request_handler
    def get_blog_by_id(self, id):
        blog = self.session.query(BlogEntity).filter(BlogEntity.id == id).first()
        return BlogOut(**blog.to_dict())
    
    @db_request_handler
    def update_blog_by_id(self, id, payload: BlogIn):
        blog = self.session.query(BlogEntity).filter(BlogEntity.id == id).first()
        blog.update(payload.dict())
        self.session.commit()
        return BlogOut(**blog.to_dict())
    
    @db_request_handler
    def delete_blog_by_id(self, id):
        self.session.query(BlogEntity).filter(BlogEntity.id == id).delete()
        self.session.commit()
