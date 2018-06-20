# -*- coding: utf-8 -*-

import numpy as np
import math
from conversion import get_action_list, conversion_divide
from data_write import write_collision_list, read_collision_list, collided_message, collided_message2


def between_distance(balls, silence_list=[]):
    collided = []
    collided_detail = []
    action_list = get_action_list(balls, silence_list)
    for i in action_list:
        po_i_x = balls['position_x'][i]
        po_i_y = balls['position_y'][i]
        ra_i = balls['radius_'][i]
        for j in range(i):
            po_j_x = balls['position_x'][j]
            po_j_y = balls['position_y'][j]
            ra_j = balls['radius_'][j]
            distance = np.sqrt((po_i_x-po_j_x)**2+(po_i_y-po_j_y)**2)
            if distance <= (ra_i+ra_j):
                delta = ra_i+ra_j-distance
                collided.append([i, j])
                collided_detail.append([i, j, delta])
    return collided, collided_detail

def between_distance2(balls, silence_list=[]):
    collided2 = []
    collided2_detail=[]
    action_list = get_action_list(balls, silence_list)
    for i in action_list:
        po_i_x = balls['position_x'][i]
        po_i_y = balls['position_y'][i]
        ra_i = balls['radius_'][i]
        for j in silence_list:
            po_j_x = balls['position_x'][j]
            po_j_y = balls['position_y'][j]
            ra_j = balls['radius_'][j]
            distance = np.sqrt((po_i_x-po_j_x)**2+(po_i_y-po_j_y)**2)
            if distance <= (ra_i+ra_j):
                delta = ra_i + ra_j - distance
                collided2.append([i, j, delta])
    return collided2



'''
def delta_v(x1, y1, x2, y2, vx1, vy1, vx2, vy2):
    delta_vx = (((vx1-vx2)*(x1-x2)*(x1-x2)+(vy1-vy2)*(x1-x2)*(y1-y2)) /
                ((x1-x2)**2+(y1-y2)**2))
    delta_vy = (((vy1-vy2)*(y1-y2)*(y1-y2)+(vx1-vx2)*(x1-x2)*(y1-y2)) /
                ((x1-x2)**2+(y1-y2)**2))
    return delta_vx, delta_vy



def velocity_change(x1,y1,x2,y2,vx1,vy1,vx2,vy2,delta,dt):
    Kn=1000
    L=np.sqrt((x1-x2)**2+(y2-y1)**2)
    l=np.array(x2-x1,y2-y1)
    l_erect=np.array(y1-y2,x2-x1)
    v1=np.array(vx1,vy1)
    v2=np.array(vx2,vy2)
    v1_para=np.dot(l,v1)/L
    v2_para=np.dot(l,v2)/L
    v1_erect=np.dot(l_erect,v1)/L
    v2_erect=np.dot(l_erect,v2)/L
    v11_para=v1_para-Kn*delta*dt
    v22_para=v2_para+Kn*delta*dt
    v11_erect=v1_erect-delta*dt*v1_erect/np.abs(v1_erect)
    v22_erect = v2_erect - delta * dt * v2_erect / np.abs(v2_erect)
    cosangle=(x2-x1)/L
    sinangle=(y2-y1)/L
    vx1_new=v11_para*cosangle-v1_erect*sinangle
    vy1_new=v11_para*sinangle+v1_erect*cosangle
    vx2_new = v22_para * cosangle - v2_erect * sinangle
    vy2_new = v22_para * sinangle + v2_erect * cosangle
    v_change_list=[vx1_new,vy1_new,vx2_new,vy2_new]
    return v_change_list


def velocity_change2(x1,y1,x2,y2,vx1,vy1,vx2,vy2,r,delta,dt):
    Kn=1
    g=10
    damping=0.5
    l=np.array(x2-x1,y2-y1)
    L=math.sqrt((x1-x2)**2+(y2-y1)**2)
    vx11=damping*vx1-Kn / (2 * r - delta+0.000001)*dt*(x2-x1)/L
    vx22 = damping*vx2 + Kn / (2 * r - delta+0.000001) * dt * (x2 - x1) / L
    if np.abs(y2-y1)<0.05*r:
        vy11=damping*vy1-Kn / (2 * r - delta+0.000001)*dt*(y2-y1)/L+2*g*dt
        vy22 = damping*vy2 + Kn / (2 * r - delta+0.000001) * dt * (y2 - y1) / L+2*g*dt
    else:
        vy11 = damping*vy1 - Kn / (2 * r - delta+0.000001) * dt * (y2 - y1) / L
        vy22 = damping*vy2 + Kn / (2 * r - delta+0.000001) * dt * (y2 - y1) / L
    v_change=[vx11,vy11,vx22,vy22]
    return v_change
'''

#------*coupling between two balls*------#
def force_acc(i,j,balls,collide_message):
    Kn = 1
    dt=0.005
    r=balls['radius_'][0]
    x1 = balls['position_x'][i]
    y1 = balls['position_y'][i]
    x2 = balls['position_x'][j]
    y2 = balls['position_y'][j]
    vx1 = balls['velocity_x'][i]
    vy1 = balls['velocity_y'][i]
    for k in range(len(collide_message[i])):
        if collide_message[i][k][0]==j:
            delta=collide_message[i][k][1]
    L = np.sqrt((x1 - x2) ** 2 + (y2 - y1) ** 2)
    l_erect = np.array(y1 - y2, x2 - x1)
    v1 = np.array(vx1, vy1)
    v1_erect = np.dot(l_erect, v1) / L
    dvx1_para = - Kn / (2 * r - delta + 0.00001 ) * dt * (x2 - x1) / L
    dvy1_para = - Kn / (2 * r - delta + 0.00001) * dt * (y2 - y1) / L
    dv1_erect = -delta*dt*v1_erect/(2*r)
    cos_angle = (x2 - x1) / L
    sin_angle = (y2 - y1) / L
    dvx1 = dvx1_para  - dv1_erect * sin_angle
    dvy1 = dvy1_para + dv1_erect * cos_angle
    v_change = [dvx1, dvy1]
    return v_change

def add_acc(i,balls,collide_message):
    Dx=0
    Dy=0
    for k in range(len(collide_message[i])):
        j=collide_message[i][k][0]
        v_change=force_acc(i,j,balls,collide_message)
        Dx=Dx+v_change[0]
        Dy=Dy+v_change[1]
    return Dx,Dy


def between_collision(balls, silence_list=[], counter=None):
    collided1,collided_detail = between_distance(balls, silence_list)
    collide_message, collisi_list1=collided_message(collided1, collided_detail)
    m = 3
    if counter > m:
        collision_list = [read_collision_list(counter-(i+1)) for i in range(m)]
        for i in range(len(collision_list)):
            collided1 = conversion_divide(collided1, collision_list[i])
    write_collision_list(collided1, counter)
    for z in range(len(collisi_list1)):
        i=collisi_list1[z]
        Dx,Dy=add_acc(i, balls, collide_message)
        balls['velocity_x'][i] = balls['velocity_x'][i]+Dx
        balls['velocity_y'][i] = balls['velocity_y'][i]+Dy
    collided2 = between_distance2(balls,silence_list)
    collide_message2,collisi_list2=collided_message2(collided2)
    for j in range(len(collisi_list2)):
        p=collisi_list2[j]
        Dx2, Dy2=add_acc(p, balls, collide_message2)
        balls['velocity_x'][p] = balls['velocity_x'][p] + Dx2
        balls['velocity_y'][p] = balls['velocity_y'][p] + Dy2
    return balls