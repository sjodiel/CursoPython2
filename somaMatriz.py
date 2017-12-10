def soma_matrizes(m1,m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False

    resultado = []
    for i in range(len(m1)):
        resultado.append([])
        for j in range(len(m1[0])):
            resultado[i].append(m1[i][j] + m2[i][j])
    return resultado

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]

print(soma_matrizes(m1, m2))

m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]

print(soma_matrizes(m1, m2))