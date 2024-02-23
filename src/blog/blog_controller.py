from typing import cast

from nest.core import Controller, Get, Post, Depends

from .blog_service import BlogService
from .blog_model import BlogIn, BlogOut


@Controller("blog")
class BlogController:

    service: BlogService = cast(BlogService, Depends(BlogService))
    
    @Get("/")
    async def get_blog(self):
        return self.service.get_blog()
                
    @Post("/", status_code=201, response_model=BlogOut)
    def add_blog(self, payload: BlogIn):
        return self.service.add_blog(payload)
 