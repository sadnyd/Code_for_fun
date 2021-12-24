import random
import math
import numpy

side_len_cube=1
h=side_len_cube*0.5 #half the side length
position_vertices=[[0 for x in range(3)] for y in range(8)]
position_vertices=[
[h,h,h],[h,-h,h],[h,-h,-h],[h,h,-h],
[-h,h,h],[-h,-h,h],[-h,-h,-h],[-h,h,-h]]


def generate_angles():
    angle_list=numpy.random.uniform(1, math.pi*2, 3)
    #print("angles=",angle_list)
    return angle_list



def vertex_pos_after_rotaion(vertex,angles):
    ax=angles[0]#for rotation about x
    ay=angles[1]#for rotation about y
    az=angles[2]#for rotation about z
    x_matrix=[[1,0,0],[0,math.cos(ax),-math.sin(ax)],[0,math.sin(ax),math.cos(ax)]]
    pos_x_rotation=numpy.matmul(numpy.array(x_matrix),numpy.array(vertex)).tolist()
    y_matrix=[[math.cos(ay),0,math.sin(ay)],[0,1,0],[-math.sin(ay),0,math.cos(ay)]]
    pos_y_rotation=numpy.matmul(numpy.array(y_matrix),numpy.array(pos_x_rotation)).tolist()
    z_matrix=[[math.cos(az),-math.sin(az),0],[math.sin(az),math.cos(az),0],[0,0,1]]
    pos_z_rotation=numpy.matmul(numpy.array(z_matrix),numpy.array(pos_y_rotation)).tolist()
    # print(pos_z_rotation)
    return pos_z_rotation

def vertex_update(angles):
    for i in range(8):
        position_vertices[i]=vertex_pos_after_rotaion(position_vertices[i],angles)

def angle_bw_lines(p1,p2,p3): 
    p2p1=[p1[0]-p2[0],p1[1]-p2[1]]
    # magp2p1=math.sqrt(p2p1[0]**2+p2p1[1]**2)
    p2p3=[p3[0]-p2[0],p3[1]-p2[1]]
    dot = p2p1[0]*p2p3[0] + p2p1[1]*p2p3[0]     
    det = p2p1[1]*p2p3[0]- p2p1[0]*p2p3[1]   
    theta = math.atan2(det, dot)
    # magp3p1=math.sqrt(p2p3[0]**2+p2p3[1]**2)
    # theta=numpy.arccos((float(numpy.dot(numpy.array(p2p1),numpy.array(p2p3)))/(magp2p1*magp3p1)))
    return theta 



def shadow_veticesandangle():
    verticesandangle=[[[position_vertices[i][0],position_vertices[i][1]],0] for i in range(8)] #extra 0 will be replaced by the angle with x axis later on
    center=[0 for x in range(2)]
    for i in range(8):
        # print(type(verticesandangle[i][0][0]),type(verticesandangle[i][0][1]))
        center[0]=center[0]+ verticesandangle[i][0][0]
        center[1]=center[1]+ verticesandangle[i][0][1]
    for i in range(8):
        verticesandangle[i][1]=angle_bw_lines(verticesandangle[i][0],[center[1],center[1]],[center[1],center[1]+1])
    verticesandangle.sort(key=lambda row: (row[1]))
    vertex_no_to_remove=[]
    for i in range(8):
        anglecheck=angle_bw_lines(verticesandangle[i][0],verticesandangle[(i+1)%8][0],verticesandangle[(i+2)%8][0])
        # print(anglecheck)
        if anglecheck>=math.pi:
            vertex_no_to_remove.append(i)
    counter=0
    # print(verticesandangle)
    for vno in vertex_no_to_remove:
        verticesandangle.pop(vno-counter)
        counter+=1
    # print(verticesandangle)
    return verticesandangle


def distace(p1,p2):
    # print(type(p1[0]),type(p1[1]))
    # print(type(p1[0]),type(p1[1]))
    dist=math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    # print(type(dist))
    return dist


def area(verticesandangle):
    lenlist=len(verticesandangle)
    # print(lenlist)
    ar=0
    center=[0,0]
    for i in range(lenlist):
        center[0]=center[0]+verticesandangle[i][0][0]
        center[1]=center[1]+verticesandangle[i][0][1]
    for i in range(lenlist):
        l1=distace(verticesandangle[i][0],center)
        # print(type(verticesandangle[i][0][0]),type(verticesandangle[i][0][0]),type(center[0]),type(center[1]),type(verticesandangle[(i+1)%lenlist][0][0]),type(verticesandangle[(i+1)%lenlist][0][1]))
        l2=distace(center,verticesandangle[(i+1)%lenlist][0])
        l3=distace(verticesandangle[i][0],verticesandangle[(i+1)%lenlist][0])
        # print(type(l1))
        # print(type(l2))
        # print(type(l3))
        s=float((l1+l2+l3)*0.5)
        triarea=math.sqrt(abs(s*(s-l1)*(s-l2)*(s-l3)))
        ar=ar+triarea
    # print(type(ar))
    return ar

def run():
    answer=0
    test=1000
    for i in range(test):
        angles=generate_angles()
        vertex_update(angles)
        arearequired=area(shadow_veticesandangle())
        # print(type(arearequired))
        answer+=arearequired
    print(answer/test)

run()
