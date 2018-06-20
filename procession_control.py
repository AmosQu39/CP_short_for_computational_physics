# -*- coding: utf-8 -*-

from generate_balls import add_balls
from time_axis import get_frame_nodes
from silence_balls import get_silence_list


def procession_control(balls, counter):
    frame_nodes = get_frame_nodes()
    if (counter > frame_nodes[0]) & (counter % 5 == 0)&(len(balls)<400):
        balls = add_balls(balls)
    counter = counter + 1
    return balls, counter


def procession_silence_list(counter):
    if counter > 100:
        silence_list = get_silence_list(counter)
    else:
        silence_list = []
    return silence_list


if __name__ == "__main__":
    pass
