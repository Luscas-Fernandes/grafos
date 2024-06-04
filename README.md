# Grafos

---
# MODO INTERATIVO

# Adicionar os vértices:
Simplesmente digite o nome de cada vértice quando pedido
 
# Adicionar as arestas:
Para adicionar as arestas deve-se digitar com o padrão de:

# Arestas nao direcionais:

# Sem peso
a--b para arestas não direcionadas e sem peso

# Com peso
a--b$2 para arestas não direcionadas de peso 2

---

# Arestas direcionadas

# Sem peso
a->b, deste modo a apontando para b, arestas sem peso
a<>b, deste modo bidirecional, arestas sem peso
a<-b, deste modo b apontando para a, arestas sem peso

# Com peso
a->b$2, deste modo a apontando para b, com peso 2
a<>b$2, deste modo bidirecional, com peso 2
a<-b$2, deste modo b apontando para a, com peso 2

---

# MODO INSERÇÃO DE ARQUIVO

A inserção de arquivo requer os mesmos padrões para funcionamento do que o modo interativo, a unica diferença consiste em que:
deve-se vir primeiro os vértices, uma linha vazia e as arestas em seguida da linha vazia, ex.:

a
b
c
d
<!-- LINHA VAZIA AQUI -->
a--b$2
a--c$6
b--c$4
c--d$9

---

# Funcionamento do código

Não é possível, depois de inserir uma aresta direcional, inserir arestas não direcionais,
o sistema trata, assim que inserida uma aresta direcional, o grafo todo como direcional, portanto
torna-se por motivos de proteção ao código impossível de adicionar arestas não direcionais

---

Não é possível, depois de inserir uma aresta não direcional, inserir arestas direcionais,
o sistema trata, assim que inserida uma aresta não direcional, o grafo todo como não direcional, portanto
torna-se por motivos de proteção ao código impossível de adicionar arestas direcionais

--- 

Não é possível inicializar uma aresta que já existe mais de uma vez, pois trata-se de um contexto
de grafo simples.

---




Grupo: 
Lucas Fernandes
Victor Aroucha