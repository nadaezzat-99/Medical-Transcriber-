from fastapi import FastAPI, Request, Form, File, UploadFile 
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from src.model import spell_number , predict 

app = FastAPI()
#app.mount("templates/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates/')


def save_to_text(content, filename):
    filepath = 'data/{}.txt'.format(filename)
    with open(filepath, 'w') as f:
        f.write(content)
    return filepath


@app.get('/')
def read_form():
    return 'hello world'

@app.get('/form')
def form_post(request: Request):
    result = 'Type a number'
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.post('/form')
def form_post(request: Request, num: int = Form(...), files: UploadFile = File(...)):
    result1=files
    result2=files.filename
    #result2=predict(files)
    result = spell_number(num)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result, 'num': num , 'result1': result1 , 'result2': result2})




