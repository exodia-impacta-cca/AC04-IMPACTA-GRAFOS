import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.bipartite.basic import color
from networkx.algorithms.distance_measures import center

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



def criaGrafoDict(listaDistancias):
    grafo = dict()
    for distanc in listaDistancias:
        #  origem[0], destino[1] distancia [2] 
        if distanc[0] not in grafo.keys():
            grafo[distanc[0]] = {}
            v = {distanc[1]:distanc[2]}
            grafo[distanc[0]] = v
        else:
            antes = grafo[distanc[0]]
            antes[distanc[1]] = distanc[2]
            grafo[distanc[0]] = antes

        if distanc[1] not in grafo.keys():
            grafo[distanc[1]] = {}
            v = {distanc[0]:distanc[2]}
            grafo[distanc[1]] = v
        else:
            antes = grafo[distanc[1]]
            antes[distanc[0]] = distanc[2]
            grafo[distanc[1]] = antes

    return grafo



def desenhaGrafoComPeso(listaCidadeDistancia):
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
    options = {
        "font_size": 24,
        "node_size": 3000,
        "node_color": "white",
        "edgecolors": "black",
        "linewidths": 5,
        "width": 5,
    }
    peso_total = f'Peso total: {sum_weight:.2f}'
    pos=nx.spring_layout(G) 
    nx.draw_networkx(G,pos)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.text(0.15, 1, peso_total, color = 'black', size = 24)
    plt.show()


def desenhaGrafo(listaCidadeDistancia):
    import networkx as nx
    import matplotlib.pyplot as plt
    g = nx.Graph()
    for edge in listaCidadeDistancia:
        g.add_edge(edge[0], edge[1])
    options = {
        "font_size": 24,
        "node_size": 3000,
        "node_color": "white",
        "edgecolors": "black",
        "linewidths": 5,
        "width": 5,
    }
    nx.draw_networkx(g, **options)
    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.05)
    plt.axis("off")
    plt.show()