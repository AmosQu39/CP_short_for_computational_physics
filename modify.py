import numpy as np
import json
import math.sqrt as sqrt
from scipy import interpolate
import matplotlib.pyplot as plt

#------*get the message*------#
def get_boundary_message():
    file = open('json/boundary_message.json')
    json_data = json.load(file)
    boundary_message = json_data['boundary'][0]
    return boundary_message


def get_init_message():
    file = open('json/ball_message.json')
    json_data = json.load(file)
    ball_message = json_data['ball'][0]
    return ball_message

#------*form the grid which have power*------#
def form_grid(balls):
    boundary_message = get_boundary_message()
    xmin, xmax, ymin, ymax = list(boundary_message.values())
    r = balls['radius_'][0]
    a1=np.arange(xmin+r,xmax,r)
    b1=np.arange(ymin+r,ymax,r)
    number1=len(a1)
    number2=len(b1)
    point_power_list=np.zeros[number1][number2]
    point_x,point_y=np.meshgrid(a1,b1)
    return None


#------*rules to add power*------#
def reverse_power(positionx,positiony,pointx,pointy):
    return sqrt((positionx-pointx)**2+(positiony-pointy)**2)


#------*judge which 4 point the ball is closest to*------#
def judge_neighbourlist(balls):
    r = balls['radius_'][0]
    number_x= balls['position_x']//r
    number_y= balls['position_y']//r
    position_down=number_y*r
    position_up=position_down+r
    position_left=number_x*r
    position_right=position_left+r
    d1=reverse_power(balls['position_x'],balls['position_y'],position_down,position_left)
    d2=reverse_power(balls['position_x'],balls['position_y'],position_down,position_right)
    d3=reverse_power(balls['position_x'],balls['position_y'],position_up,position_right)
    d4=reverse_power(balls['position_x'],balls['position_y'],position_up,position_left)
    sum=d1+d2+d3+d4
    return d1/sum,d2/sum,d3/sum,d4/sum,number_x,number_y


#------*Add power to each point*------#
def cal_power(balls):
    number_of_balls=len(balls)
    for i in range(number_of_balls):
        p1,p2,p3,p4,k,t=judge_neighbourlist(balls[i])
        point_power_list[k][t]+=p1
        point_power_list[k][t+1]+=p2
        point_power_list[k+1][t+1]+=p3
        point_power_list[k+1][t]+=p4
    return None


#------*2D-interpolate*------#
def inter(x,y,point_power_list,balls):
    r = balls['radius_'][0]
    boundary_message = get_boundary_message()
    xmin, xmax, ymin, ymax = list(boundary_message.values())
    newfunc=interpolate.interp2d(x,y,point_power_list,kind='cubic')
    xnew=np.arange(xmin+r,xmax,r/20)
    ynew=np.arange(ymin+r,ymax,r/20)
    newf=newfunc(xnew,ynew)
    return newf

#-----*draw the boundary line*------#
power_to_determine_stack=0.5
boundary_list=list()
def determine_boundary(newf,xnew,ynew,power_to_determine_stack):
    number_of_column=len(newf[:,0])
    number_of_row=len(newf[0,:])
    for i in xnew:
        for j in ynew:
            if newf(i,j)>power_to_determine_stack and newf(i,j+1)<power_to_determine_stack
                boundary_list.append([i,j])
    return None



after_interpolation=inter(x,y,point_power_list,balls)

#------*eliminate the acceleration field*------#
def action_range(boundary_list,balls):
    for i in len(balls):
        















