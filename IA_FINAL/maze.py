import numpy as np
import matplotlib.pyplot as plt
import time

class Maze:
    def __init__(self):
        pass
    
    def read_txt(self):
        #Lendo o arquivo txt de parâmetros
        self.linelist = [line.rstrip('\n') for line in open("maze.txt")]

        #Lendo o tamanho de linhas e colunas
        size = self.linelist[0].split(" ")
        self.rows = int(size[0])
        self.cols = int(size[1])
        del self.linelist[0]
        
        return self.rows, self.cols, self.linelist
    def create_graph(self):
        
        self.rows, self.cols, self.linelist = self.read_txt()
        #Guardando a posição de cada elemento do labirinto em um dicionario, que será nosso grafo
        #Cada elemento do grafo tem a forma current_node: adjacent_node_1, adjacent_node_2, ...

        #O grafo será implementado na forma de um dicionário, no formato descrito acima
        graph = {}

        #Agora, vamos ramificar nosso grafo a partir do nó inicial
        #A estratégia será checar todos os elementos ao redor do current_node
        adjacent = []
        for i in range(0, self.rows):
            for j in range(0, self.cols):

                #Antes de iniciar a adição no gráfico, vamos guardar a posição
                #inicial e final do labirinto em duas variáveis
                if(self.linelist[i][j] == "#"):
                    init_node_pos = (i,j)
                if(self.linelist[i][j] == "$"):
                    final_node_pos = (i,j)

                #Guarda o nó atual sendo adicionado
                self.current_node_pos = [i,j]
                
                #Se a posição atual for um traço, pula para o próximo
                if(self.linelist[self.current_node_pos[0]][self.current_node_pos[1]] == "-"):
                    continue
                    
                #Pesquisando os nós ao redor do atual
                #Os if's a seguir checam os 4 elementos ao redor do nó atual
                if((self.current_node_pos[0]-1) >= 0 and (self.current_node_pos[0]-1) < self.rows):
                    #Caso o elemento atual seja diferente de um traço(posição inválida)
                    #adiciona ele na lista de adjacentes do nó atual
                    if(self.linelist[self.current_node_pos[0]-1][self.current_node_pos[1]] != "-"):
                        adjacent_element = [ self.current_node_pos[0]-1 , self.current_node_pos[1]]
                        adjacent.append(adjacent_element)
                
                if((self.current_node_pos[0]+1) >= 0 and (self.current_node_pos[0]+1) < self.rows):
                    if(self.linelist[self.current_node_pos[0]+1][self.current_node_pos[1]] != "-"):
                        adjacent_element = [self.current_node_pos[0]+1 , self.current_node_pos[1]]
                        adjacent.append(adjacent_element)
                
                if((self.current_node_pos[1]-1) >= 0 and (self.current_node_pos[1]-1) < self.cols):
                    if(self.linelist[self.current_node_pos[0]][self.current_node_pos[1]-1] != "-"):
                        adjacent_element = [self.current_node_pos[0], self.current_node_pos[1]-1]
                        adjacent.append(adjacent_element)
            
                if((self.current_node_pos[1]+1) >= 0 and (self.current_node_pos[1]+1) < self.cols): 
                    if(self.linelist[self.current_node_pos[0]][self.current_node_pos[1]+1] != "-"):
                        adjacent_element = [self.current_node_pos[0], self.current_node_pos[1]+1]
                        adjacent.append(adjacent_element)

                #Convertendo self.current_node_pos para uma tupla para podermos adicioná-lo no dicionário
                self.current_node_pos = tuple(self.current_node_pos)
                #Adicionando o nó atual no dicionário
                graph[self.current_node_pos] = adjacent
                #Zera a lista de adjacentes para nova adição
                adjacent = []
#        print(graph)
                
        #Aqui, vamos criar uma cópia numérica de linelist
        self.number_list = np.zeros([self.rows, self.cols], dtype=int)
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                if(self.linelist[i][j] == "-"):
                    self.number_list[i][j] = 0
                elif(self.linelist[i][j] == "*"):
                    self.number_list[i][j] = 1
                elif(self.linelist[i][j] == "#"):
                    self.number_list[i][j] = 2
                elif(self.linelist[i][j] == "$"):
                    self.number_list[i][j] = 3
                    
        return graph, init_node_pos, final_node_pos, self.number_list
    
    def draw_maze(self, print_list):
        maze_pixels = np.zeros((self.rows, self.cols,3), np.uint8)

        for i in range(0, self.rows):
            for j in range(0, self.cols):
                #Guarda o nó atual sendo adicionado
                self.current_node_pos = [i,j]
                
                    
                if(print_list[self.current_node_pos[0]][self.current_node_pos[1]] == 1):
                    maze_pixels[i][j] = [100, 50, 0]
                elif(print_list[self.current_node_pos[0]][self.current_node_pos[1]] == 0):
                    maze_pixels[i][j] = [0, 20, 80]
                elif(print_list[self.current_node_pos[0]][self.current_node_pos[1]] == 2):
                     maze_pixels[i][j] = [255, 50, 50]
                elif(print_list[self.current_node_pos[0]][self.current_node_pos[1]] == 3):
                    maze_pixels[i][j] = [50, 255, 50]
                    
                
        fig, maze = plt.subplots(figsize = (5,5))
        
        maze.imshow(maze_pixels)
        #plt.show()
        plt.savefig("Maze")
        maze.axis('off')
        

        

