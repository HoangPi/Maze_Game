import cv2
import heapq
import numpy as np
#A Star
class Node:
    def __init__(self, x, y, h_cost):
        self.x = x
        self.y = y
        self.h_cost = h_cost
        self.g_cost = float('inf')
        self.f_cost = float('inf')
        self.parent = None

    def __lt__(self, other):
        return self.f_cost < other.f_cost

def calculate_heuristic(node, goal):
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def reconstruct_path(node):
    path = []
    current = node
    while current is not None:
        path.append(current)
        current = current.parent
    return path[::-1]

def AStar_Search(grid, originalmaze):
    (x, y) = grid.shape
    x -= 1
    y -= 1
    mazecopy = np.zeros((x * 2 + 1, y * 2 + 1), dtype='uint8')
    mazecopy[0, 0] = 1

    start = Node(0, 0, 0)
    goal = Node(x, y, 0)

    open_set = []
    closed_set = set()

    start.g_cost = 0
    start.f_cost = start.g_cost + calculate_heuristic(start, goal)

    heapq.heappush(open_set, start)

    while open_set:
        current = heapq.heappop(open_set)
        closed_set.add((current.x, current.y))

        if current.x == goal.x and current.y == goal.y:
            mazecopy[current.x * 2, current.y * 2] = 1
            cv2.imshow('Simmulate', originalmaze - cv2.resize(mazecopy * 127, (600, 600), interpolation=0))
            path = reconstruct_path(current)
            return path, mazecopy

        mazecopy[current.x * 2, current.y * 2] = 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x = current.x + dx
            new_y = current.y + dy

            if new_x < 0 or new_x > x or new_y < 0 or new_y > y:
                continue

            if grid[new_x, new_y] == 0 or (new_x, new_y) in closed_set:
                continue

            neighbor = Node(new_x, new_y, calculate_heuristic(Node(new_x, new_y, 0), goal))
            tentative_g_cost = current.g_cost + 1

            if tentative_g_cost < neighbor.g_cost:
                neighbor.parent = current
                neighbor.g_cost = tentative_g_cost
                neighbor.f_cost = neighbor.g_cost + neighbor.h_cost

                if (new_x, new_y) not in closed_set:
                    heapq.heappush(open_set, neighbor)

        cv2.imshow('Simmulate', originalmaze - cv2.resize(mazecopy * 127, (600, 600), interpolation=0))
        cv2.waitKey(1)
    return []
# Usage:
# decoy = grid
# cv2.imshow('maze', truemaze)
# k = AStar_Search(grid=decoy, originalmaze=truemaze)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(len(k))