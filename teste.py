import re
edges = ["a->b", "z->x", "x->z"]
vertices = ["a", "b", "z", "x"]

n = len(vertices)
adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
print(adj_matrix)

for i in edges:
    a,b = filter(None, re.split(r"[<>\-]", i))
    adj_matrix[vertices.index(a)][vertices.index(b)] = 1
    

for i in range(len(adj_matrix)):
    for j in range(len(adj_matrix)):
        print(f"[{adj_matrix[i][j]}] ", end='')
    print("\n")