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
	gray_frame = cv2.cvtColor(this_frame, cv2.COLOR_BGR2GRAY)
	gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)
	
	# 3. Create a difference frame to detect changes
	diff_frame = cv2.absdiff(background, gray_frame)
	
	# 4. Create a binary threshold frame that tells us *where* the two are significantly different
	pixel_difference = 30
	thresh_frame = cv2.threshold(diff_frame, pixel_difference, 255, cv2.THRESH_BINARY)[1]

	# Our instructor used the cv2.dilate() method to dilate the picture here, but I want to try without it
	
	# 5. Find the contours in the images to see *where* the different things are
	(_, ctrs, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	
	# 6. Go through each contour
	for contour in ctrs:
		# 6b. if it's big enough to warrent being called "movement", rectangle it
		if cv2.contourArea(contour) >= 500:
			(x, y, w, h) = cv2.boundingRect(contour)
			color = (0, 255, 0)
			width = 3
			# 7. Draw rectangle
			cv2.rectangle(this_frame, (x, y), (x+w, y+h), color, width)
	
	# Show the stream
	cv2.imshow(this_frame)
	
	# Listen for key press
	key = cv2.waitKey(1)
	
	# If key pressed is "q", quit
	if key == ord("q"):
		break
	
	

# Remember this is after the loop!
cv2.destroyAllWindows()
# MAKE SURE YOU RELEASE THE STREAM
video_stream.release()