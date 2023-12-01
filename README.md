# Rover SocketIO

API em tempo real que atua escutando os eventos enviados pelo usuário através do navegador. Através de uma página web que a API disponibiliza, um usuário poderá emitir comandos, como pressionar as teclas: W, A, S e D, para controlar o rover. A API se encarrega de escutar esses eventos e de disparar outros eventos que são executados na placa Labrador que interagem diretamente com as portas PWM para que o rover possa se movimentar (a interação com as portas PWM são realizadas no projeto [https://github.com/labrador-rover/rover-remote-control](rover-remote-control)).

# Comece por aqui

## Anote o IP da sua Labrador
O IP da sua labrador será necessário para realizar a configuração da comunicação.
- Abra seu terminal;
- Digite: `ip a | grep -oE 'inet [0-9.]+'`;
  - Idealmente o retorno desse comando será:
      `inet 127.0.0.1
       inet 192.168.1.6`
  - Anote a segunda opção.

## Obtendo o projeto

### Via git clone
- Através do seu terminal, escolha um diretório onde você deseja colocar o projeto;
- Rode o comando: `git clone https://github.com/zNexTage/rover-socketio.git`;

### Através da interface do GitHub
- Na página do projeto: https://github.com/zNexTage/rover-socketio/tree/main;
- Procure e clique em `<> code` (Botão verde);
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

## Configuração comunicação SocketIO Javascript com API
Para que a interface funcione corretamente, é preciso colocar o IP da sua labrador no `script_socketio.js`;
- Abra o arquivo `script_socketio.js`;
- Procure pela linha `const url = "http://192.168.1.6:8000/";`;
- Altere `http://192.168.1.6:8000/` para o **IP da sua labrador**.
  - `const url = "http://<IP-DA-SUA-LABRADOR>:8000/";`

## Como rodar a aplicação?
- Abra o terminal na pasta onde está o projeto;
- Rode o comando: `uvicorn main:socketio_app --reload --host 0.0.0.0`;
- Acesse: http://127.0.0.1:8000/ ou http://localhost:8000/ ou http://<IP-DA-LABRADOR>:8000/

## Conhecendo algumas partes do projeto
- `main.py` -> Aqui está localizado a configuração do servidor. É nesse arquivo onde está definido os listeners do `socket`, isto é, as funções que possibilitam movimentar o rover.
- `rover.py` -> Configuração PWM e dos pinos da labrador. Além disso, nesse arquivo está as funções que movimentam o hover;
- `index.html` -> Apenas uma interface web para interagir com o servidor.
- `static/js/script_socketio.js` -> Através da interação do usuário na página web (http://127.0.0.1:8000/), esse script é responsável por emitir os eventos para o servidor, isto é, através da interação nessa página que o Rover é controlado.

# Problemas identificados na labrador

## Pip não localizado
Caso a labrador não reconheça o comando: `pip`, rode os seguintes comandos no terminal:
  - `sudo apt clean`;
  - `sudo apt update`;
  - `sudo apt install --fix-missing`;
  - `sudo apt -y upgrade`;
  - `sudo apt-get install python3-venv`;

# Referências
- https://www.reddit.com/r/FastAPI/comments/neds9c/integrate_socketio_with_fastapi/;
- https://python-socketio.readthedocs.io/en/latest/intro.html;
- https://fastapi.tiangolo.com/
- https://stackoverflow.com/questions/73335010/how-to-set-fastapi-websocket-properly-with-nginx
- https://dylancastillo.co/fastapi-nginx-gunicorn/#tech-stack
