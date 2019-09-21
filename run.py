# coding:utf-8
import os
import configparser
from PIL import Image

if __name__ == '__main__':
    print("start!")
    # 读取logo原图
    logo = Image.open('logo.png')
    config = configparser.ConfigParser()
    config.read('app/icon.ini')
    # 创建存图文件夹
    try:
        os.mkdir('icons')
    except IOError as e:
        print(e)
    os.chdir('icons')
    # 读取所有icon尺寸
    icons = config.items('icon')
    # print(config.items('icon'))
    for icon in icons:
        name = icon[0]
        size = icon[1]  # str
        size = tuple(eval(size))   # tuple
        # 采样影响图形边缘平滑程度
        image = logo.resize(size=size, resample=Image.HAMMING)
        image.save('%s.png' % name, 'png')
    print('done!')
