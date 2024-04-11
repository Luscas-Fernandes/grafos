from os import system, name

class Grafo:
    def clearScreen(): # Depois mudar a função para separar a chamada de inserção de vértice e aresta. Podem ser colocados separadamente!
        if name == 'nt':
            return system('cls')
        
        return system('clear')


    def retrieveGraph(self): #Backtracking se aplicaria acho. Hash1(vert, aresta) HashConexoes(vertice, vertices) ?
        graph = {}
        vertice = "qualquer_coisa"

        # Pega vértices
        while vertice:
            print("\nEnter vazio para parar de adicionar vértices")
            vertice = input("Nome do vértice: ")

            if not vertice and not graph:
                Grafo.clearScreen()
                return exit("\nlista de vértices está vazia.\nPrograma finalizado forçadamente")

            if not vertice:
                continue
            
            graph[vertice] = []

        # pega arestas
        edge_name = "oi"

        while edge_name:
            edge_name = "oi"
            edge_value = 0
            src_vertice = ""
            dst_vertice = ""


            print("\nNome de aresta vazio para parar de adicionar arestas")

            edge_name = input("Nome da aresta: ")

            if not edge_name: 
                continue

            edge_value = int(input("Valor da aresta: "))

            print("\nVértices presentes no grafo: ")
            for keys in graph.items():
                print(keys)
            print("\n")


            while not src_vertice:
                src_vertice = input("Vértices que está saindo esta aresta: ")
                if src_vertice not in graph:
                    print("vértice que recebe a aresta não existe")
                    src_vertice = ""

            while not dst_vertice:
                dst_vertice = input("Vértices que está chegando esta aresta: ")
                if dst_vertice not in graph:
                    print("vértice que chega a aresta não existe")
                    dst_vertice = ""
            
            graph[src_vertice].append([edge_name, edge_value, dst_vertice]) # Add nome da aresta, destino e valor da aresta         

        return graph

grafo_instance = Grafo()
print(grafo_instance.retrieveGraph())
