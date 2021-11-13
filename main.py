from ac04_ex_03 import *
from pythonKruskal import *

csv = 'cidadedistancia.csv'
distanc =leCsvCriaListaDistancias(csv)
grafo = criaGrafoDict(distanc)

arvore_geradora_minima = kruskal(grafo)
print(arvore_geradora_minima)

desenhaGrafo(arvore_geradora_minima)
desenhaGrafo(distanc)