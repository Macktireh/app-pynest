from .blog_service import BlogService
from .blog_controller import BlogController


class BlogModule:

    def __init__(self):
        self.providers = [BlogService]
        self.controllers = [BlogController]
