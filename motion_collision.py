# -*- coding: utf-8 -*-

import json
from conversion import get_action_list


def gravity_acceleration(balls, time_interval):
    g = 9.8
    return -g*time_interval


def motion(balls, time_interval, silence_list=[]):
    action_list = get_action_list(balls, silence_list)
    for i in action_list:
        balls['velocity_y'][i] += gravity_acceleration(balls, time_interval)
        balls['position_x'][i] += balls['velocity_x'][i]*time_interval
        balls['position_y'][i] += balls['velocity_y'][i]*time_interval
    return balls


def get_boundary_message():
    file = open('json/boundary_message.json')
    json_data = json.load(file)
    boundary_message = json_data['boundary'][0]
    return boundary_message


def boundary_collision(balls, boundary_message, silence_list=[]):
    loss_about_x = 0.1
    loss_about_y = 0.1
    action_list = get_action_list(balls, silence_list)
    for i in action_list:
        po_x, po_y, ve_x, ve_y, ra = balls[i]
        xmin, xmax, ymin, ymax = list(boundary_message.values())
        if (po_x - ra) <= xmin:
            ve_x = -ve_x*loss_about_x
            po_x = xmin + ra
        elif (po_x + ra) >= xmax:
            ve_x = -ve_x*loss_about_x
            po_x = xmax - ra
        if (po_y - ra) <= ymin:
            ve_y = -ve_y*loss_about_y
            ve_x= 0.1*ve_x*loss_about_x
            po_y = 2*ra - po_y
        elif (po_y + ra) >= ymax:
            ve_y = -ve_y*loss_about_y
            po_y = ymax-ra
        balls[i] = (po_x, po_y, ve_x, ve_y, ra)
    return balls
