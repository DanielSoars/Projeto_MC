from djitellopy import tello
import KeyBoardPressModule as kpm
from time import sleep

kpm.iniciar()
my_tello = tello.Tello()
my_tello.connect()
print(my_tello.get_battery())

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if kpm.getKey("LEFT"): 
        lr = -speed
    elif kpm.getKey("RIGHT"):
        lr = speed
    if kpm.getKey("UP"): 
        fb = speed
    elif kpm.getKey("DOWN"):
        fb = -speed
    if kpm.getKey("w"): 
        ud = speed
    elif kpm.getKey("s"):
        ud = -speed
    if kpm.getKey("a"): 
        yv = speed
    elif kpm.getKey("d"):
        yv = -speed
    if kpm.getKey("q"): 
        my_tello.land()
    elif kpm.getKey("e"):
        my_tello.takeoff()
        
    return [lr, fb, ud, yv]
    
while True:
    valores = getKeyboardInput()
    my_tello.send_rc_control(valores[0], valores[1], valores[2], valores[3])
    sleep(0.05)