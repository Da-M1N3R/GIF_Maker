import cv2 as cv
import os

def conv_pic_to_vid(pathIn, pathOut, fps, time):
    # convert pictures to video
    font = cv.FONT_HERSHEY_SIMPLEX
    frame = []
    print(files)
    for i in range(len(files)):
        filename = pathIn + files[i]
        # Read image
        im = cv.imread(filename)
        height, width, layers = im.shape
        size = (width, height)
        # Numbers on image
        #im = cv.putText(im, str(i+1), (20, 35), font, 1, (255, 255, 255), 2)

        for j in range(time):
            frame.append(im)

    out = cv.VideoWriter(pathOut, cv.VideoWriter_fourcc(*'MJPG'), fps, size)
    for i in range(len(frame)):
        out.write(frame[i])
    out.release()

input_folder = "GIF" # Input filename
output_folder = "output" # Output filename
directory = "C:/Users/Billy/Desktop/OPDT/"

files = [f for f in os.listdir(input_folder + "/") if os.path.isfile(os.path.join(input_folder + "/", f))]
print(files)

# Parameters
pathIn = directory + input_folder + "/" # Image source
pathOut = directory + output_folder + "/" + "GIF_maker.avi" # Video output location
fps = 10
time = 1

# Functions
conv_pic_to_vid(pathIn, pathOut, fps, time)
"""
borderType = cv.BORDER_CONSTANT

im = cv.imread("img/aokiji.png")
'''
# Border setting
top = 0
bottom = left = 0
right = 400
borderColor = [0, 0, 0]
#im = cv.copyMakeBorder(im, top, bottom, left, right, borderType, None, borderColor)
'''

# Text setting
#im = cv.putText(im, "Kuzan (Aokiji)", (20, 35), font, 0.5, (255, 255, 255), 2)

cv.imshow("img", im)

cv.waitKey(0)

"""






