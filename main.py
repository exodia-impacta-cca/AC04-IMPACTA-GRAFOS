from ac04_ex_03 import *
from pythonKruskal import *

grafo = {
    'Bauru': {'Sao Carlos': 174.6, 'Sao Paulo': 178.3, 'Campinas': 261.6},
    'Campinas': {'Indaiatuba': 28.6, 'Sorocaba': 88.9, 'Itapevi': 98.0, 'Bauru': 261.6,'Registro': 259.1, 'Sao Carlos':146.2},
    'Itapevi': {'Sorocaba': 73.6, 'Campinas': 98.0},
    'Osasco': {'Indaiatuba': 100.0, 'Sao Paulo': 21.7},
    'Registro': {'Campinas': 259.1, 'Sorocaba': 160.5, 'Sao Paulo': 191.9},
    'Sao Carlos': {'Campinas': 146.2, 'Bauru': 174.6, 'Sao Paulo': 315.6 },
    'Sao Paulo': {'Sorocaba': 99.0, 'Indaiatuba': 103.4, 'Sao Carlos': 315.6, 'Registro': 191.9, 'Osasco': 21.7},
    'Sorocaba': {'Campinas': 88.9, 'Indaiatuba': 65.7, 'Sao Paulo': 99.0, 'Registro': 160.5, 'Itapevi': 73.6},
    'Indaiatuba': {'Campinas': 28.6, 'Osasco': 100.0, 'Sao Paulo': 103.4, 'Sorocaba': 65.7}
}

#arvore_geradora_minima = kruskal(grafo)
#print(arvore_geradora_minima)

csv = 'cidadedistancia.csv'
G = criaGrafoDict(leCsvCriaListaDistancias(csv))
for k,v in G.items():
    print(k, v)

print(G)