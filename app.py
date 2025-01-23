from fastapi import FastAPI, Request, Form
from fastapi.responses import Response, JSONResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from urllib.request import urlopen
import json

## LOAD API KEY FROM .ENV FILE ##
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
#################################

app = FastAPI()

# Add CORS (Cross Origin Resource Sharing) middleware.
# middleware basically acts as a middleman making API integration 
# (calls, endpoints) and JSONResponse more secure and correct error handling
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # allows requests from any (*) domain 
    allow_credentials=True,  # credentials basically hits the enable cookies button for us
    allow_methods=["*"],     # allows all HTTP methods we will use (GEt, POST, PUSH)
    allow_headers=["*"],     # Allows all header types when making a request
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory=".")

# Global variable to store stock data
stock_data = {}

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

@app.get("/stock", response_class=HTMLResponse)
async def serve_stock_form(request: Request):
    return templates.TemplateResponse("stock/index.html", {"request": request})


########################################################################################################################
######################### ALL ROUTE HANDLERS TO FETCH FROM THE URL #####################################################
########################################################################################################################


# fetch the stock symbol inputted into all 3 forms in the frontend (index.html)
@app.post("/stock")
async def handle_stock_form(
    request: Request,
    symbol1: str = Form(...),
    symbol2: str = Form(...),
    symbol3: str = Form(...)
):
    # stock_data is a global dictionary that stores stock data for each of the 3 symbols we passed in on the form above
    global stock_data
    symbols = [symbol1, symbol2, symbol3]
    stock_data = {}

    for i, symbol in enumerate(symbols, start=1):
        url = f"https://financialmodelingprep.com/api/v3/profile/{symbol}?apikey={api_key}"
        try:
            response = urlopen(url)
            data_json = json.loads(response.read())
            
            if data_json:
                company_data = data_json[0]
                stock_data[i] = {
                    "Company Name": company_data.get("companyName", "N/A"),
                    "Industry": company_data.get("industry", "N/A"),
                    "Sector": company_data.get("sector", "N/A"),
                    "Stock Price": company_data.get("price", "N/A")
                }
            else:
                stock_data[i] = {
                    "Company Name": "Invalid Symbol",
                    "Industry": "N/A",
                    "Sector": "N/A",
                    "Stock Price": "N/A"
                }
        except Exception as e:
            print(f"Error fetching data for {symbol}: {str(e)}")
            stock_data[i] = {
                "Company Name": "Error",
                "Industry": "N/A",
                "Sector": "N/A",
                "Stock Price": "N/A"
            }

    return RedirectResponse(url="/stock/page", status_code=303)


# display the results of the fetch after clicking "get stock information"
@app.get("/stock/page", response_class=HTMLResponse)
async def serve_stock_page(request: Request):
    return templates.TemplateResponse("stock/page.html", {"request": request})

# api endpoint for each stock data + error handling if incorrect/unavailable stock symbol
@app.get("/stock/{stock_id}")
async def get_stock_data(stock_id: int):
    if stock_id not in stock_data:
        return JSONResponse(
            status_code=200,
            content={"message": "No data available for this stock."}
        )
    return JSONResponse(content=stock_data[stock_id])

# Routing to our other pages

@app.get("/blog", response_class=HTMLResponse)
async def blog_home(request: Request):
    return templates.TemplateResponse("blog/index.html", {"request": request})

@app.get("/blog/case_studies", response_class=HTMLResponse)
async def case_studies(request: Request):
    return templates.TemplateResponse("blog/case_studies.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6543)
