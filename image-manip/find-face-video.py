import cv2

stream = cv2.VideoCapture(0)

while True:
    check, frame = stream.read()
    cv2.imshow("Video Stream", frame)
    key = cv2.waitKey(10)

    if key == ord("q"):
        break

cv2.destroyAllWindows()
stream.release()
