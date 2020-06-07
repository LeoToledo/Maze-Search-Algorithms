
# Python3 program to print DFS traversal
# from a given given graph
from maze import Maze
import time

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
        last = len(self.stacked)
        if self.visited.__contains__([i,j]):
            self.stacked.remove(self.stacked[last-1])
            last = len(self.stacked)
            return self.DiscoverNode(self.stacked[last-1][0], self.stacked[last-1][1], x)
        self.stacked.remove([i,j])
        self.visited.append([i, j])
        atual = x[i,j]
        
        for y in range(0, len(x[i,j])):
            
            if(maze.render == '1'):
                maze.update_maze(number_list, original_number_list, i, j) 
            
            if self.stacked.__contains__(atual[y]):
                b = '1'
            else:
                self.stacked.append(atual[y])
            if atual[y] == [end_position[0], end_position[1]]:
                self.visited.append(atual[y])
                print('caminho', self.visited)
                return 'end'
        last = len(self.stacked)
        return self.DiscoverNode(self.stacked[last-1][0], self.stacked[last-1][1], x)

# Driver code
# Create a graph given
# in the above diagram
g  =  Graph()

maze = Maze(0)
graph, init_position, end_position, number_list = maze.create_graph()
original_number_list = number_list.copy()

atual = graph[init_position[0],init_position[1]]
g.stacked.append([init_position[0],init_position[1]])
g.DiscoverNode(init_position[0], init_position[1], graph)
#28, 22