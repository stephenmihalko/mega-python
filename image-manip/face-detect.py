import cv2

filename = "uganda.jpg"
#filename = "me.jpg"

# Read the picture in color so we can display in color
pic = cv2.imread(filename, 1)

# Load the "what a face looks like" file
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Convert to grayscale
gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

# Find faces - this returns a list of tuples [(x, y, w, h), (x, y, w, h), ...]
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Go through each tuple in the list and add the rectangle
for x, y, w, h in faces:
    cv2.rectangle(pic, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow(filename, pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
