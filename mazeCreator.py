# Init the Gird components and functions
import numpy as np
from tkinter import W
import heapq


class node():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.connections = []
    def connect(self,newnode):
        if(len(self.connections)>0):
            for i in self.connections:
                if(i.x == newnode.x and i.y == newnode.y):return
        
        if((self.x == newnode.x + 1 or self.x == newnode.x - 1) and self.y == newnode.y):
            self.connections.append(newnode)
            newnode.connections.append(self)
            return
        if((self.y == newnode.y + 1 or self.y == newnode.y - 1) and self.x == newnode.x):
            self.connections.append(newnode)
            newnode.connections.append(self)
            return
def randomConnection(grid):
    (w,h) = grid.shape
    x = np.random.randint(0,w)
    y = np.random.randint(0,h)
    neighbor = np.random.randint(0,4)
    if(neighbor==0 and x>0):
        grid[x,y].connect(grid[x-1,y])
        return
    elif(neighbor==1 and x<w-1):
        grid[x,y].connect(grid[x+1,y])
        return
    elif(neighbor==2 and y>0):
        grid[x,y].connect(grid[x,y-1])
        return
    elif(y<h-1):
        grid[x,y].connect(grid[x,y+1])
        return
def fillAll(grid):
    (w,h) = grid.shape
    flag = False
    while(flag==False):
        flag=True
        for i in range(w):
            for j in range(h):
                if(len(grid[i,j].connections)<=0):
                    flag=False
                    neighbor = np.random.randint(0,4)
                    if(neighbor==0 and i>0):
                        grid[i,j].connect(grid[i-1,j])
                    elif(neighbor==1 and i<w-1):
                        grid[i,j].connect(grid[i+1,j])
                    elif(neighbor==2 and j>0):
                        grid[i,j].connect(grid[i,j-1])
                    elif(j<h-1):
                        grid[i,j].connect(grid[i,j+1])

def GridCreator(w,h):
    # Init the grid
    (w,h) = (w,h)
    grid = np.full((h,w),fill_value=node(0,0))
    for i in range(h):
        for j in range(w):
            grid[i,j]=node(i,j)

    # fillAll(grid=grid)
    for i in range(int(w*h*1.6)): randomConnection(grid=grid)
    for i in range(int(w*h/20)): randomConnection(grid=grid[0:int(h/3),0:int(w/3)])
    for i in range(int(w*h/20)): randomConnection(grid=grid[int(2.0*h/3):h,int(2.0*w/3):w])
    fillAll(grid=grid)
    return grid
def GridToMaze(grid,h,w):
    # matrix = np.zeros((h,w),dtype='uint8')
    # for i in range(h):
    #     for j in range(w):
    #         matrix[i,j]=len(grid[i,j].connections)
    maze = np.zeros((h*2-1,w*2-1),dtype='uint8')
    # maze=maze+1
    for i in range(h*2-1):
        for j in range(w*2-1):
            if(i&1==1 or j&1==1):maze[i,j]=1
    for i in range(h):
        for j in range(w):
            for k in range(len(grid[i,j].connections)):
                if(grid[i,j].x==grid[i,j].connections[k].x):
                    if(grid[i,j].y==grid[i,j].connections[k].y+1): maze[i*2,j*2-1]=0
                    else: maze[i*2,j*2+1]=0
                else: 
                    if(grid[i,j].x==grid[i,j].connections[k].x+1): maze[i*2-1,j*2]=0
                    else: maze[i*2+1,j*2]=0
    return maze
    # print(maze)