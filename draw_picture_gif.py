# -*- coding: utf-8 -*-

import os
import shutil
import imageio
import numpy as np
import matplotlib.pyplot as plt


def draw_init():
    if os.path.exists('pictures/balls'):
        shutil.rmtree('pictures/balls')
        os.makedirs('pictures/balls')
    else:
        os.makedirs('pictures/balls')
    if os.path.exists('pictures/balls'):
        shutil.rmtree('pictures/balls')
        os.makedirs('pictures/balls')
    else:
        os.makedirs('pictures/balls')


def read_balls_data(counter):
    filename = 'data/frame_balls/balls' + str(counter)+'.npy'
    balls = np.load(filename)
    return balls


def draw_one_pictures(counter, balls):
    filename = 'pictures/balls/balls_scatter' + str(counter)+'.png'
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], frameon=False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.scatter(balls['position_x'], balls['position_y'])
    plt.savefig(filename)
    plt.close('all')


def draw_pictures():
    draw_init()
    length = len([i for i in os.listdir('data/frame_balls')])
    for i in range(length):
        balls = read_balls_data(i)
        draw_one_pictures(i, balls)


def create_gif():
    frames = []
    path = 'pictures/balls'
    pngfiles = os.listdir(path)
    image_list = [os.path.join(path, f) for f in pngfiles]
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave('balls.gif', frames, 'GIF', duration=0.005)


if __name__ == "__main__":
    pass
