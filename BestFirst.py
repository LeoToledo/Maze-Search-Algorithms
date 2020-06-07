from maze import Maze
import numpy as np


def main():
    
    maze = Maze(1)
    graph, init_position, end_position, number_list = maze.create_graph()
    original_number_list = number_list.copy()

    rows = maze.rows
    cols = maze.cols



    i=0
    j=0
    current_position = init_position[0],init_position[1]
    buffer = []
    for i in range (0, len(graph)):
        
        if(maze.render == '1'):
            maze.update_maze(number_list, original_number_list, current_position[0], current_position[1])
                
        if(graph[current_position] != graph[end_position[0], end_position[1]]):
            inicio = tuple(current_position)
            current_position = adjacentes_dic(graph, inicio)
            print(current_position)
            buffer.append(current_position)
            if(i>=2 and buffer[i]==buffer[i-2]):
                current_position = np.random.randint(0,rows), np.random.randint(0,cols)
                while(number_list[current_position[0],current_position[1]] == 0):
                    current_position = np.random.randint(0,rows), np.random.randint(0,cols)
                
                
            #print(current_position)
        else:
            print("Caminho encontrado")
            break





def adjacentes_dic(graph, alneu):
    menor_custo = 100
    aux = "erro"

    for k in range(len(graph[alneu])):
        if(graph[alneu][k][2]<menor_custo):
            menor_custo = graph[alneu][k][2]
            aux = graph[alneu][k][0],graph[alneu][k][1]

   
    return aux
            




if __name__ == '__main__':
    main()