from nest.core import Module

from src.blog.blog_controller import BlogController
from src.blog.blog_service import BlogService


@Module(
    controllers=[BlogController],
    providers=[BlogService],
    imports=[]
)   
class BlogModule:
    pass

    