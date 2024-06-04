<span></span>
---
# Teoria dos Grafos - AV2
# MANUAL DE USO E DOCUMENTAÇÃO DO SISTEMA
**O modo de inserção do sistema depende da linha de comando que inicializa o sistema. Para usar o modo interativo, apenas rode o programa normalmente via terminal, e para o modo de inserção de arquivo, insira o nome do arquivo de entrada após o comando.**

Exemplos:

- python sistema-grafos.py
- python sistema-grafos.py input.txt

---
## MODO INTERATIVO
### Adicionar os vértices:

Para adicionar os vértices deve-se dar enter contendo:

*nome do vértice*

**Ao dar enter numa linha vazia, encerra o estado de inserção de vértices.**

### Adicionar as arestas:

Deve-se inserir as arestas com o seguinte formato:

**Arestas Direcionais:**

 *nome do vértice* -> ou <- ou <> *nome do vértice*

 ENão é possível, depois de inserir uma aresta direcional, inserir arestas não xemplos:
 
 - V1->V2
 - A<>B
 - c<-d

**O nome da aresta direcional sempre segue o formato "N1->N2", independente de como foi inserida no sistema. a forma de inserção V1<>V2 adiciona duas arestas independentes, "V1->V2" e "V2->V1".**

**Arestas Não-Direcionais:**

Deve-se inserir as arestas com o seguinte formato:

*nome do vértice* -- *nome do vértice*

Exemplos:

- V1--V2
- A--B
- c--d

### Sem peso
apenas o nome da aresta insere-a sem peso (peso 0)

Exemplos:

a--b
V1<>V2
A<-B

### Com peso
deve-se concatenar o peso da aresta em sua inserção da seguinte forma:

*aresta* $ *peso*

Exemplos:

- a--b$10
- V1--V2$3
- A->B$5

**Ao dar enter em uma linha vazia, encerra o estado de inserção de arestas.**

---

# MODO INSERÇÃO DE ARQUIVO

O modo de inserção de arquivo segue o mesmo formato do modo interativo, mas deve ser formatado num arquivo txt segundo o exemplo:

*vertices separados por enter*
*linha vazia*
*arestas separadas por enter*

Exemplo de arquivo txt:

a<br/>
b<br/>
c<br/>
d
<p> 
a--b$2<br/>
b--c$3<br/>
c--d<br/>
d--a$10<br/>
</p>

---

## PREVENÇÃO DE ERROS

- Não é possível, depois de inserir uma aresta direcional, inserir arestas não direcionais,
o sistema trata, assim que inserida uma aresta direcional, o grafo todo como direcional, portanto
torna-se por motivos de proteção ao código impossível de adicionar arestas não direcionais e o oposto
ocorre ao adicionar-se uma aresta não direcional primeiro.

- Não é possível inicializar uma aresta que já existe mais de uma vez, pois trata-se de um contexto
de grafo simples.

---




Grupo: 
- Lucas Fernandes
- Victor Aroucha
