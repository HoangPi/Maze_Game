from A_Star_Search import AStar_Search
from UCS_Search import ucs_search
from mazeCreator import node, GridCreator,GridToMaze
import cv2
from BFS_Search import BFS_Search
from ContructPath import ShowPath
from DFS_Search import DFS_Search
from Greedy_Search import Greedy_Search

def back(*args):
    pass
def nothing(x):
    pass
def adjustMaze(d):
    grid = GridCreator(d,d)
    maze = GridToMaze(grid=grid,h=d,w=d)
    truemaze=maze*255
    truemaze=255-truemaze
    truemaze=cv2.resize(truemaze,(600,600),interpolation=0)
    return truemaze, grid


defaultvalue=10
grid = GridCreator(defaultvalue,defaultvalue)
maze = GridToMaze(grid=grid,h=defaultvalue,w=defaultvalue)
truemaze=maze*255
truemaze=255-truemaze
truemaze=cv2.resize(truemaze,(600,600),interpolation=0)


cv2.namedWindow('maze')
cv2.createTrackbar('C', 'maze', 10, 100, nothing)
# cv2.createButton("maze",back,None,cv2.QT_PUSH_BUTTON,1)
cv2.setTrackbarPos('C','maze',10)
cv2.imshow('maze',truemaze)
while(True):
    if(defaultvalue!=cv2.getTrackbarPos('C','maze') and cv2.getTrackbarPos('C','maze')!=0):
        defaultvalue=cv2.getTrackbarPos('C','maze')
        truemaze, grid=adjustMaze(d=defaultvalue)
        cv2.imshow('maze',truemaze)

    k = cv2.waitKey(5) & 0xFF
    
    if k==49:
        try:
            path, mazecopy = BFS_Search(grid=grid,originalmaze=truemaze)
            print("BFS:", len(path))
            ShowPath(path,mazecopy,defaultvalue,truemaze)
        except Exception as e:
            print(e)
            pass
    elif k==50:
        try:
            path, mazecopy = DFS_Search(grid,truemaze)
            print("DFS:", len(path))
            ShowPath(path,mazecopy,defaultvalue,truemaze)
        except Exception as e:
            print(e)
            pass
    elif k==51:
        try:
            k, mazecopy = AStar_Search(grid=grid, originalmaze=truemaze)
            print("A*:", len(k))
            ShowPath(k, mazecopy, defaultvalue,truemaze)
            # cv2.putText()
        except Exception as e:
            print(e)
            pass
    elif k==52:
        try:
            k,mazecopy = ucspath = ucs_search(grid=grid, original_maze=truemaze)
            print("UCS:", len(k))
            ShowPath(k,mazecopy,defaultvalue,truemaze)
        except Exception as e:
            print(e)
            pass
    elif k==53:
        try:
            k, mazecopy = Greedy_Search(grid,truemaze,defaultvalue)
            print("Greedy:", len(k))
            # ShowPath(k,mazecopy,defaultvalue)
            ShowPath(k,mazecopy,defaultvalue,truemaze)
        except Exception as e:
            print(e)
            pass
    elif k == 27:
        cv2.destroyAllWindows()
        break