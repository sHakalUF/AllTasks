from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
imageArray = np.array(img)
lineLen = len(imageArray)
columnLen = len(imageArray[1])


def task3(gradation_num=5, mosaic_size=10   ):
    greyStep = 256 // gradation_num
    i = 0
    while i < lineLen - 1:
        j = 0
        while j < columnLen - 1:
            count = 0
            for n in range(i, i + mosaic_size):
                for k in range(j, j + mosaic_size):
                    red = imageArray[n][k][0]
                    green = imageArray[n][k][1]
                    blue = imageArray[n][k][2]
                    color = (int(red) + int(green) + int(blue)) // 3
                    count += color

            count = int(count // 100)
            for n in range(i, i + mosaic_size):
                for k in range(j, j + mosaic_size):
                    imageArray[n][k][0] = int(count // greyStep) * greyStep
                    imageArray[n][k][1] = int(count // greyStep) * greyStep
                    imageArray[n][k][2] = int(count // greyStep) * greyStep
            j = j + mosaic_size
        i = i + mosaic_size
    res = Image.fromarray(imageArray)
    res.save('res.jpg')


task3()
