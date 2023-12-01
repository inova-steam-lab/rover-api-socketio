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

    # Invoca o método rover_move_forward no carrinho para que ele mova para frente.
    await socket.emit("rover_move_forward", {})

    # Invoca o método rover_status no navegador para indicar que o carrinho está se movendo
    await socket.emit("rover_status", data={'message': '[Rover] - Movendo...'})


@socket.event
async def move_backward(sid, data):
    logging.info("Retrocedendo...")
    
    # Invoca o método rover_move_forward no carrinho para que ele retroceda
    await socket.emit("rover_move_backward", {})

    # Invoca o método rover_status no navegador para indicar que o carrinho está se movendo
    await socket.emit("rover_status", data={'message': '[Rover] - Retrocedendo...'})


@socket.event
async def move_left(sid, data):
    logging.info("Movendo para esquerda...")

    # Invoca o método rover_move_left no carrinho para que ele vire para esquerda
    await socket.emit("rover_move_left", {})

    # Invoca o método rover_status no navegador para indicar que o carrinho está se movendo
    await socket.emit("rover_status", data={
        'message': '[Rover] - Movendo para esquerda...'})


@socket.event
async def move_right(sid, data):
    logging.info("Movendo para direita...")
    
    # Invoca o método rover_move_right no carrinho para que ele vire para direita
    await socket.emit("rover_move_right", {})

    # Invoca o método rover_status no navegador para indicar que o carrinho está se movendo
    await socket.emit("rover_status", data={
        'message': '[Rover] - Movendo para direita...'})


@socket.event
async def stop(sid, data):
    logging.info("Parando...")
    
    # Invoca o método rover_stop no carrinho para que pare
    await socket.emit("rover_stop", {})

    # Invoca o método rover_status no navegador para indicar que o carrinho está parando
    await socket.emit("rover_status", data={'message': '[Rover] - Parando...'})
