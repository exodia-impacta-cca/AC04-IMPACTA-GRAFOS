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

def kruskal(grafo):
    # arvore geradaora miníma a retornar após aplicar o algoritmo de kruskal
    arvore = dict()

    # ordena o grafo pela distância
    grafo = sorted(G.edges.data('weight'), key=lambda cidadeDistancia: cidadeDistancia[2])

    # percorrer grafo com (origem, destino, distância) ordenado do menor para maior

    # marcar vertices com conexões

    # se vertice atual, não tiver a mesma marcação na origem e destino, pode se juntar





# cria grafo
G = nx.Graph()

# adiciona vértices e arestas a partir do arquivo
# subtituir cidadeDistancia pelo retorno do método de kruskal
G.add_weighted_edges_from(cidadeDistancia)

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
