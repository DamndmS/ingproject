import pickle


import io
import base64
import matplotlib.pyplot as plt
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
#from fastapi.templating import Jinja2Template
import os

if os.path.exists('answers.pkl'):
    answer = pickle.load(open('answers.pkl', 'rb'))
    print(answer)
else:
    answer = []
from fastapi.staticfiles import StaticFiles

app=FastAPI()
app.mount("/static", StaticFiles(directory="html"), name="static")
app.mount("/audio", StaticFiles(directory="html/audio"), name="audio")
templates = Jinja2Templates(directory="html")
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return (templates.TemplateResponse("index.html", context={"request": request, "my_first_header": "42"}))

@app.post("/sendForm")
async def send_form(request: Request):
    form  = await request.form()
    data_from_from = dict(form.items())
    answer.append(data_from_from)
    pickle.dump(answer, open('answer.pkl', 'wb'))

@app.get("/answers")
async def get_answers(request: Request):
    return (templates.TemplateResponse("answers.html", context={"request": request, "answer": answer}))

@app.get("/instruction")
async def get_instruction(request: Request):
    return (templates.TemplateResponse("instruction.html", context={"request": request}))


@app.get("/index")
async def get_index(request: Request):
    return (templates.TemplateResponse("index.html", context={"request": request}))

@app.get("/autoz")
async def get_autoz(request: Request):
    return (templates.TemplateResponse("autoz.html", context={"request": request}))



@app.middleware("http")
async def add_cache_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.get("/shu")
async def get_shu(request: Request):
    return (templates.TemplateResponse("shu.html", context={"request": request}))

@app.get("/audio")
async def get_shu(request: Request):
    return (templates.TemplateResponse("audio.html", context={"request": request}))

@app.get("/result")
async def get_results(request: Request):
    return (templates.TemplateResponse("result.html", context={"request": request}))

async def result(request: Request, time: str = ""):

    global x
    global y
    global attempt

    if time != "":
        attempt += 1
        x += [attempt]
        time = float(time[3:-4] + '.' + time[6:])
        y.append(time)

    plt.figure(figsize=(15, 10))
    plt.plot(x, y)
    plt.title('График')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    image_base64 = base64.b64encode(buf.read()).decode('UTF-8')
    print(image_base64)
    buf.close()
    return (templates.TemplateResponse("result.html", {"request": request, 'image_base64': image_base64}))

@app.get("/morzeq")
async def get_morzeq(request: Request):
    return (templates.TemplateResponse("morzeq.html", context={"request": request}))

@app.get("/quest")
async def get_quest(request: Request):
    return (templates.TemplateResponse("quest.html", context={"request": request}))