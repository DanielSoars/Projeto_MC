from djitellopy import tello
from time import sleep

my_tello = tello.Tello()
my_tello.connect()
print(my_tello.get_battery())
