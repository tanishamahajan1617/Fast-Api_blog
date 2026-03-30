from fastapi import FastAPI, Request,HTTPException,status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

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
     request,"home.html",{ "posts": posts,"title": "home" } )

@app.get("/api/posts")
def get_posts():
    return {"data": posts}

@app.get("/posts/{post_id}")
def get_one_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return {"data": post}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")  
  