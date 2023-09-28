import caninos_sdk as k9

labrador = k9.Labrador()


# PWM Motores
contador_tempo = 1
while contador_tempo <= 4:
    labrador.pin5.enable_pwm(
        alias="P1", freq=25, duty_cycle=0.1*contador_tempo)
    labrador.pin15.enable_pwm(
        alias="P3", freq=25, duty_cycle=0.1*contador_tempo)
    labrador.pin3.enable_pwm(
        alias="P2", freq=25, duty_cycle=0.1*contador_tempo)
    labrador.pin13.enable_pwm(
        alias="P4", freq=25, duty_cycle=0.1*contador_tempo)
    contador_tempo = contador_tempo+1


def go_forward():
    ''' Move o rover para frente '''
    labrador.P1.pwm.start()
    labrador.P3.pwm.start()
    labrador.P2.pwm.stop()
    labrador.P4.pwm.stop()


def go_backward():
    ''' Retrocede o rover '''
    labrador.P1.pwm.stop()
    labrador.P3.pwm.stop()
    labrador.P2.pwm.start()
    labrador.P4.pwm.start()


def go_left():
    ''' Vira o rover para esquerda'''
    labrador.P1.pwm.stop()
    labrador.P3.pwm.start()
    labrador.P2.pwm.start()
    labrador.P4.pwm.stop()


def go_right():
    ''' Vira o rover para direita'''
    labrador.P1.pwm.start()
    labrador.P3.pwm.stop()
    labrador.P2.pwm.stop()
    labrador.P4.pwm.start()


def stop():
    ''' Para o rover '''
    labrador.P1.pwm.stop()
    labrador.P3.pwm.stop()
    labrador.P2.pwm.stop()
    labrador.P4.pwm.stop()


# PonteH
labrador.pin7.enable_gpio(k9.Pin.Direction.OUTPUT, alias="P5")
labrador.pin11.enable_gpio(k9.Pin.Direction.OUTPUT, alias="P6")

labrador.P5.high()
labrador.P6.high()
