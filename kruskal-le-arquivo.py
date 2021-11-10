# Quantidade de cidades diferentes = 9
# Quantidade de arestas que tem que dar = 8

cidadeDistancia = []

# pega do arquivo e transfoma em lista de dicionários
with open('cidadedistancia.csv', 'r') as csvfile:
    for line in csvfile:
        l = line.strip().split(';')
        dis = [
            float(l[2]), l[0], l[1]  
        ]
        cidadeDistancia.append(dis)

# ordena o dict pela menor distância
cidadeDistancia = sorted(cidadeDistancia, key=lambda cidadeDistancia: cidadeDistancia[0])


# Verifica se já visitou o vértice, se não add ele na lista de visitados
cidPercorridas = []

#implementação da adaptação do algoritmo de busca em largura
def kruskal(grafo):
    arvore = dict()
    fila = [grafo[0][0]] # recebe o primeiro elemento
    visitados = []

    while len(fila) > 0:
        v = fila.pop(0)
        visitados.append(v)

    if v not in arvore.keys():
        arvore[v] = []

        for i in range(len(grafo)):
            if grafo[i][0] not in visitados:
                visitados.append(grafo[i][0])
                fila.append(grafo[i][0])
                arvore[v].append(grafo[i][0])

    return arvore

cidPercorridas = kruskal(cidadeDistancia)

# mostra cidades percorridas
for i in cidPercorridas:    
    print(i)

print(len(cidPercorridas))
