from fastapi import FastAPI, Request
from fastapi import *
from fastapi.responses import HTMLResponse, Response, JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
import json
from contextlib import asynccontextmanager

from fastapi.staticfiles import StaticFiles

# Global dictionaries for book storage
library_inventory = []
my_inventory = {}



# Load books from JSON file
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load books on startup
    global library_inventory
    with open("static/books.json", "r") as f:
        library_inventory = json.load(f)
    yield

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/book")
async def get_all_books():
    return JSONResponse(content=library_inventory, status_code=200)

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

@app.get("/weather", response_class=HTMLResponse)
async def weather_page(request: Request):
    try:
        file_path = os.path.join(os.path.dirname(__file__), "Weather", "weather.html")
        with open(file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        return HTMLResponse(content=html_content, status_code=200)
    except FileNotFoundError:
        return HTMLResponse(content="Weather page not found", status_code=404)


############################################################################################################
#########################Challenge 2 of tech assignment 3###################################################
############################################################################################################

@app.post("/books")
async def create_book(request: Request):
    try:
        book_data = await request.json()
        library_inventory.append(book_data)
        return JSONResponse(content=book_data, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

@app.get("/library", response_class=HTMLResponse)
async def library_page(request: Request):
    file_path = os.path.join(os.path.dirname(__file__), "Library", "library.html")
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.get("/my-library", response_class=HTMLResponse)
async def my_library_page(request: Request):
    file_path = os.path.join(os.path.dirname(__file__), "Library", "my_library.html")
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.get("/my-inventory")
async def get_my_inventory():
    return JSONResponse(content=my_inventory)

@app.get("/books/{book_id}")
async def get_book(book_id: int):
    book = next((book for book in library_inventory if book["book_id"] == book_id), None)
    if book:
        return JSONResponse(content=book)
    return JSONResponse(content={"error": "Book not found"}, status_code=404)

@app.get("/authors/{author_name}")
async def get_books_by_author(author_name: str):
    books = [book for book in library_inventory if author_name.lower() in book["author"].lower()]
    return JSONResponse(content=books)

@app.put("/books/{book_id}")
async def update_book_status(book_id: int):
    book = next((book for book in library_inventory if book["book_id"] == book_id), None)
    if not book:
        return JSONResponse(content={"error": "Book not found"}, status_code=404)
    if book["status"] == "borrowed":
        return JSONResponse(content={"error": "Book already borrowed"}, status_code=400)
    book["status"] = "borrowed"
    my_inventory[book_id] = book.copy()
    return JSONResponse(content=book)

@app.delete("/books/{book_id}")
async def return_book(book_id: int):
    if book_id not in my_inventory:
        return JSONResponse(content={"error": "Book not in your inventory"}, status_code=404)
    book = next((book for book in library_inventory if book["book_id"] == book_id), None)
    if book:
        book["status"] = "not borrowed"
    del my_inventory[book_id]
    return JSONResponse(content={"message": "Book returned successfully"})

############################################################################################################
############################################################################################################
############################################################################################################


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6543)
