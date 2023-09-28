const url = "http://localhost:8000";

const socket = io(url);

/**
 * Obtém as divs referente as teclas W, S, A e D.
 */
const keyWDiv = document.getElementById("key-w");
const keySDiv = document.getElementById("key-s");
const keyADiv = document.getElementById("key-a");
const keyDDiv = document.getElementById("key-d");

/**************
 * Emitters de movimento do Rover! Todas as vezes que uma tecla é pressionada é emitido um evento no 
 * servidor.
 **************/

/**
 * Invoca o evento `move_forward` que foi declarado no servidor quando o usuário
 * pressiona a tecla W.
 */
const onWPress = () => {
    socket.emit("move_forward", null);

    // Altera a cor da tecla W para demonstrar que ela está sendo pressionada
    keyWDiv.classList.add("key-button-dark-gray");
}

/**
 * Invoca o evento `move_backward` que foi declarado no servidor quando o usuário
 * pressiona a tecla S.
 */
const onSPress = () => {
    socket.emit("move_backward", null);

    // Altera a cor da tecla S para demonstrar que ela está sendo pressionada    
    keySDiv.classList.add("key-button-dark-gray");
}

/**
 * Invoca o evento `move_left` que foi declarado no servidor quando o usuário
 * pressiona a tecla A.
 */
const onAPress = () => {
    socket.emit("move_left", null);

    // Altera a cor da tecla A para demonstrar que ela está sendo pressionada
    keyADiv.classList.add("key-button-dark-gray");
}

/**
 * Invoca o evento `move_right` que foi declarado no servidor quando o usuário
 * pressiona a tecla D.
 */
const onDPress = () => {
    socket.emit("move_right", null);

    // Altera a cor da tecla D para demonstrar que ela está sendo pressionada
    keyDDiv.classList.add("key-button-dark-gray");
}

/**
 * Listener para evento keypress. Será chamado sempre quando o usuário pressionar uma tecla.
 */
document.addEventListener("keypress", event => {
    const keyPressed = event.key;

    switch (keyPressed) { 
        case 'w': onWPress(); break;
        case 's': onSPress(); break;
        case 'a': onAPress(); break;
        case 'd': onDPress(); break;
    };
});

/**
 * Listener para evento keydown. Será chamado sempre quando o usuário soltar uma tecla.
 */
document.addEventListener("keyup", event => {
    socket.emit("stop", null);

    // Retorna a cor original das teclas após solta-lá.
    keyWDiv.classList.remove("key-button-dark-gray");
    keySDiv.classList.remove("key-button-dark-gray");
    keyADiv.classList.remove("key-button-dark-gray");
    keyDDiv.classList.remove("key-button-dark-gray");
});

/**************
 * Listeners de eventos enviados pelo servidor.
 *************/

/**
 * rover_status é emitido pelo servidor todas as vezes que o Rover realiza uma ação.  
 */
socket.on("rover_status", data => {
    const txtLogMoviment = document.getElementById("txtLogHoverMovment");

    const currentValue = txtLogMoviment.value;

    // Concatena o valor atual do campo texto com o status enviado pelo servidor.
    txtLogMoviment.value = `${currentValue}\n${data.message}`;

    // Realiza o scroll do textarea para que ele sempre demonstre as mensagens mais recentes.
    txtLogMoviment.scrollTop = txtLogMoviment.scrollHeight;        
});