from djitellopy import tello
from time import sleep

my_tello = tello.Tello()
my_tello.connect()
print(my_tello.get_battery())
my_tello.takeoff()
my_tello.send_rc_control(0, 50, 0, 0)
sleep(2)
my_tello.send_rc_control(0, 0, 0, 0)
my_tello.land()
