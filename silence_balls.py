# -*- coding: utf-8 -*-

import numpy as np
from conversion import deal_pretreat_list


def get_silence_possible_list(balls):
    silence_possible_list = []
    for i in range(len(balls)):
        ve_i_x = balls['velocity_x'][i]
        ve_i_y = balls['velocity_y'][i]
        ve_i = np.sqrt(ve_i_x**2+ve_i_y**2)
        if ve_i < 10**(-2):
            silence_possible_list.append(i)
    return silence_possible_list


def read_silence_possible_list(counter):
    filename = 'data/silence_list/silence_possible_list' + str(counter)+'.npy'
    silence_possible_list = np.load(filename)
    return silence_possible_list


def get_silence_list(counter):
    pretreat_list = []
    for i in range(counter-10, counter):
        silence_possible_list = read_silence_possible_list(counter)
        pretreat_list.append(silence_possible_list)
    silence_list = deal_pretreat_list(pretreat_list)
    return silence_list


if __name__ == "__main__":
    silence_list = get_silence_list(900)
