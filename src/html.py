from fastapi import FastAPI, Request, Form, File, UploadFile 
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from src.model import predict 

 
app = FastAPI()
app.mount("/static", StaticFiles(directory='templates/static'), name="static")
templates = Jinja2Templates(directory='templates/')


def save_to_text(content, filename):
    filepath = 'data/{}.txt'.format(filename)
    with open(filepath, 'w') as f:
        f.write(content)
    return filepath

@app.get('/')
def form_post(request: Request):
    return templates.TemplateResponse('form.html', context={'request': request})


@app.post('/')
def form_post(request: Request, files: UploadFile = File(...)):
    transcription=predict(files)
    Audio_fileName=files.filename
    return templates.TemplateResponse('form.html', context={'request': request , 'file_name':Audio_fileName ,'Transcription':transcription})



