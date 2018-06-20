# -*- coding: utf-8 -*-

import numpy as np
import json


def get_init_message():
    file = open('json/ball_message.json')
    json_data = json.load(file)
    ball_message = json_data['ball'][0]
    return ball_message


def generate_one_ball():
    ball_message = get_init_message()
    ball_feature = ['position_x',
                    'position_y',
                    'velocity_x',
                    'velocity_y',
                    'radius_']
    ball_feature1 = ['position_x',
                    'position_y',
                    'velocity_y',
                    'radius_']
    dtype = [(ball_feature[i], float) for i in range(len(ball_feature))]
    ball = np.zeros(1, dtype=dtype)
    for i in ball_feature1:
        ball[i] = np.random.uniform(ball_message[i+'min'],
                                    ball_message[i+'max'])
    return ball


def generate_balls(n_balls=5):
    for i in range(n_balls):
        if i == 0:
            balls = generate_one_ball()
        else:
            ball = generate_one_ball()
            balls = np.concatenate([balls, ball])
    return balls


def add_balls(balls):
    add_balls = generate_balls(1)
    balls = np.concatenate([balls, add_balls])
    return balls
