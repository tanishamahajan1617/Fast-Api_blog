from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Make sure this matches your folder name
templates = Jinja2Templates(directory="templates")

# Renamed to 'posts' (plural) for better clarity
posts = [
    {"id": 1, "title": "First Post", "content": "This is the content of the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the content of the second post."},
    {"id": 3, "title": "Third Post", "content": "This is the content of the third post."}
]

@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def read_root(request: Request):
    # We pass "posts" to the template
    return templates.TemplateResponse(
        "home.html", 
        {"request": request, "posts": posts} 
    )

@app.get("/api/posts")
def get_posts():
    return {"data": posts}