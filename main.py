from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Mock data for posts
posts = [
    {"id": 1, "title": "Getting Started with FastAPI", "content": "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints."},
    {"id": 2, "title": "Rendering Templates with Jinja2", "content": "Jinja2 is a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to Python syntax."},
    {"id": 3, "title": "Building RESTful APIs", "content": "RESTful APIs allow for interaction with web services by using HTTP methods like GET, POST, PUT, and DELETE."}
]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "posts": posts, "title": "FastAPI Blog"})

@app.get("/posts", response_class=HTMLResponse)
async def get_posts_html(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "posts": posts, "title": "All Posts"})

@app.get("/api/posts")
async def get_posts_json():
    return posts
