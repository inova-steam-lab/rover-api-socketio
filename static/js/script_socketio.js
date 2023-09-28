const url = "http://localhost:8000";

const socket = io(url);

// Listeners de movimento do hover!!

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

document.addEventListener("keypress", event => {
    const keyPressed = event.key;

    switch (keyPressed) {
        case 'w': onWPress(); break;
        case 's': onSPress(); break;
        case 'a': onAPress(); break;
        case 'd': onDPress(); break;
    };
})