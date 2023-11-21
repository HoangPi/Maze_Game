import heapq
import cv2
import numpy as np
#Uniform Cost Search
class UCSNode:
    def __init__(self, state, cost, parent=None):
        self.state = state
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

def ucs_search(grid, original_maze):
    (x, y) = grid.shape
    x -= 1
    y -= 1
    maze_copy = np.zeros((x * 2 + 1, y * 2 + 1), dtype='uint8')
    maze_copy[0, 0] = 1

    start_node = UCSNode(state=grid[0, 0], cost=0)
    priority_queue = [start_node]
    visited = set()

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        if current_node.state.x == x and current_node.state.y == y:
            return reconstruct_path(current_node),maze_copy

        if current_node.state in visited:
            continue

        visited.add(current_node.state)

        for connect in current_node.state.connections:
            new_cost = current_node.cost + 1
            new_node = UCSNode(state=connect, cost=new_cost, parent=current_node)
            heapq.heappush(priority_queue, new_node)

            maze_copy[current_node.state.x * 2 + connect.x - current_node.state.x,
                      current_node.state.y * 2 + connect.y - current_node.state.y] = 1

            maze_copy[connect.x * 2, connect.y * 2] = 1

            cv2.imshow('Simmulate', original_maze - cv2.resize(maze_copy * 127, (600, 600), interpolation=0))
            cv2.waitKey(1)

    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]