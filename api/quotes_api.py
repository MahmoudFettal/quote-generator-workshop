import json
import random
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/quote")
async def get_quote():
    quotes = None

    with open("tech_quotes.json") as file:
        quotes = json.load(file)

    return quotes[random.randint(0, len(quotes) - 1)]


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
