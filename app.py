from config import config
from nest.core.app import App
from src.blog.blog_module import BlogModule

app = App(description="PyNest service", modules=[BlogModule])


@app.on_event("startup")
def startup():
    config.create_all()
