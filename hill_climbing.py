
# Python3 program to print DFS traversal
# from a given given graph
from maze import Maze

from collections import defaultdict
# This class represents a directed graph using
# adjacency list representation
class Edge:
    def __init__(self, v, lat, lng):
        self.v = v



class Graph:
    path = []
    visited = []
    stacked = []
    last = []
    # Constructor
    def __init__(self):

        self.graph = defaultdict(list)


    def distanceNode(self,node, x,a,b):
        aux = 9999999999999
        start = [a,b]
        aux1 = [a,b]
        for y in range(len(node)):
            if(maze.render == '1'):
                maze.update_maze(number_list, original_number_list, a, b) 
           # print (node[y],'once',  self.path)
            if self.visited.__contains__(node[y]) or self.path.__contains__(node[y]):
                y
            else:
               # print(self.visited, self.path)
               # print('not visited',node[y])
                i =  node[y][0]
                j =  node[y][1]
                distance =  ((end_position[0]-i)**2)+((end_position[1]-j)**2)
               # print('b',distance, aux)
                if distance <= aux:
                    aux =  distance
                    aux1 = node[y]

        if aux1 == start:
           # print('aaaa',aux1, start)
            self.visited.append([a,b])
            self.path.remove([a,b])
            aux1 = self.path[len(self.path)-1]
        self.path.append(aux1);
      #  print('aaa',aux1, start)
        return aux1

    def DiscoverNode(self, i, j, x):
        
        next_node = self.distanceNode(x[i,j], x,i,j)
        if next_node == [end_position[0],end_position[1]]:
         #   print (self.path)
            return self.path
       # print('no atual', next_node)
        self.last.append([i,j])
        return self.DiscoverNode(next_node[0], next_node[1], x)

# Driver code
# Create a graph given
# in the above diagram
g  =  Graph()

maze = Maze(0)
graph, init_position, end_position, number_list = maze.create_graph()
original_number_list = number_list.copy()

atual = graph[init_position[0],init_position[1]]
g.stacked.append([init_position[0],init_position[1]])
p = g.DiscoverNode(init_position[0], init_position[1], graph)
print('caminho',p)
#28, 22