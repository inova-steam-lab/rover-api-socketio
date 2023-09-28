from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import socketio
import rover


app = FastAPI()

# Ref: https://www.reddit.com/r/FastAPI/comments/neds9c/integrate_socketio_with_fastapi/
# Estabelece a integração entre o FastAPI e o SocketIO.
socket = socketio.AsyncServer(cors_allowed_origins='*', async_mode='asgi')
socketio_app = socketio.ASGIApp(socket, app)

# Serve os arquivos que estão na pasta /static
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index():
    ''' Página inicial que será utilizada para controlar o Hover. '''
    return FileResponse('static/index.html')


@socket.event
def connect(sid, environ):
    print("connect ", sid)


@socket.event
async def move_forward(sid, data):
    print("Movendo...")

    rover.go_forward()

    await socket.emit("hover_status", data={'message': '[Hover] - Movendo...'})


@socket.event
async def move_backward(sid, data):
    print("Retrocedendo...")

    rover.go_backward()

    await socket.emit("hover_status", data={'message': '[Hover] - Retrocedendo...'})


@socket.event
async def move_left(sid, data):
    print("Movendo para esquerda...")

    rover.go_left()

    await socket.emit("hover_status", data={
        'message': '[Hover] - Movendo para esquerda...'})


@socket.event
async def move_right(sid, data):
    print("Movendo para direita...")

    rover.go_right()

    await socket.emit("hover_status", data={
        'message': '[Hover] - Movendo para direita...'})


@socket.event
async def stop(sid, data):
    print("Parando...")

    rover.stop()

    await socket.emit("hover_status", data={'message': '[Hover] - Parando...'})
