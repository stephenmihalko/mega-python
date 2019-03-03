import cv2

#filename = "uganda.jpg"
filename = "business.jpg"

# Read the picture in color so we can display in color
pic = cv2.imread(filename, 1)

cv2.imshow("Business People", pic)
