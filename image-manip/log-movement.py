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
	
	# Create a difference frame to detect changes
	diff_frame = cv2.absdiff(background, this_frame)
	
	# Create a binary threshold frame that tells us *where* the two are significantly different
	pixel_difference = 30
	thresh_frame = cv2.threshold(diff_frame, pixel_difference, 255, cv2.THRESH_BINARY)[1]







# MAKE SURE YOU RELEASE THE STREAM
video_stream.release()