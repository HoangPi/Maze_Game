import cv2
import numpy as np
# BFS Search
def stack_BFS(path, root):
    root1=root
    nodestack = []
    while(len(path)>0):
        for node in path.pop():
            for connect in node.connections:
                flag = False
                if(connect.x==root1.x and connect.y==root1.y): 
                    nodestack.append(node)
                    root1=node
                    flag=True
                    break
                if(flag):break
    return nodestack
def BFS_Search(grid,originalmaze):
    (x,y)=grid.shape
    x-=1
    y-=1
    mazecopy=np.zeros((x*2+1,y*2+1),dtype='uint8')
    mazecopy[0,0]=1
    # t=0
    path=[]
    temp=[]
    temp.append(grid[0,0])
    path.append(temp)
    while(True):
        batch=[]
        for node in path[-1]:
            mazecopy[node.x*2,node.y*2]=1
            for connect in node.connections:
                flag = False
                # Check if node is in path
                for n in path:
                    flag1 = False
                    for m in n:
                        if(connect.x==m.x and connect.y==m.y):
                            flag1=True
                            flag=True
                            break
                    if(flag1): break
                mazecopy[node.x*2 + connect.x-node.x,node.y*2 + connect.y-node.y]=1
                if(flag==False): 
                    for n in batch:
                        if(connect.x==n.x and connect.y==n.y):
                            flag=True
                            break

                if(flag): continue
                if(connect.x==x and connect.y==y): 
                    # cv2.waitKey(0)
                    # cv2.destroyAllWindows()
                    # print(t)
                    mazecopy[node.x*2 + connect.x-node.x,node.y*2 + connect.y-node.y]=1
                    mazecopy[connect.x*2,connect.y*2]=1
                    cv2.imshow('Simmulate',originalmaze-cv2.resize(mazecopy*127,(600,600),interpolation=0))
                    return stack_BFS(path,connect),mazecopy
                
                mazecopy[connect.x*2,connect.y*2]=1
                batch.append(connect)
                # t+=1
                # print(t)
                # cv2.imshow('maze',originalmaze-cv2.resize(mazecopy*127,(600,600),interpolation=0))
        if(len(batch)<=0): 
            # print(t)
            # cv2.destroyAllWindows()
            return
        cv2.imshow('Simmulate',originalmaze-cv2.resize(mazecopy*127,(600,600),interpolation=0))
        path.append(batch)
        cv2.waitKey(10)
        