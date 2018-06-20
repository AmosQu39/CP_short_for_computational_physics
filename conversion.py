# -*- coding: utf-8 -*-

import numpy as np

def conversion_set_offsets(balls):
    position_x = balls['position_x'].reshape(len(balls), 1)
    position_y = balls['position_y'].reshape(len(balls), 1)
    position = np.hstack((position_x, position_y))
    return position


def conversion_divide(set_list, subset_list):
    divide_list = [i for i in set_list if i not in subset_list]
    return divide_list


def get_action_list(balls, silence_list):
    total_list = range(len(balls))
    action_list = conversion_divide(total_list, silence_list)
    return action_list


def deal_pretreat_list(pretreat_list):
    silence_set = set(pretreat_list[0])
    for i in range(1, len(pretreat_list)):
        other_set = set(pretreat_list[i])
        silence_set = silence_set & other_set
    return list(silence_set)

