import base64
import io
import random
from http.client import responses
import matplotlib.pyplot as plt

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pickle
import os
from random import randint
from time import sleep

from starlette import status
from starlette.responses import RedirectResponse

if os.path.exists('answers.txt'):
    answers = pickle.load(open('answers.txt', 'rb'))
else:
    answers = []

def generate_schulte(n: int):
    numbers = list(range(1, n*n + 1))
    random.shuffle(numbers)
    return numbers


best = 0
last = 0
y = []
x = []
attempt = 0






app=FastAPI()
templates = Jinja2Templates(directory="html")
app.mount("/html", StaticFiles(directory="html"), name="static")
app.mount("/audio", StaticFiles(directory="html/audio"), name="audio")
@app.middleware("http")
async def add_cache_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.get("/quest")
async def get_quest(request: Request):
    return (templates.TemplateResponse("quest.html", context={"request": request}))

@app.get("/audio")
async def get_shu(request: Request):
    return (templates.TemplateResponse("audio.html", context={"request": request}))

@app.get("/morzeq")
async def get_morzeq(request: Request):
    return (templates.TemplateResponse("morzeq.html", context={"request": request}))


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index2.html", context={"request": request})

@app.get('/instruction')
async def sumarise(request: Request):
    return templates.TemplateResponse('instruction.html', {"request": request})

@app.get("/login")
async def login(request: Request):
    return (templates.TemplateResponse("login.html", context={"request": request}))

@app.get("/login2")
async def login2(request: Request):
    return (templates.TemplateResponse("login2.html", context={"request": request}))

@app.post("/sendForm")
async def send_form(request: Request):
    body = await request.json()
    form = await request.form()
    data_from_from = dict(form.items())

    answers.append(data_from_from)
    pickle.dump(answers, open('answers.txt', 'wb'))
    return RedirectResponse(url='/html/index', status_code=status.HTTP_307_TEMPORARY_REDIRECT)


@app.get("/answers")
async def get_answers(request: Request):
    return (templates.TemplateResponse("answers.html", context={"request": request, 'data_items': answers}))


@app.get("/index")
async def login(request: Request):
    return (templates.TemplateResponse("index.html", context={"request": request}))

@app.get("/shulte")
async def shulte(request: Request):
    return (templates.TemplateResponse("shulte.html", context={"request": request}))





@app.get('/result')
async def result(request: Request, time: str = ""):

    global x
    global y
    global attempt
    global best
    global last


    if time != "":
        attempt += 1
        x += [attempt]
        if int(time[:-7]) == 0:
            time = float(time[3:-4] + '.' + time[6:])
            y.append(time)
        else:
            time = float(str(float(time[:-7])*60 + float(time[3:-4]))[:-2] + '.' + time[6:])
            y.append(time)
        best = (min(y))
        last = y[-1]

    plt.figure(figsize=(15, 10))
    plt.plot(x, y)
    plt.title('График')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    image_base64 = base64.b64encode(buf.read()).decode('UTF-8')
    print(image_base64)
    buf.close()
    return (templates.TemplateResponse("result.html", {"request": request, 'image_base64': image_base64, 'best': best, 'last': last}))

# @app.get("/result")
# async def resultat(request: Request):
#     return (templates.TemplateResponse("result.html", context={"request": request}))
#
