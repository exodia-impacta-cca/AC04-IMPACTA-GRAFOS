import networkx as nx
import matplotlib.pyplot as plt

# Quantidade de cidades diferentes = 9
# Quantidade de arestas que tem que dar = 8

cidadeDistancia = []
# pega do arquivo e transfoma em lista de dicionários
with open('cidadedistancia.csv', 'r') as csvfile:
    for line in csvfile:
        l = line.strip().split(';')
        dis = (
            l[0], l[1] ,float(l[2])
        )
        cidadeDistancia.append(dis)

# ordena o dict pela menor distância
cidadeDistancia = sorted(cidadeDistancia, key=lambda cidadeDistancia: cidadeDistancia[0])

# cria grafo
FG = nx.Graph()

# adiciona vértices e arestas a partir do arquivo
FG.add_weighted_edges_from(cidadeDistancia)

# mostra valores de vértices e pesos das arestas
for (u, v, wt) in FG.edges.data('weight'):
    print(f"({u}, {v}, {wt})")

# printa grafo
nx.draw(FG, with_labels=True, font_weight='bold')
plt.show()