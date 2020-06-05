# Python3 program to print DFS traversal
# from a given given graph
from maze import Maze
import time
import numpy as np

from collections import defaultdict
# This class represents a directed graph using
# adjacency list representation
class Edge:
    def __init__(self, v, lat, lng):
        self.v = v
        self.lat = lat
        self.lng = lng



class Graph:
    path = []
    visited = []
    stacked = []
    # Constructor
    def __init__(self):

     # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def DiscoverNode(self, i, j, x):
        if self.visited.__contains__([i,j]):
            self.stacked.remove(self.stacked[0])
            return self.DiscoverNode(self.stacked[0][0], self.stacked[0][1], x)
        self.stacked.remove([i,j])
        self.visited.append([i, j])
        atual = x[i,j]
        
        old_i = 2
        old_j = 2
        for y in range(0, len(x[i,j])):
            
            
            if(i == 0 and j == 0):
                old_i = i
                old_j = j
                number_list[i][j] = 2
            
            else:
                number_list[old_i][old_j] = original_number_list[old_i][old_j]
                old_i = i
                old_j = j
                number_list[i][j] = 2
                
             
            maze.draw_maze(number_list)
            time.sleep(0.1)
            
        
            if self.stacked.__contains__(atual[y]):
                b = '1'
            else:
                self.stacked.append(atual[y])
            if atual[y] == [28, 22]:
                self.visited.append(atual[y])
                print('caminho', self.visited)
                        
                
                return 'end'
        return self.DiscoverNode(self.stacked[0][0], self.stacked[0][1], x)
        print(self.stacked)
        print(self.visited)
        
                

# Driver code
# Create a graph given
# in the above diagram
g  =  Graph()
maze = Maze()
graph, init_position, end_position, number_list = maze.create_graph()
original_number_list = number_list.copy()
atual = graph[0,2]
g.stacked.append([0,2])
g.DiscoverNode(0, 2, graph)

#28, 22