# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from generate_balls import generate_balls
from conversion import conversion_set_offsets
from motion_collision import motion, get_boundary_message, boundary_collision
from between_collision import between_collision
from time_axis import time_axis
from procession_control import procession_control, procession_silence_list
from data_write import data_init, write_data


def Show(balls):
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], frameon=False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    scatter_figure = ax.scatter(balls['position_x'],
                                balls['position_y'])
    return fig, scatter_figure


def Play(frame_number):
    global balls, counter
    silence_list = procession_silence_list(counter)
    balls, counter = procession_control(balls, counter)
    motion(balls, time_interval, silence_list)
    boundary_collision(balls, boundary_message, silence_list)
    between_collision(balls, silence_list, counter)
    position = conversion_set_offsets(balls)
    write_data(counter, balls)
    scatter_figure.set_offsets(position)


def global_variable():
    balls = generate_balls()
    fig, scatter_figure = Show(balls)
    boundary_message = get_boundary_message()
    total_time, time_interval = time_axis()
    counter = 0
    data_init(counter, balls)
    return (balls, counter,
            fig, scatter_figure,
            total_time, time_interval,
            boundary_message)


if __name__ == "__main__":
    List = global_variable()
    balls, counter = List[0], List[1]
    fig, scatter_figure = List[2], List[3]
    total_time, time_interval = List[4], List[5]
    boundary_message = List[6]
    animation = FuncAnimation(fig, Play, frames=int(total_time/time_interval),
                              interval=200*time_interval, repeat=False)
    plt.show()
