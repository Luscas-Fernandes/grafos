import sys

class Graph:

    directed = None
    vertices = []
    edges = []

    def __init__(self) -> None:
        pass

    def getVertex(self, name):
        for vertice in self.vertices:
            if(vertice.name == name):
                return vertice
            
        return None
    
    def addEdge(self, new_edge):
        for edge in self.edges:
            if edge.name == new_edge.name:
                print(f'Edge {new_edge.name} already exists!')
                return 1

        self.edges.append(new_edge)


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
        

def getSeparator(string):

    for separator in ['--', '->', '<-', '<>']:
        if string.find(separator) != -1:
            return separator

graph = Graph()

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

        if not name:
            break

        if graph.getVertex(name):
            print(f'Vertex {name} already exists!')
            continue

        graph.vertices.append(Vertex(name))

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

#print do resultado final
print(f'directed: {graph.directed}')

for vertex in graph.vertices:
    print(vertex.name)

for edge in graph.edges:
    print(edge.name)