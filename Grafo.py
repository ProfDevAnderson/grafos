# Iniciando os trabalhos com Grafo
# Matriz = [
#     [10,25,30],
#     [3,99,98]
# ]
# G = [
#     [0, 1],
#     [1, 0]
# ]

def inicializar_matriz():
    for i in range(vertice):
        novaLinha = []
        for j in range(vertice):
            novaLinha.append(0)
        grafo.append(novaLinha)

def mostrar_matriz():
    for i in range(vertice):
        for j in range(vertice):
            print(grafo[i][j], end=" ")
        print("")


def adicionar_aresta(l, c):
    grafo[l-1][c-1] += 1
    grafo[c-1][l-1] += 1

grafo = []
vertice = int(input('Qual a quantidade de vértice do grafo? '))
inicializar_matriz()

mostrar_matriz()

adicionar_aresta(1, 2)
adicionar_aresta(1, 2)

print('Matriz Atualizada --------')
mostrar_matriz()










