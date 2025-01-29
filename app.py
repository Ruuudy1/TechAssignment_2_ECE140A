from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, Response, JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

app = FastAPI()

# Serve static files (JS, CSS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=Response)
def get_hello() -> Response:
    return Response(content="Hello, World!", media_type="text/html")

@app.get("/about")
def about():
    return JSONResponse(content={
        "name": "Rudy Osuna",
        "major": "Computer Science",
        "year": "3rd",
        "College": "ERC",
        "bio": "I am rudy Osuna, a rising 3rd year majoring in computer science and minoring in business analytics",
        "interests": ["Soccer", "FullStack Software Engineering", "Quantitative Trading", "Fintech"]
    })

# Challenge 1 (World Clock)
@app.get("/world-clock", response_class=HTMLResponse)
def world_clock_page(request: Request):
    file_path = os.path.join(os.path.dirname(__file__), "world_clock", "index.html")
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

# Challenge 2 (Puppy Pong)
@app.get("/puppy-pong", response_class=HTMLResponse)
def puppy_pong_page(request: Request):
    file_path = os.path.join(os.path.dirname(__file__), "puppy_pong", "index.html")
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6543)
