from typing import List

from nest.core import Controller, Get, Post

from src.blog.blog_model import BlogIn, BlogOut
from src.blog.blog_service import BlogService


@Controller("blog")
class BlogController:

    def __init__(self, blog_service: BlogService):
        self.blog_service = blog_service
    
    @Get("/", response_model=List[BlogOut])
    def get_blog(self):
        return self.blog_service.get_blog()
                
    @Post("/", status_code=201, response_model=BlogOut)
    def add_blog(self, payload: BlogIn):
        return self.blog_service.add_blog(payload)
 