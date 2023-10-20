from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import socketio
import logging
import rover

logging.basicConfig(
    level="INFO",
    format="%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s",
    datefmt="[%Y-%m-%d,%H:%M:%S]",
)

app = FastAPI()

# Ref: https://www.reddit.com/r/FastAPI/comments/neds9c/integrate_socketio_with_fastapi/
# Estabelece a integração entre o FastAPI e o SocketIO.
socket = socketio.AsyncServer(cors_allowed_origins='*', async_mode='asgi')
socketio_app = socketio.ASGIApp(socket, app)

# Serve os arquivos que estão na pasta /static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configuração de CORS; Permite a comunicação entre diferentes domínios
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Vamos utilizar um estado para verificar se o carrinho está se movendo ou não
# FIXME: Utilizar outro mecanismo para armazenar o estado do carrinho.
app.is_moving = False


@app.get("/")
def index():
    ''' Página inicial que será utilizada para controlar o Rover. '''
    return FileResponse('static/index.html')


@socket.event
def connect(sid, environ):
    logging.info(f"Usuário conectado - {sid}")


@socket.event
async def move_forward(sid, data):
    logging.info("Movendo...")

    if not app.is_moving:
        rover.go_forward()        
        app.is_moving = True

    await socket.emit("rover_status", data={'message': '[Rover] - Movendo...'})


@socket.event
async def move_backward(sid, data):
    logging.info("Retrocedendo...")
    
    if not app.is_moving:
        rover.go_backward()
        app.is_moving = True

    await socket.emit("rover_status", data={'message': '[Rover] - Retrocedendo...'})


@socket.event
async def move_left(sid, data):
    logging.info("Movendo para esquerda...")

    if not app.is_moving:
        rover.go_left()
        app.is_moving = True

    await socket.emit("rover_status", data={
        'message': '[Rover] - Movendo para esquerda...'})


@socket.event
async def move_right(sid, data):
    logging.info("Movendo para direita...")
    
    if not app.is_moving:
        rover.go_right()
        app.is_moving = True

    await socket.emit("rover_status", data={
        'message': '[Rover] - Movendo para direita...'})


@socket.event
async def stop(sid, data):
    logging.info("Parando...")
    
    if app.is_moving:
        rover.stop()       
        app.is_moving = False

    await socket.emit("rover_status", data={'message': '[Rover] - Parando...'})
