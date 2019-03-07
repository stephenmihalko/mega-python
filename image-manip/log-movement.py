# A script to detect movement on the webcam and log the times at which movement was found.

import cv2

# Get the video stream from the webcam
video_stream = cv2.VideoCapture(0)

# 1. Store the first frame of the video as a background
check, background = video_stream.read()

# 1b. Gray the background frame
background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)

# 2. Gaussian blur the background to smooth it
background = cv2.GaussianBlur(background, (21, 21), 0)

# Now loop through the rest of the frames
while True:
	
	# Get the frame, grayscale it, smooth it
	check, this_frame = video_stream.read()
	this_frame = cv2.cvtColor(this_frame, cv2.COLOR_BGR2GRAY)
	this_frame = cv2.GaussianBlur(this_frame, (21, 21), 0)













# MAKE SURE YOU RELEASE THE STREAM
video_stream.release()