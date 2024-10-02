from PIL import Image
import numpy as np
import requests as rq

dict_urls = {
    (1, 'im_url_rq'): 'https://requests.readthedocs.io/en/latest/_static/requests-sidebar.png',
    (2, 'im_url_np'): 'https://numpy.org/doc/stable/_static/numpylogo.svg',
    (3, 'im_url_pil'): 'https://pillow.readthedocs.io/en/stable/_static/pillow-logo.png'
}

'''
REQUESTS
'''

for key, item in dict_urls.items():
    key = key[0]

    image = rq.get(item)
    print(type(image))

    with open(f'image{key}.{item[-3:]}', 'wb') as file:
        file.write(image.content)

'''
REQUESTS
'''

'''
PILLOW
'''


def show_image_info(name_image):
    """Идентифицирует атрибуты формата, размера и режима"""
    im = Image.open(name_image)  # модуль Image, функция open - присвоить(загрузить) в переменную изображение
    return im.format, im.size, im.mode  # Вывод информации о изображении


def show_image(name_image):
    """Выводит изображение на экран"""
    im = Image.open(name_image)
    im.show()  # Открытие изображения для просмотра


def cut_image(name_image, save_image_name, *params):
    """Обрезает изображение по заданным параметрам и сохраняет его"""
    im = Image.open(name_image)
    im = im.crop(params)  # Обрезает по заданным параметрам
    im.save(save_image_name)  # Сохраняет в текущую директорию
    im.show()


def rotate_image(name_image, save_image_name, degree):
    """Поворачивает изображение на заданный угол и сохраняет его"""
    im = Image.open(name_image)
    im = im.rotate(degree)
    im.save(save_image_name)
    im.show()


def transpose_image(name_image, save_image_name):
    """Отзеркаливает изображение и сохраняет его"""
    im = Image.open(name_image)
    im = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    im.save(save_image_name)
    im.show()


def merge(name_image1, name_image2, save_image_name):
    """Объединяет два изображения и сохраняет результат"""
    im1 = Image.open(name_image1)
    im2 = Image.open(name_image2)

    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))

    im.save(save_image_name)
    im.show()


'''
PILLOW
'''

'''
NumPy
'''


def array_operations():
    """Операции NumPy."""
    # 1. Creating a NumPy array
    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Created Array:\n", array)

    # 2. Performing mathematical operations
    sum_array = np.sum(array)
    mean_array = np.mean(array)
    print("Sum of Array:", sum_array)
    print("Mean of Array:", mean_array)

    # 3. Reshaping the array
    reshaped_array = array.reshape(1, 9)
    print("Reshaped Array:\n", reshaped_array)


array_operations()
'''
NumPy
'''

info = show_image_info('image3.png')
print(info)
show_image('image3.png')
cut_image('image3.png', 'image3_crop.png', 0, 0, 65, 71)
transpose_image('image3_crop.png', 'image3_transposed.png')
merge('image3.png', 'image3_transposed.png', 'fital_res.png')