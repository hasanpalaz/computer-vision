# Import numpy and OpenCV
import numpy as np
import cv2
import imutils
print (cv2.__version__)

# Load a color image in grayscale
image = cv2.imread('sample.jpg',0)
print(image.shape)
cv2.imshow("Gray scale sample.jpg", image)
cv2.waitKey(0)

# Load a color image in BGR
# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
image = cv2.imread('sample.jpg')
(h, w, d) = image.shape
print(image.shape)
print("width={}, height={}, depth={}".format(w, h, d))
cv2.imshow("sample.jpg", image)
cv2.waitKey(0)

# Load an color image in BGR
image = cv2.imread('sample.jpg')
# Assigning the image stored in numpy array img to
# another numpy array img_copy
img_copy = image.copy()
# Copies from rows 150 to 250 and columns 150 to 350
cropped_image = image[150:250,150:350]
# Find the number of rows in the cropped image
imgRows = cropped_image.shape[0]
# Find the number of columns in the cropped image
imgCols = cropped_image.shape[1]
# Find the number of channels in the cropped image
Channels = cropped_image.shape[2]
print (imgRows, imgCols, Channels)
cv2.imshow("cropped image", cropped_image)
cv2.waitKey(0)

# convert color image to gray
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save result
cv2.imwrite("sample_image_gray.jpg", gray_image)

# Display image
cv2.imshow("image", image)
cv2.imshow("gray image", gray_image)

# Wait for a keystroke in the window
cv2.waitKey(0)

# Load an color image in BGR
image_b = cv2.imread('sample.jpg', 1)
cv2.imshow("image blue", image_b)
# Wait for a keystroke in the window
cv2.waitKey(0)
image_g = cv2.imread('sample.jpg', 2)
cv2.imshow("image green", image_g)
# Wait for a keystroke in the window
cv2.waitKey(0)
image_r = cv2.imread('sample.jpg', 3)
cv2.imshow("image red", image_r)
# Wait for a keystroke in the window
cv2.waitKey(0)

# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("jp.png")
(h, w, d) = image.shape
print(image.shape)
print("width={}, height={}, depth={}".format(w, h, d))

# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
cv2.imshow("jp.png", image)
cv2.waitKey(0)

# access the RGB pixel located at x=50, y=100, keepind in mind that
# OpenCV stores images in BGR order rather than RGB
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=320,y=60 at ending at x=420,y=160
roi = image[60:160, 320:420]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# resize the image to 200x200px, ignoring aspect ratio
resized = cv2.resize(image, (200, 200))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)

# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)

# manually computing the aspect ratio can be a pain so let's use the
# imutils library instead
resized = imutils.resize(image, width=300)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)

# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)

# rotation can also be easily accomplished via imutils with less code
rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)

# OpenCV doesn't "care" if our rotated image is clipped after rotation
# so we can instead use another imutils convenience function to help
# us out
rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated)
cv2.waitKey(0)

# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

# draw a 2px thick red rectangle surrounding the face
output = image.copy()
cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150
output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1)
cv2.imshow("Circle", output)
cv2.waitKey(0)

# draw a 5px thick red line from x=60,y=20 to x=400,y=200
output = image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)

# draw green text on the image
output = image.copy()
cv2.putText(output, "OpenCV + Jurassic Park!!!", (10, 25),
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)