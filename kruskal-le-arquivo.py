# Quantidade de cidades diferentes = 9
# Quantidade de arestas que tem que dar = 8

cidadeDistancia = []

# pega do arquivo e transfoma em lista de dicionários
with open('cidadedistancia.csv', 'r') as csvfile:
    for line in csvfile:
        l = line.strip().split(';')
        dis = {
            'distanc': float(l[2]),
            'origem' :  l[0],
            'destino' : l[1]  
        }
        cidadeDistancia.append(dis)

# ordena o dict pela menor distância
cidadeDistancia = sorted(cidadeDistancia, key=lambda cidadeDistancia: cidadeDistancia['distanc'])

# Verifica se já visitou o vértice, se não add ele na lista de visitados
cidPercorridas = []

# mostra cidades percorridas
for i in cidPercorridas:    
    print(i)

print(len(cidPercorridas))
