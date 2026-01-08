import cv2 as cv
#rescaling img
# img = cv.imread('../Resources/Photos/cat_large.jpg')
# cv.imshow('Cat', img)
def rescaleFrame(frame, scale=0.75):
    width = int( frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

#Resizing videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()

    if not isTrue:
        break
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('t'):
        break
        #if letter t is pressed then the video is terminated.

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)
