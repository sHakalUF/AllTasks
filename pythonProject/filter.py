from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
imageArray = np.array(img)

gradation_num = int(input("Введиьте значение градации "))
mosaic_size = int(input("Введите размеры мозаики "))


def task3(image_array):
    """
    >>> task3(imageArray)
    Test completed successfully
    """

    line_len = len(image_array)
    column_len = len(image_array[0])
    grey_step = 256 // gradation_num
    for i in range(0, line_len, mosaic_size):
        for j in range(0, column_len, mosaic_size):
            count = np.sum(image_array[i:i + mosaic_size, j:j + mosaic_size])
            count = int(count // 3 // mosaic_size // mosaic_size) // grey_step * grey_step
            image_array[i:i + mosaic_size, j:j + mosaic_size] = count
    print("Test completed successfully")


res = Image.fromarray(imageArray)
res.save('res.jpg')

if __name__ == "__main__":
    import doctest

    doctest.testmod()
