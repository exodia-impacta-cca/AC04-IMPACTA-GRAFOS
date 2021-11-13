from ac04_ex_03 import *

grafo = {
    'Bauru': {'Sao Carlos': 174.6, 'Sao Paulo': 178.3, 'Campinas': 261.6},
    'Campinas': {'Indaiatuba': 28.6, 'Sorocaba': 88.9, 'Itapevi': 98.0, 'Bauru': 261.6},
    'Itapevi': {'Sorocaba': 73.6, 'Campinas': 98.0},
    'Osasco': {'Indaiatuba': 100.0, 'Sao Paulo': 21.7},
    'Registro': {'Campinas': 259.1, 'Sorocaba': 160.5, 'Sao Paulo': 191.9},
    'Sao Carlos': {'Campinas': 146.2, 'Bauru': 174.6, 'Sao Paulo': 315.6 },
    'Sao Paulo': {'Sorocaba': 99.0, 'Indaiatuba': 103.4, 'Sao Carlos': 315.6, 'Registro': 191.9, 'Osasco': 21.7},
    'Sorocaba': {'Campinas': 88.9, 'Indaiatuba': 65.7, 'Sao Paulo': 99.0, 'Registro': 160.5, 'Itapevi': 73.6},
    'Indaiatuba': {'Campinas': 28.6, 'Osasco': 100.0, 'Sao Paulo': 103.4, 'Sorocaba': 65.7}
}


def quicksort(vetor,inicio,fim):
    if(inicio < fim):
        q = pQSort(vetor,inicio,fim) #q[0] = pivo; q[1] = inicio; q[2] = fim
        quicksort(vetor, q[1],q[0]-1) #(vetor, inicio, pivo-1)
        quicksort(vetor, q[0]+1,q[2]) #(vetor, pivo+1, fim)

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
            arestas_ordenadas.append(tuple([u, v]))
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



# arvore_geradora_minima = kruskal(grafo)
# print(arvore_geradora_minima)

