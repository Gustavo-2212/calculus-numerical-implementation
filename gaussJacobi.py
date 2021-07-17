def gaussJacobi(matriz, b, x0, precisao):
    # Obtendo matriz C e g
    C = []
    g = []
    elementoC = 0
    elementoG = 0
    dPrincipal = 0
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz)):
            if i == j:
                dPrincipal = matriz[i][j]
                elementoC = 0
                elementoG = b[i] / dPrincipal
            else:
                dPrincipal = matriz[i][i]
                elementoC = (-1)*matriz[i][j]/dPrincipal
            C.append(elementoC)
        g.append(elementoG)
        dPrincipal = 0
        elementoC = 0
        elementoG = 0

    # Transformando o vetor C em uma matriz nxn    
    a = 0
    matrizC = []
    for i in range(0, len(matriz)):
        vet = []
        for j in range(0, len(matriz)):
            vet.append(C[a])
            a += 1
        matrizC.append(vet)

    # Cálculo das aproximações
    k = 0
    erro = 1
    n = len(x0)
    while erro > precisao and k <= 5:
        x = [0]*n
        for i in range(0, len(matriz)):
            for j in range(0, len(matriz)):
                x[i] += matrizC[i][j]*x0[j]
            x[i] += g[i]

        valor = 0
        maior = 0
        for i in range(0, len(matriz)):
            if valor <= abs(x[i] - x0[i]):
                valor = abs(x[i] - x0[i])
            if maior <= abs(x[i]):
                maior = abs(x[i])
        erro = valor / maior
        if erro <= precisao:
            break
        else:
            x0 = x
        k += 1
    return x

def main():
    # Dados de entrada
    matriz = [
        [10, 2, 1],
        [1, 5, 1],
        [2, 3, 10]
    ]
    b = [7, -8, 6]
    x0 = [0.7, -1.6, 0.6]
    precisao = 0.05
    print('\nVetor solução de x: ', gaussJacobi(matriz, b, x0, precisao))


if __name__ == '__main__':
    main()

