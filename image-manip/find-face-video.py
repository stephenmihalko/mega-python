import cv2

stream = cv2.VideoCapture(0)
face_cas = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    check, frame = stream.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cas.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    cv2.imshow("Video Stream", frame)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cv2.destroyAllWindows()
stream.release()
