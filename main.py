from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve os arquivos que estão na pasta /static
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index():
    ''' Página inicial que será utilizada para controlar o Hover. '''
    return FileResponse('static/index.html')
