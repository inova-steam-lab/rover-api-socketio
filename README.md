# Rover SocketIO

Interface Web para interação com o Rover (labrador) através de WebSockets.

# Comece por aqui

## Obtendo o projeto

### Via git clone
- Através do seu terminal, escolha um diretório onde você deseja colocar o projeto;
- Rode o comando: `git clone https://github.com/zNexTage/rover-socketio.git`;

### Através da interface do GitHub
- Clique em `<> code`;
- Clique em `Download Zip`;

## Criação de ambiente virtual (opcional)
Caso você não queira instalar as libs em seu computador, crie um ambiente virtual utilizando o Python para evitar que isso ocorra!
- Abra o terminal na pasta onde está o projeto;
- Digite: `python3 -m venv venv`;
- Será criado um diretório chamado `venv`;
- Rode o comando: `source venv/bin/activate`. Isso ativará o ambiente virtual! 
  - o (`venv`) em seu terminal (`(venv) christian@DESKTOP-BJHHGVF`) comprova que o ambiente virtual foi ativado.
- Enquanto o ambiente virtual estiver ativado todas as libs serão instaladas nele e não globalmente em seu computador.

## Instalando as libs
- Abra o terminal na pasta onde está o projeto;
- Rode o comando: `pip install -r requirements.txt`;

# Como rodar a aplicação?
- Abra o terminal na pasta onde está o projeto;
- Rode o comando: `uvicorn main:socketio_app --reload`;
- Acesse: http://127.0.0.1:8000/ ou http://localhost:8000/

# Conhecendo algumas partes do projeto
- `main.py` -> Aqui está localizado a configuração do servidor. É nesse arquivo onde está definido os listeners do `socket`, isto é, as funções que que possibilitam movimentar o rover.
- `rover.py` -> Configuração PWM e dos pinos da labrador. Além disso, nesse arquivo está as funções que movimentam o hover;
- `index.html` -> Apenas uma interface web para interagir com o servidor.
- `static/js/script_socketio.js` -> Através da interação do usuário na página web (http://127.0.0.1:8000/), esse script é responsável por emitir os eventos para o servidor, isto é, através da interação nessa página que o Rover é controlado.

# Referências
- https://www.reddit.com/r/FastAPI/comments/neds9c/integrate_socketio_with_fastapi/;
- https://python-socketio.readthedocs.io/en/latest/intro.html;
- https://fastapi.tiangolo.com/
