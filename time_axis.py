# -*- coding: utf-8 -*-

import json


def get_time_axis():
    file = open('json/time_axis_message.json')
    json_data = json.load(file)
    time_axis_message = json_data['time_axis'][0]
    return time_axis_message


def time_axis():
    time_axis_message = get_time_axis()
    total_time = time_axis_message['total_time']
    time_interval = time_axis_message['time_interval']
    return total_time, time_interval


def get_time_nodes():
    time_axis_message = get_time_axis()
    time_nodes = []
    for i in range(2, len(time_axis_message)):
        time_nodes.append(time_axis_message['time_node_'+str(i-1)])
    return time_nodes


def get_frame_nodes():
    total_time, time_interval = time_axis()
    time_nodes = get_time_nodes()
    frame_nodes = []
    for i in range(len(time_nodes)):
        frame_number_now = time_nodes[i]/time_interval
        frame_nodes.append(frame_number_now)
    frame_nodes.append(total_time/time_interval)
    return frame_nodes


if __name__ == "__main__":
    frame_nodes = get_frame_nodes()
