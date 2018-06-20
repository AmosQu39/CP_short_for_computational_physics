import numpy as np
import json
import math.sqrt as sqrt
from scipy import interpolate


def get_boundary_message():
    file = open('json/boundary_message.json')
    json_data = json.load(file)
    boundary_message = json_data['boundary'][0]
    return boundary_message


boundary_message=get_boundary_message()
xmin, xmax, ymin, ymax = list(boundary_message.values())


def get_init_message():
    file = open('json/ball_message.json')
    json_data = json.load(file)
    ball_message = json_data['ball'][0]
    return ball_message

r = balls['radius_'][0]
a1=np.arange(xmin+r,xmax,r)
b1=np.arange(ymin+r,ymax,r)

number1=len(a1)
number2=len(b1)
point_power_list=np.zeros[number1][number2]
point_x,point_y=np.meshgrid(a1,b1)

def reverse_power(positionx,positiony,pointx,pointy):
    return sqrt((positionx-pointx)**2+(positiony-pointy)**2)

def cal_power(number_x,number_y):
    for i in range(balls):
        p1,p2,p3,p4,k,t=judge_neighbourlist(balls)
        point_power_list[k][t]+=p1
        point_power_list[k][t+1]+=p2
        point_power_list[k+1][t+1]+=p3
        point_power_list[k+1][t]+=p4





def judge_neighbourlist(balls):
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



#------*2D-interpolate*------#



def inter(x,y,point_power_list):
    newfunc=interpolate.interp2d(x,y,point_power_list,kind='cubic')
    xnew=np.arange(xmin+r,xmax,r/10)
    ynew=np.arange(ymin+r,ymax,r/10)
    newf=newfunc(xnew,ynew)








