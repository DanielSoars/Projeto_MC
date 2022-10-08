from djitellopy import tello
import cv2

my_tello = tello.Tello()
my_tello.connect()
print(my_tello.get_battery())

my_tello.streamon()

while True:
    imagem = my_tello.get_frame_read().frame
    imagem = cv2.resize(imagem,(360, 240))
    cv2.imshow("Imagem", imagem)
    cv2.waitKey(1)
