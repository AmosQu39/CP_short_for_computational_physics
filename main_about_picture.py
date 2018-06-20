# -*- coding: utf-8 -*-

from generate_balls import generate_balls
from motion_collision import motion, get_boundary_message, boundary_collision
from between_collision import between_collision
from time_axis import time_axis
from procession_control import procession_control, procession_silence_list
from data_write import data_init, write_data


def Play(balls, counter, time_interval, boundary_message):
    silence_list = procession_silence_list(counter)
    balls, counter = procession_control(balls, counter)
    motion(balls, time_interval, silence_list)
    boundary_collision(balls, boundary_message, silence_list)
    between_collision(balls, silence_list)
    write_data(counter, balls)
    return balls, counter


def get_variable():
    balls = generate_balls()
    boundary_message = get_boundary_message()
    total_time, time_interval = time_axis()
    counter = 0
    data_init(counter, balls)
    return balls, counter, total_time, time_interval, boundary_message


def Main():
    List = get_variable()
    balls, counter = List[0], List[1]
    total_time, time_interval = List[2], List[3]
    boundary_message = List[4]
    for i in range(int(total_time/time_interval)):
        balls, counter = Play(balls, counter, time_interval, boundary_message)


if __name__ == "__main__":
    Main()
