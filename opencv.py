import cv2 as cv
import os

def conv_pic_to_vid(pathIn, pathOut, fps, time):
    # convert pictures to video
    frame = []
    files = [f for f in os.listdir(folderName + "/") if os.path.isfile(os.path.join(folderName + "/", f))]
    print(files)
    for i in range(len(files)):
        filename = pathIn + files[i]
        # Read image
        im = cv.imread(filename)
        height, width, layers = im.shape
        size = (width, height)

        for j in range(time):
            frame.append(im)

    out = cv.VideoWriter(pathOut, cv.VideoWriter_fourcc(*'MJPG'), fps, size)
    for i in range(len(frame)):
        out.write(frame[i])
    out.release()

folderName = "img"
directory = "C:/Users/Billy/Desktop/OPDT/" + folderName
pathIn = directory + "/"
pathOut = pathIn + "vid_test.avi"
fps = 1
time = 1

conv_pic_to_vid(pathIn, pathOut, fps, time)
'''
borderType = cv.BORDER_CONSTANT
font = cv.FONT_HERSHEY_SIMPLEX
im = cv.imread("img/aokiji.png")

# Border setting
top = 0
bottom = left = 0
right = 400
borderColor = [0, 0, 0]
im = cv.copyMakeBorder(im, top, bottom, left, right, borderType, None, borderColor)

# Text setting
im = cv.putText(im, "Kuzan (Aokiji)", (20 + 650, 35), font, 0.5, (255, 255, 255), 2)

cv.imshow("img", im)

cv.waitKey(0)


'''







