import cv2
import numpy as np

def Greedy_Search(grid, originalmaze,d):
    (x,y)=grid.shape
    x-=1
    y-=1
    path=[grid[0,0]]
    root=grid[0,0]
    trash=[]
    mazecopy=np.zeros((x*2+1,y*2+1),dtype='uint8')
    mazecopy[0,0]=1
    while(True):
        flag = True
        if(root.x==d-1 and root.y==d-1): return 1,2
        if(root.x<d-1):
            for connect in grid[root.x+1,root.y].connections:
                flag1=True
                for t in trash:
                    if(t.x==grid[root.x+1,root.y].x and t.y==grid[root.x+1,root.y].y):
                        flag1=False
                        break
                if(flag1):
                    for t in path:
                        if(t.x==grid[root.x+1,root.y].x and t.y==grid[root.x+1,root.y].y):
                            flag1=False
                            break
                if(flag1 and connect.x==root.x and connect.y==root.y):
                    root=grid[root.x+1,root.y]
                    path.append(root)
                    flag = False
                    break
        if(flag and root.y<d-1):
            for connect in grid[root.x,root.y+1].connections:
                flag1=True
                for t in trash:
                    if(t.x==grid[root.x,root.y+1].x and t.y==grid[root.x,root.y+1].y):
                        flag1=False
                        break
                if(flag1):
                    for t in path:
                        if(t.x==grid[root.x,root.y+1].x and t.y==grid[root.x,root.y+1].y):
                            flag1=False
                            break
                if(flag1 and connect.x==root.x and connect.y==root.y):
                    root=grid[root.x,root.y+1]
                    path.append(root)
                    flag=False
                    break
        if(flag and root.y>0):
            for connect in grid[root.x,root.y-1].connections:
                flag1=True
                for t in trash:
                    if(t.x==grid[root.x,root.y-1].x and t.y==grid[root.x,root.y-1].y):
                        flag1=False
                        break
                if(flag1):
                    for t in path:
                        if(t.x==grid[root.x,root.y-1].x and t.y==grid[root.x,root.y-1].y):
                            flag1=False
                            break
                if(flag1 and connect.x==root.x and connect.y==root.y):
                    root=grid[root.x,root.y-1]
                    path.append(root)
                    flag=False
                    break
        if(flag and root.x>0):
            for connect in grid[root.x-1,root.y].connections:
                flag1=True
                for t in trash:
                    if(t.x==grid[root.x-1,root.y].x and t.y==grid[root.x-1,root.y].y):
                        flag1=False
                        break
                if(flag1):
                    for t in path:
                        if(t.x==grid[root.x-1,root.y].x and t.y==grid[root.x-1,root.y].y):
                            flag1=False
                            break
                if(flag1 and connect.x==root.x and connect.y==root.y):
                    root=grid[root.x-1,root.y]
                    path.append(root)
                    flag = False
                    break
        if(flag==False):
            mazecopy[root.x*2,root.y*2]=1
            mazecopy[path[-2].x*2 + root.x - path[-2].x,path[-2].y*2 + root.y - path[-2].y]=1
            cv2.imshow('Simmulate',originalmaze-cv2.resize(mazecopy*127,(600,600),interpolation=0))
            cv2.waitKey(0)
        if(flag):
            trash.append(path.pop())
            if(len(path)<=0): return 1, 2
            root=path[-1]
            
        pass
