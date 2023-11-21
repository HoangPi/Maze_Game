import cv2
import numpy as np

def ShowPath(path,truemaze,d):
    if(path is None): return

    maze=np.zeros((d*2-1,d*2-1),dtype='uint8')
    maze[0,0]=1
    maze[d*2-2,d*2-2]=1
    if(path[0].x==d*2-2): maze[d*2-3,d*2-2]=1
    else: maze[d*2-2,d*2-3]=1
    for i in range(len(path)-1):
        maze[path[i].x*2,path[i].y*2]=1
        maze[path[i].x*2 + path[i+1].x - path[i].x, path[i].y*2 + path[i+1].y - path[i].y]=1
        # cv2.imshow('BFS',cv2.resize(maze*255,(600,600),interpolation=0))
        # cv2.waitKey(0)
    maze=cv2.resize(maze*127,(600,600),interpolation=0)
    r=cv2.resize(truemaze*127,(600,600),interpolation=0)
    b=r.copy()
    g=r.copy()+maze
    cv2.imshow('Simmulate',cv2.merge((r,g,b)))
    
    pass