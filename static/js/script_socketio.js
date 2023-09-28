const url = "http://localhost:8000";

const socket = io(url);

/**************
 * Emitters de movimento do hover! Todas as vezes que uma tecla é pressionada é emitido um evento no 
 * servidor.
 **************/

/**
 * Invoca o evento `move_forward` que foi declarado no servidor quando o usuário
 * pressiona a tecla W.
 */
const onWPress = () => {
    socket.emit("move_forward", null);
}

/**
 * Invoca o evento `move_backward` que foi declarado no servidor quando o usuário
 * pressiona a tecla S.
 */
const onSPress = () => {
    socket.emit("move_backward", null);
}

/**
 * Invoca o evento `move_left` que foi declarado no servidor quando o usuário
 * pressiona a tecla A.
 */
const onAPress = () => {
    socket.emit("move_left", null);
}

/**
 * Invoca o evento `move_right` que foi declarado no servidor quando o usuário
 * pressiona a tecla D.
 */
const onDPress = () => {
    socket.emit("move_right", null);
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
});

/**************
 * Listeners de eventos enviados pelo servidor.
 *************/

/**
 * hover_status é emitido pelo servidor todas as vezes que o hover realiza uma ação.  
 */
socket.on("hover_status", data => {
    const txtLogMoviment = document.getElementById("txtLogHoverMovment");

    const currentValue = txtLogMoviment.value;

    // Concatena o valor atual do campo texto com o status enviado pelo servidor.
    txtLogMoviment.value = `${currentValue}\n${data.message}`;

    // Realiza o scroll do textarea para que ele sempre demonstre as mensagens mais recentes.
    txtLogMoviment.scrollTop = txtLogMoviment.scrollHeight;
});