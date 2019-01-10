import cv2


def main():
    cam=cv2.VideoCapture(0)
    frame= cam.read()[1]

    cv2.imwrite(filename='img2.jpg',img=frame)
main()