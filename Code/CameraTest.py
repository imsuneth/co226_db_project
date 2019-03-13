import cv2
import requests
import numpy as np

while (True):
    url = "http://192.168.8.100:8080/shot.jpg"

    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    cv2.imwrite(filename='img2.png', img=img)
    #cv2.imshow("cam", img)

    break
