from PIL import Image
import os
import math
import numpy as np
from time import sleep
import glob
import shutil


main_path = os.getcwd()
print(main_path)
rotated = []
folders = ['jpgs', 'middle', 'square', 'output']

for elem in folders:
    shutil.rmtree(f'{main_path}/{elem}')
    os.mkdir(f'{main_path}/{elem}')

c = input('Меняем дефолтные настройки? ')
if c == '1':
    edge = int(input('Какой процент от длины наибольшей стороны составляет длина края? - Натуральное число '))
    color = [int(elem) for elem in input('Какого цвета края? - Три целых числа от 0 до 255 через пробел в формате r g b ').split()]
else:
    edge = 5
    color = [255, 255, 255]

'''
for f in os.listdir('input/.'):
    if f.endswith('.png'):
        fn, type_ = os.path.splitext(f)
        rgba_image = Image.open(f'input/{f}')
        rgba_image.load()
        background = Image.new("RGB", rgba_image.size, (255, 255, 255))
        background.paste(rgba_image, mask = rgba_image.split()[3])
        background.save(f'{main_path}/jpgs/{fn}.jpg', "JPEG", quality=100)
        print('done')
    elif f.endswith('.JPG') or f.endswith('.jpg') or f.endswith('.jpeg'):
        fn, type_ = os.path.splitext(f)
        im = Image.open(f)
        im.save(f'{main_path}/jpgs/{fn}.jpg')
       
'''

for f in os.listdir('input/.'):
    if f.endswith('.JPG') or f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png'):
        fn, type_ = os.path.splitext(f)
        im = Image.open(f'input/{f}')
        width, height = im.size
        print(width, height)
        if height > width:
            im = im.rotate(90, Image.NEAREST, expand = 1)
            im.save(f'{main_path}/middle/{fn}.jpg')
            rotated.append(fn)
            print('added')
        else:
            im.save(f'{main_path}/middle/{fn}.jpg')
            print('not')

for f in os.listdir('middle/.'):
    if f.endswith('.JPG') or f.endswith('.jpg') or f.endswith('.jpeg'):
        fn, type_ = os.path.splitext(f)
        im = Image.open(f'middle/{f}')
        width, height = im.size
        arr = np.array(im)
        white_strip = np.asarray([[color for i in range(width)] for j in range((width - height)//2 + int(width * (edge / 100)))])
        arr = np.vstack((white_strip, arr, white_strip))
        arr = np.uint8(arr)
        photo = Image.fromarray(arr)
        photo.rotate(-90, Image.NEAREST, expand = 1).save(f'{main_path}/square/{fn}.jpg')


for f in os.listdir('square/.'):
    if f.   endswith('.JPG') or f.endswith('.jpg') or f.endswith('.jpeg'):
        fn, type_ = os.path.splitext(f)
        im = Image.open(f'square/{f}')
        width, height = im.size
        arr = np.array(im)
        white_strip = np.asarray([[color for i in range(width)] for j in range(int(height * (edge / 100)))])
        arr = np.vstack((white_strip, arr, white_strip))
        arr = np.uint8(arr)
        photo = Image.fromarray(arr)
        if fn not in rotated:
            photo.rotate(90, Image.NEAREST, expand = 1).save(f'{main_path}/output/{fn}.jpg')
        else:
            photo.save(f'{main_path}/output/{fn}.jpg')
        print('success')

print(rotated)
        







        

