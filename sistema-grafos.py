import sys
import networkx as nx

class Graph:

    directed = None
    vertices = []
    edges = []

    def __init__(self) -> None:
        pass

    def getVertex(self, name):
        for vertex in self.vertices:
            if(vertex.name == name):
                return vertex
            
        return None
    
    def addEdge(self, new_edge):
        for edge in self.edges:
            if edge.name == new_edge.name:
                print(f'Edge {new_edge.name} already exists!')
                return 1

        self.edges.append(new_edge)

    def CreateEmptyAdjMatrix(self):
        n = len(self.vertices)
        adj_matrix = [[0 for _ in range(n)] for _ in range(n)]

        return adj_matrix
    
    def populateAdjMatrix(self, adj_matrix: object) -> object:
        import re
        def printAdjMatrix():
            for i in range(len(adj_matrix)):
                for j in range(len(adj_matrix)):
                    print(f"[{adj_matrix[i][j]}] ", end='')
                print("\n")

        if self.directed:
            for edge in self.edges:
                n1, n2 = filter(None, re.split(r"[<>\-]", edge.name))
                v1 = self.getVertex(n1) # pega vertice pelo nome
                v2 = self.getVertex(n2) 
                adj_matrix[self.vertices.index(v1)][self.vertices.index(v2)] = 1
            
        else:
            for edge in self.edges:
                n1, n2 = filter(None, re.split(r"[<>\-]", edge.name))
                v1 = self.getVertex(n1) # pega vertice pelo nome
                v2 = self.getVertex(n2) 
                adj_matrix[self.vertices.index(v1)][self.vertices.index(v2)] = 1
                adj_matrix[self.vertices.index(v2)][self.vertices.index(v1)] = 1

        printAdjMatrix()

        return adj_matrix
    

    def vertexAdjacents(self, fEdge, sEdge, adjMatrix): # precisa ser testado
        v1 = self.getVertex(fEdge)
        v2 = self.getVertex(sEdge)
        adj = 1 if adjMatrix[v1][v2] else 0 # da p trocar adj = adjMatrix[v1][v2] só kkk
        sAdj = "" if adj else " not"

        print(F"vertex {v1} and {v2} are{sAdj} adjacent")
        
        return adj

    def shortestPath(self, start_name, end_name):
        if not self.getVertex(start_name) or not self.getVertex(end_name):
            print(f"One or both vertices not found in the graph: {start_name}, {end_name}")
            return

        # Create a NetworkX graph inside the method
        if self.directed:
            G = nx.DiGraph()
        else:
            G = nx.Graph()

        # Add vertices
        for vertex in self.vertices:
            G.add_node(vertex.name)

        # Add edges
        for edge in self.edges:
            G.add_edge(edge.pair[0], edge.pair[1], weight=int(edge.weight))

        try:
            length = nx.dijkstra_path_length(G, start_name, end_name)
            path = nx.dijkstra_path(G, start_name, end_name)
            print(f"Shortest path from {start_name} to {end_name}: {' -> '.join(path)} with distance {length}")
        except nx.NetworkXNoPath:
            print(f"No path exists between {start_name} and {end_name}")


class Vertex:

    edges = []

    def __init__(self, name):
        self.name = name

    def addEdge(self, new_edge):
        for edge in self.edges:
            if edge.name == new_edge.name:
                print(f'Edge {new_edge.name} already exists!')
                return 1

        self.edges.append(new_edge)


class Edge:

    def __init__(self, name, pair, weight):
        self.name = name
        self.pair = pair
        self.weight = weight
        
def clearScreen(): 
        from os import system, name

        if name == 'nt':
            return system('cls')
        
        return system('clear')

def getSeparator(string):

    for separator in ['--', '->', '<-', '<>']:
        if string.find(separator) != -1:
            return separator

graph = Graph()

def vertexConnections(name):
    connections = []

    if graph.directed == False:
        for edge in graph.edges:
            if name in edge.pair:
                #adiciona "o outro" na lista de connections
                connections.append(edge.pair[edge.pair.index(name) - 1 ** 2])

        return set(connections)
    
    entry = []
    exit = []

    for edge in graph.edges:
        if edge.pair[0] == name:
            exit.append(edge.pair[1])

        elif edge.pair[1] == name:
            entry.append(edge.pair[0])

    return [set(entry),set(exit)]

#se for usado o txt para inserir tudo de uma vez:
if len(sys.argv) > 1:
    filename = sys.argv[1]

    with open(filename, 'r+') as file:

        line = ' '

        while line:
            line = file.readline()
            line = line.strip()

            if not line:
                break
            
            if graph.getVertex(line):
                print(f'Vertex {line} already exists!')
                continue

            graph.vertices.append(Vertex(line))

        line = ' '

        while line:
            line = file.readline()
            line = line.strip()

            if not line:
                break

            separator = getSeparator(line)

            match separator:

                case '--':
                    if graph.directed == None:
                        graph.directed = False

                    elif graph.directed == True:
                        print("cannot add not-directed edge to directional graph!")
                        continue

                    try:
                        name, weight = line.split('$')

                    except:

                        name = line
                        pair = line.split(separator)
                        weight = 0

                    finally:
                        pair = name.split(separator)
                        new_edge = Edge(name, pair, weight)

                        vertex = graph.getVertex(pair[0])
                        vertex.addEdge(new_edge)
                        graph.addEdge(new_edge)

                case '->':
                    if graph.directed == None:
                        graph.directed = True

                    elif graph.directed == False:
                        print("Cannot add directed edge to non-directional graph!")
                        continue

                    try:
                        name, weight = line.split('$')

                    except:

                        name = line
                        pair = line.split(separator)
                        weight = 0

                    finally:
                        pair = name.split(separator)
                        new_edge = Edge(name, pair, weight)

                        vertex = graph.getVertex(pair[0])
                        vertex.addEdge(new_edge)
                        graph.addEdge(new_edge)
                
                case '<-':
                    if graph.directed == None:
                        graph.directed = True

                    elif graph.directed == False:
                        print("Cannot add directed edge to non-directional graph!")
                        continue

                    try:
                        name, weight = line.split('$')

                    except:

                        name = line
                        weight = 0

                    finally:
                        a, b = name.split(separator)
                        pair = [b,a]
                        name = f'{b}->{a}'
                        new_edge = Edge(name, pair, weight)

                        vertex = graph.getVertex(pair[0])
                        vertex.addEdge(new_edge)
                        graph.addEdge(new_edge)

                case '<>':
                    if graph.directed == None:
                        graph.directed = True

                    elif graph.directed == False:
                        print("Cannot add directed edge to non-directional graph!")
                        continue

                    try:
                        name, weight = line.split('$')

                    except:

                        name = line
                        weight = 0

                    finally:
                        a, b = name.split(separator)
                        pair = [a,b]
                        name = f'{a}->{b}'
                        new_edge = Edge(name, pair, weight)

                        vertex = graph.getVertex(pair[0])
                        vertex.addEdge(new_edge)
                        graph.addEdge(new_edge)

                        name = f'{b}->{a}'
                        pair = [b, a]
                        new_edge = Edge(name, pair, weight)

                        vertex = graph.getVertex(pair[0])
                        vertex.addEdge(new_edge)
                        graph.addEdge(new_edge)

#se for inserção manual:
else:
    name = ' '

    while name:
        name = input("Input new vertex name: ")

        if not name and not len(graph.vertices):
            sys.exit("No vertices added in Graph, forced exit!")

        if not name:
            break

        if graph.getVertex(name):
            print(f'Vertex {name} already exists!')
            continue

        graph.vertices.append(Vertex(name))

    adjacencyMatrix = graph.CreateEmptyAdjMatrix()

    print("\n\nEdge input format:\n\n(source vertex name)(-- or ->)(destiny vertex name)\nto add weight, add ;(weight)\n\n")

    prompt = ' '

    while prompt:
        prompt = input("Input new edge:")

        if not prompt:
            break

        separator = getSeparator(prompt)

        match separator:

            case '--':
                if graph.directed == None:
                    graph.directed = False

                elif graph.directed == True:
                    print("Cannot add directed edge to non-directional graph!")
                    continue

                try:
                    name, weight = prompt.split('$')

                except:

                    name = prompt
                    pair = prompt.split(separator)
                    weight = 0
            
                finally:
                    pair = name.split(separator)
                    new_edge = Edge(name, pair, weight)

                    vertex = graph.getVertex(pair[0])
                    vertex.addEdge(new_edge)
                    graph.addEdge(new_edge)

            case '->':
                if graph.directed == None:
                    graph.directed = True

                elif graph.directed == False:
                    print("Cannot add directional edge to non-directional graph!")
                    continue

                try:
                    name, weight = prompt.split('$')

                except:

                    name = prompt
                    pair = prompt.split(separator)
                    weight = 0
            
                finally:
                    pair = name.split(separator)
                    new_edge = Edge(name, pair, weight)

                    vertex = graph.getVertex(pair[0])
                    vertex.addEdge(new_edge)
                    graph.addEdge(new_edge)

            case '<-':
                if graph.directed == None:
                    graph.directed = True

                elif graph.directed == False:
                    print("Cannot add directional edge to non-directional graph!")
                    continue

                try:
                    name, weight = prompt.split('$')

                except:
                    name = prompt
                    weight = 0
            
                finally:
                    a, b = name.split(separator)
                    pair = [b,a]
                    name = f'{b}->{a}'
                    new_edge = Edge(name, pair, weight)

                    vertex = graph.getVertex(pair[0])
                    vertex.addEdge(new_edge)
                    graph.addEdge(new_edge)

            case '<>':
                if graph.directed == None:
                    graph.directed = True

                elif graph.directed == False:
                    print("Cannot add directional edge to non-directional graph!")
                    continue

                try:
                    name, weight = prompt.split('$')

                except:
                    name = prompt
                    weight = 0
            
                finally:
                    a, b = name.split(separator)
                    pair = [a,b]
                    name = f'{a}->{b}'
                    new_edge = Edge(name, pair, weight)

                    vertex = graph.getVertex(pair[0])
                    vertex.addEdge(new_edge)
                    graph.addEdge(new_edge)

                    name = f'{b}->{a}'
                    pair = [b, a]
                    new_edge = Edge(name, pair, weight)

                    vertex = graph.getVertex(pair[0])
                    vertex.addEdge(new_edge)
                    graph.addEdge(new_edge)
    

# clearScreen() # Só pra limpar o de antes
#print do resultado final

while True:
    
    try:
        command = int(input('\n=======================================\n1 - Check graph properties\n2 - Print vertices and edges\n3 - Check single vertex connections\n4 - Dijskstra\n5 - Adjacent Matrix\n6 - Check if vertices are adjacent\n7 - Exit\n: '))
    except ValueError("Invalid input, not an int\nDigita um melhor") as e:
        print(e)
        

    match command:
        case 1:
            print('\n')
            print(f'order: {len(graph.vertices)}')
            print(f'size: {len(graph.vertices) + len(graph.edges)}')
            print(f'directed: {graph.directed}')
            input("\npress enter to continue")
            clearScreen()
        case 2:
            print('\n')
            for i, vertex in enumerate(graph.vertices):
                print(f"vertice {i}: {vertex.name}")

            for edge in graph.edges:
                print(edge.name)
            input("\npress enter to continue")
            clearScreen()
        case 3:
            vertex = input("\nInput vertex to check connections: ")

            print('\n')

            if graph.directed:
                entry, exit = vertexConnections(vertex)

                print('entry:', entry)
                print('exit:', exit)
                print(f'\nDegree: {len(entry) + len(exit)}')
            
            else:
                connections = vertexConnections(vertex)
                print(connections)
                print(f'\nDegree: {len(connections)}')
            input("\npress enter to continue")
            clearScreen()
        case 4:
            v1 = input("Type the origin vertex to check the shortest path between them: ")
            v2 = input("Type the destiny vertex to check the shortest path between them: ")
            shortestPath = graph.shortestPath(v1, v2)
            input("\npress enter to continue")
            clearScreen()
        case 5:
            adjacencyMatrix = graph.CreateEmptyAdjMatrix()
            adjacencyMatrix = graph.populateAdjMatrix(adjacencyMatrix)
            input("\npress enter to continue")
            clearScreen()
        case 6:
            v1 = input("Type the origin vertex to check they are adjacent: ")
            v2 = input("Type the destiny vertex to check they are adjacent: ")

            print('\n')

            if graph.directed:
                entry, exit = vertexConnections(v1)

                if v2 in entry or v2 in exit:
                    print(f"vertex {v1} and {v2} are adjacent")
                else:
                    print(f"vertex {v1} and {v2} are not adjacent")
            
            else:
                connections = vertexConnections(v1)

                if v2 in connections:
                    print(f"vertex {v1} and {v2} are adjacent")
                else:
                    print(f"vertex {v1} and {v2} are not adjacent")
    
            input("\npress enter to continue")
            clearScreen()
        case 7:
            print("\nShutting down...\n")
            exit()
        