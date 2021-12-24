import os
ext=0
while ext!=1:
    zoom=6
    print("The canvas size must be smaller than equal to 10 for clean output")
    canvas_size=zoom*(int(input("Canvas/Page Size, it's a square--  "))+1)
    print("Please input your x y coordinates of points either clockwise or anti clock wise")
    print("The TOP LEFT of your output represents x=0 y=0 coordinate and the BOTTOM RIGHT x=pagesize y=pagesize ")
    no_of_points=int(input("Number of points in the figure--  "))
    x_point=[]
    y_point=[]
    max_x_point=0
    max_y_point=0
    min_x_point=canvas_size
    min_y_point=canvas_size
    for k in range(0,no_of_points):
        print("Point",k+1," coordinates:")
        x_point.append(zoom*int(input("x coordinate  ")))
        y_point.append(zoom*int(input("y coordinate  ")))#negative
        max_x_point=max(max_x_point,x_point[k])
        max_y_point=max(max_y_point,y_point[k])
        min_x_point=min(min_x_point,x_point[k])
        min_y_point=min(min_y_point,y_point[k])
    #     print(str(x[k])+' '+str(y[k]))
    # print(mxX,"=max x ",mxY,"=max y ",mnX,"=min x ",mnY,"=mod min y")

    canvas=[["  "]*canvas_size for t in range(canvas_size)]
    for Y in range(min_y_point,max_y_point+1):
        # print("  Y =",Y)
        for X in range(min_x_point,max_x_point+1):
            # print("  X =",X)
            for k in range(0,no_of_points):
                # print("  K =",k)
                x2=x_point[(k+1)%(no_of_points)]
                x1=x_point[k]
                max_x1_x2=max(x1,x2)
                min_x1_x2=min(x1,x2)
                y2=y_point[(k+1)%(no_of_points)]
                y1=y_point[k]
                max_y1_y2=max(y1,y2)
                min_y1_y2=min(y1,y2)
                check1=(x2-x1)*(Y-y1)==(y2-y1)*(X-x1) #| abs((x1-x2)*(-i-y1)-(y2-y1)*(j-x1))<1
                check2=min_y1_y2<=Y & Y<=max_y1_y2
                check3=min_x1_x2<=X & X<=max_x1_x2
                if check1 & check2 & check3:
                    canvas[Y][X]="# "
                

    for Y in canvas:
            for X in Y:
                print(X,end='')
            print()
    ext=int(input("Input 1 for exit---"))
os.system('cls')
