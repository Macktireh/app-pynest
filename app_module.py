from nest.core import PyNestFactory, Module

from src.blog.blog_module import BlogModule
from src.config import config


@Module(imports=[BlogModule], controllers=[], providers=[])
class AppModule:
    pass


app = PyNestFactory.create(
    AppModule,
    description="This is my PyNest app.",
    title="PyNest Application",
    version="1.0.0",
    debug=True,
)
http_server = app.get_server()


@http_server.on_event("startup")
def startup():
    config.create_all()
