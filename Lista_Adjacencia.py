#Código para demonstrar o funcionamento de uma lista de adjacencias
def inicializar_lista():
    for i in range(vertices):
        grafo.append([])

def mostrar_grafo():
    for i in range(vertices):
        print(i+1, ' : ', grafo[i])

def mostrar_grafo_detalhado():
    for i in range(vertices):
        print('')
        print(i+1, ' : ', end=' ')
        for j in grafo[i]:
            print(j, end= ' ')

def adicionar_aresta(vertice_a, vertice_b):
    grafo[vertice_a-1].append(vertice_b)
    if vertice_a != vertice_b:
        grafo[vertice_b-1].append(vertice_a)

grafo = []
vertices = int (input('Qual a quantidade de vértices no grafo? '))
inicializar_lista()
adicionar_aresta(1, 2)
adicionar_aresta(1, 3)
# adicionar_aresta(2, 1)
# adicionar_aresta(3, 1)
mostrar_grafo()
mostrar_grafo_detalhado()