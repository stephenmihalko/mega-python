import cv2

# Get the video stream from the webcam
stream = cv2.VideoCapture(0)
# Load the front face cascade XML
face_cas = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    # Get a video frame from the stream
    check, frame = stream.read()
    # Grayscale it to find the face
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Find the faces
    faces = face_cas.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    # Loop through all the faces and draw rectangles
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    # Show the stream
    cv2.imshow("Video Stream", frame)
    key = cv2.waitKey(1)
    
    # Break the loop if the user presses "Q"
    if key == ord("q"):
        break

cv2.destroyAllWindows()
stream.release()
