import cv2
import numpy as np

# DFS Search
def DFS_Search(grid, originalmaze):
    (x,y)=grid.shape
    x-=1
    y-=1
    path=[[grid[0,0],0]]
    root=grid[0,0]
    trash=[]
    mazecopy=np.zeros((x*2+1,y*2+1),dtype='uint8')
    mazecopy[0,0]=1
    while(True):
        if(root.x==x and root.y==y): 
            temp=[]
            for t in reversed(path): temp.append(t[0])
            return temp, mazecopy

        
        turn=0
        while(turn<len(root.connections)):
            flag=True
            for i in reversed(path):
                if(root.connections[turn].x==i[0].x and root.connections[turn].y == i[0].y):
                    turn+=1
                    flag=False
                    break
            if(flag):
                for j in trash:
                    if(root.connections[turn].x==j.x and root.connections[turn].y == j.y):
                        turn+=1
                        flag=False
                        break
            if(flag): break
        if(turn>=len(root.connections)):
            trash.append(path.pop()[0])
            try:
                root=path[-1][0]
            except: return
            continue


        root=path[-1][0].connections[turn]
        mazecopy[root.x*2,root.y*2]=1
        mazecopy[path[-1][0].x*2 + root.x - path[-1][0].x, path[-1][0].y*2+root.y-path[-1][0].y]=1
        cv2.waitKey(1)
        cv2.imshow('Simmulate',originalmaze-cv2.resize(mazecopy*127,(600,600),interpolation=0))
        path.append([root,0])