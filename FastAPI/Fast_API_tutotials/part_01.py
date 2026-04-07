from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs when the app starts
    # SQLModel.metadata.create_all(engine) # Optional: if you want to create tables automatically
    yield
    # This runs when the app stops


app = FastAPI(
    title="FastAPI Tutorial",
    description="Backend for FastaPI tutorial",
    version="1.0.0",
    lifespan=lifespan
)


posts: list[dict] = [
    {
        "id": 1,
        "author": "Vijesh Vidhani",
        "title": "FastAPI Tutorial",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Random user",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]



@app.get("/", tags=["Root"], response_class=HTMLResponse)
def root():
    return f"<h1>{posts[0]['title']}</h1>",
    """
    {
        "title": app.title,
        "status": "online",
        "documentation": "/docs",
        "message": "Tutorial for FastAPI: https://www.youtube.com/watch?v=7AMjmCTumuo&list=PL-osiE80TeTsak-c-QsVeg0YYG_0TeyXI"
    }
    """


@app.get("/api/posts")
def get_posts(id: int = None):
    return posts