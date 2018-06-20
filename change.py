
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
                collided2.append([i, j])
                collided2_detail.append([i, j, delta])
    return collided2

def collided_message2(collided2):
    collisi_list2=[]
    for s in range(len(collided2)):
        collisi_list2.append(collided2[s][0])
    collide_message2 = {}
    # pdb.set_trace()
    for i in collisi_list2:
        collide_i = []
        for j in range(len(collided2)):
            # pdb.set_trace()
            if collided2[j][0] == i:
                collided_i.append([collided_detail[j][1],collided_detail[j][2]])
            collide_message2[i] = collide_i
    return collide_message2,collisi_list2


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
    dv1_para = - Kn / (2 * r - delta + 0.000001) * dt * (x2 - x1) / L
    dv1_erect = -delta*dt*v1_erect/(2*r)
    cos_angle = (x2 - x1) / L
    sin_angle = (y2 - y1) / L
    dvx1 = dv1_para * cos_angle - dv1_erect * sin_angle
    dvy1 = dv1_para * sin_angle + dv1_erect * cos_angle
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
    collide_message,collisi_list1=collided_message(collided, collided_detail)
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

#------*the old style*------#
def between_collision(balls, silence_list=[], counter=None):
    collided1 = between_distance(balls, silence_list)
    collided2 = between_distance2(balls, silence_list)
    m = 3
    if counter > m:
        collision_list = [read_collision_list(counter-(i+1)) for i in range(m)]
        for i in range(len(collision_list)):
            collided1 = conversion_divide(collided1, collision_list[i])
    write_collision_list(collided1, counter)
    for i in range(len(collided1)):
        x1 = balls['position_x'][collided1[i][0]]
        y1 = balls['position_y'][collided1[i][0]]
        x2 = balls['position_x'][collided1[i][1]]
        y2 = balls['position_y'][collided1[i][1]]
        vx1 = balls['velocity_x'][collided1[i][0]]
        vy1 = balls['velocity_y'][collided1[i][0]]
        vx2 = balls['velocity_x'][collided1[i][1]]
        vy2 = balls['velocity_y'][collided1[i][1]]
        r = balls['radius_'][0]
        delta = collided1[i][2]
        dt=0.005
        v_change_list=velocity_change2(x1, y1, x2, y2, vx1, vy1, vx2, vy2, r, delta, dt)
        balls['velocity_x'][collided1[i][0]] = v_change_list[0]
        balls['velocity_y'][collided1[i][0]] = v_change_list[1]
        balls['velocity_x'][collided1[i][1]] = v_change_list[2]
        balls['velocity_y'][collided1[i][1]] = v_change_list[3]
    for j in range(len(collided2)):
        X1 = balls['position_x'][collided2[j][0]]
        Y1 = balls['position_y'][collided2[j][0]]
        X2 = balls['position_x'][collided2[j][1]]
        Y2 = balls['position_y'][collided2[j][1]]
        vX1 = balls['velocity_x'][collided2[j][0]]
        vY1 = balls['velocity_y'][collided2[j][0]]
        vX2 = balls['velocity_x'][collided2[j][1]]
        vY2 = balls['velocity_y'][collided2[j][1]]
        R = balls['radius_'][0]
        delta = collided2[j][2]
        dt = 0.005
        v_change_list = velocity_change2(X1, Y1, X2, Y2, vX1, vY1, vX2, vY2, R, delta, dt)
        balls['velocity_x'][collided2[j][0]] = v_change_list[0]
        balls['velocity_y'][collided2[j][0]] = v_change_list[1]
    return balls