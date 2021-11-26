from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
imageArray = np.array(img)


def task3(image_array, gradation_num=5, mosaic_size=10):
    line_len = len(image_array)
    column_len = len(image_array[0])
    grey_step = 256 // gradation_num
    for i in range(0, line_len, mosaic_size):
        for j in range(0, column_len, mosaic_size):
            count = np.sum(image_array[i:i + mosaic_size, j:j + mosaic_size])
            count = int(count // 3 // mosaic_size // mosaic_size) // grey_step * grey_step
            image_array[i:i + mosaic_size, j:j + mosaic_size] = count


task3(imageArray, 2, 12)

res = Image.fromarray(imageArray)
res.save('res.jpg')
