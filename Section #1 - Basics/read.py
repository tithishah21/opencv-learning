#pylint:disable=no-member

import cv2 as cv

#Reading images
# img = cv.imread('../Resources/Photos/cat_large.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)
# #keeps the image window open till any key is pressed


# Reading Videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')
#webcam is referenced by using integer 0 , and to read an alr existing video is done by providing path to video
while True:
    isTrue, frame = capture.read()

    if not isTrue:
        break

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('t'):
        break
        #if letter t is pressed then the video is terminated.

capture.release()
cv.destroyAllWindows()