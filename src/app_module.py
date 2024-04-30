from nest.core import PyNestFactory, Module

from src.blog.blog_module import BlogModule
from src.config import config


@Module(imports=[BlogModule], controllers=[], providers=[])
class AppModule:
    pass


app = PyNestFactory.create(
    AppModule,
    description="Blog Application with PyNest",
    title="Blog Application",
    version="1.0.0",
    debug=True,
    docs_url="/",
)
http_server = app.get_server()


@http_server.on_event("startup")
def startup():
    config.create_all()
