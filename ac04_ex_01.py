def arvoreGeradora(Matriz_D, Matriz_A):
    import numpy as np
    # L = (D - A)
    l = np.array(Matriz_D) - np.array(Matriz_A)

    # REMOVE 1 LINHA E 1 COLUNA
    l = np.delete(l,0,0)
    l = np.delete(l,0,1)

    # RELAIZA CALCULO DETERMINANTE DA MATRIZ LAPLACIANA 
    return round(np.linalg.det(l))

matGraus = [  
    [3,0,0,0],
    [0,2,0,0],
    [0,0,2,0],
    [0,0,0,3]
]

matAdj = [  
    [0,1,1,1],
    [1,0,0,1],
    [1,0,0,1],
    [1,1,1,0]
]


print("Quantidade de arvores possíveis:")
print(arvoreGeradora(matGraus, matAdj))