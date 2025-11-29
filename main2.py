import random

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pickle
import os
from random import randint
from time import sleep

app = FastAPI()

app.mount("/html/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="/html/templates")

def generate_schulte(n: int):
    numbers = list(range(1, n*n + 1))
    random.shuffle(numbers)
    return numbers

@app.get("/", response_class=HTMLResponse)
async def index(request: Request, n: int = 5):
    n = max(2, min(10, n))
    numbers = generate_schulte(n)
    return templates.TemplateResponse("index2.html", {"request": request, 'n': n, 'numbers': numbers})

@app.post('/result')
async def result(request: Request):
    body = await request.json()
    y = []
    x = []
    y += [body['time']]
    for i in range(1, len(y) + 1):
        x += [i]


@app.post('/result')
async def result(request: Request):
    body = await request.json()
    x = []
    y = []
    y += [body['time']]
    print(y)
    for i in range(1, len(y) + 1):
        x += [i]

    plt.plot(x, y)
    plt.title("График")
    plt.savefig("graph.png")
    plt.close()
    return "OK"


