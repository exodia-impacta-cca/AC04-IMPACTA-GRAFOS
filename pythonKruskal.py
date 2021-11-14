from ac04_ex_03 import *

csv = 'cidadedistancia.csv'
grafo = criaGrafoDict(leCsvCriaListaDistancias(csv))


def quicksort(vetor,inicio,fim):
    if(inicio < fim):
        q = pQSort(vetor,inicio,fim) 
        quicksort(vetor, q[1],q[0]-1) 
        quicksort(vetor, q[0]+1,q[2])

def pQSort(vetor,inicio,fim):
    pivo = vetor[fim]
    i = inicio-1

    for j in range(inicio,fim):
        if(peso(grafo, vetor[j]) <= peso(grafo, pivo)):
            i += 1
            vetor[i],vetor[j] = vetor[j],vetor[i]

    vetor[i+1],vetor[fim] = vetor[fim],vetor[i+1]
    return i+1,inicio,fim

def peso(grafo, aresta):
    return grafo[aresta[0]][aresta[1]]

def ordena_arestas(grafo):
    arestas_ordenadas = []
    for u,vizinhos in grafo.items():
        for v,peso in vizinhos.items():
            arestas_ordenadas.append(tuple([u, v, peso]))
    quicksort(arestas_ordenadas,0,len(arestas_ordenadas)-1)
    return arestas_ordenadas

sets = {}

def makeSet(x):
    sets[x] = set([x])

def find(x):
    for representative,subset in sets.items():
        if x in subset:
            return representative
    return None

def union(x, y):
    xRepresentative = find(x)
    yRepresentative = find(y)
    sets[yRepresentative] = sets[yRepresentative].union(sets[xRepresentative])
    del sets[xRepresentative]

def kruskal(grafo):
    arestas_ordenadas = ordena_arestas(grafo)
    arvore_geradora_minima = []
    for v in grafo.keys():
        makeSet(v)
    for aresta in arestas_ordenadas:
        if find(aresta[0]) != find(aresta[1]):
            arvore_geradora_minima.append(aresta)
            union(aresta[0], aresta[1])

    return arvore_geradora_minima