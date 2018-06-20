# -*- coding: utf-8 -*-
import os
import shutil
import numpy as np
from silence_balls import get_silence_possible_list


def data_init(counter, balls):
    if os.path.exists('data/frame_balls'):
        shutil.rmtree('data/frame_balls')
        os.makedirs('data/frame_balls')
    else:
        os.makedirs('data/frame_balls')
    if os.path.exists('data/silence_list'):
        shutil.rmtree('data/silence_list')
        os.makedirs('data/silence_list')
    else:
        os.makedirs('data/silence_list')
    if os.path.exists('data/collision_list'):
        shutil.rmtree('data/collision_list')
        os.makedirs('data/collision_list')
    else:
        os.makedirs('data/collision_list')
    filename = 'data/frame_balls/balls' + str(counter)+'.npy'
    np.save(filename, balls)


def write_balls_data(counter, balls):
    filename = 'data/frame_balls/balls' + str(counter)+'.npy'
    np.save(filename, balls)


def read_balls_data(counter):
    filename = 'data/frame_balls/balls' + str(counter)+'.npy'
    balls = np.load(filename)
    return balls


def write_silence_possible_list(counter, balls):
    silence_possible_list = get_silence_possible_list(balls)
    filename = 'data/silence_list/silence_possible_list' + str(counter)+'.npy'
    np.save(filename, silence_possible_list)


def write_data(counter, balls):
    write_balls_data(counter, balls)
    write_silence_possible_list(counter, balls)


def write_collision_list(collided, counter):
    filename = 'data/collision_list/collided' + str(counter)+'.npy'
    np.save(filename, collided)


def read_collision_list(counter):
    filename = 'data/collision_list/collided' + str(counter)+'.npy'
    collision_list = np.load(filename)
    return collision_list


def collided_message(collided,collided_detail):
    mid = np.array(collided).flatten()
    collisi_list = list(set(mid))
    collide_message = {}
    # pdb.set_trace()
    for i in collisi_list:
        collide_i = []
        for j in range(len(collided)):
            # pdb.set_trace()
            if collided[j][1] == i:
                collide_i.append([collided_detail[j][0],collided_detail[j][2]])

                #print(collide_message)
            elif collided[j][0] == i:
                collide_i.append([collided_detail[j][1],collided_detail[j][2]])
            collide_message[i] = collide_i
    return collide_message, collisi_list

def collided_message2(collided2):
    collisi_list2=[]
    for s in range(len(collided2)):
        collisi_list2.append(collided2[s][0])
    collide_message2 = {}
    # pdb.set_trace()
    for i in collisi_list2:
        collide_i = []
        for j in range(len(collided2)):
            # pdb.set_trace()
            if collided2[j][0] == i:
                collide_i.append([collided2[j][1],collided2[j][2]])
            collide_message2[i] = collide_i
    return collide_message2,collisi_list2
