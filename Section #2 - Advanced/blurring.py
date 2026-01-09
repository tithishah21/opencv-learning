#pylint:disable=no-member
#smooth the image / blur out the image
import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# # Averaging - avg of pixels of img
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# # Gaussian Blur - less blur than avg blue , takes avg of weights of pixels
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)
#
# # Median Blur - finds the median of surrounding pixels and used to reduce noise of the picture
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)
#
# # Bilateral - most effective used in computer vision , it applies blurring but retains the edges of the image
bilateral = cv.bilateralFilter(img, 10, 35, 25)
#img,d,color sigma - more colors, sigmaspace - pixels from how far away
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)