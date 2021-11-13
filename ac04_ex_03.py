import networkx as nx
import matplotlib.pyplot as plt

# Quantidade de cidades diferentes = 9
# Quantidade de arestas que tem que dar = 8
def leCsvCriaListaDistancias(caminhoArquivo):
    cidadeDistancia = []
    # pega do arquivo e transfoma em lista de dicionários
    with open(caminhoArquivo, 'r') as csvfile:
        for line in csvfile:
            l = line.strip().split(';')
            dis = (
                l[0], l[1] ,float(l[2])
            )
            cidadeDistancia.append(dis)
    # ordena o dict pela menor distância
    cidadeDistancia = sorted(cidadeDistancia, key=lambda cidadeDistancia: cidadeDistancia[0])
    return cidadeDistancia


def criaGrafoList(listaDistancias):
    grafo = dict()
    visitados = dict()
    for distanc in listaDistancias:
        if distanc[0] not in grafo.keys():
            grafo[distanc[0]] = [[distanc[1], distanc[2]]]
        else:
            l = [x for x in grafo[distanc[0]]]
            l.append([distanc[1], distanc[2]])
            grafo[distanc[0]] = l
            #a1, a2 = grafo[distanc[0]][0], grafo[distanc[0]][1]
            #grafo[distanc[0]] = [a1, a2, distanc[1], distanc[2]]

    #     # origem destino distancia  # distancia0 destino1 origem2
    # for distanc in listaDistancias:
    #     #distanc = distanc[::-1]
    #     if distanc[1] not in grafo.keys():
    #         grafo[distanc[1]] = [distanc[0], distanc[2]]
    #     else:
    #         l = [x for x in grafo[distanc[2]]]
    #         grafo[distanc[1]] = [l, distanc[1], distanc[0]]
    #         #a1, a2 = grafo[distanc[2]][0], grafo[distanc[2]][1]
    #         #grafo[distanc[1]] = [a1, a2, distanc[1], distanc[0]]
    return grafo


def criaGrafoDict(listaDistancias):
    grafo = dict()
    for distanc in listaDistancias:
        #  origem[0], destino[1] distancia [2] 
        if distanc[0] not in grafo.keys():
            grafo[distanc[0]] = []
            v = {distanc[1]:distanc[2]}
            grafo[distanc[0]] = v
        else:
            antes =  grafo[distanc[0]]
            v = {distanc[1]:distanc[2]}
            grafo[distanc[0]] = antes, v

        #  origem[0], destino[1] distancia [2] 
        if distanc[1] not in grafo.keys():
            grafo[distanc[1]] = []
            v = {distanc[0]:distanc[2]}
            grafo[distanc[1]] = v
        else:
            antes =  grafo[distanc[1]]
            v = {distanc[0]:distanc[2]}, antes
            grafo[distanc[1]] = v

    return grafo



def desenhaGrafo(listaCidadeDistancia):
    # cria grafo
    G = nx.Graph()
    # adiciona vértices e arestas a partir do arquivo
    G.add_weighted_edges_from(listaCidadeDistancia)
    # mostra valores de vértices e pesos das arestas
    sum_weight = 0
    for (u, v, wt) in G.edges.data('weight'):
        sum_weight += wt
        print(f"({u}, {v}, {wt})")
    print(f'{sum_weight:.2f}')
    # printa grafo
    pos=nx.spring_layout(G) 
    nx.draw_networkx(G,pos)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
