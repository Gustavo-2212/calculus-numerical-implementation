import math

def gaussPivoteamento(A, b):
    # acessar as linhas
    for i in range(len(A)):
        # verificar o maior pivô
        pivo = math.fabs(A[i][i])
        linhaPivo = i
        # (em linhas) vai de abaixo da linha atual até o final de A
        for j in range(i+1, len(A)):
            if math.fabs(A[j][i]) > pivo:
                pivo = math.fabs(A[j][i])
                linhaPivo = j

        # trocar as linhas
        if linhaPivo != i:
            linhaAux = A[i]
            A[i] = A[linhaPivo]
            A[linhaPivo] = linhaAux

            bAux = b[i]
            b[i] = b[linhaPivo]
            b[linhaPivo] = bAux

        # eliminação gaussiana
        for m in range(i+1, len(A)):
            mult = A[m][i] / A[i][i]
            # n - coluna
            for n in range(i, len(A)):
                A[m][n] -= mult*A[i][n]
            b[m] -= mult*b[i]
    # print de A e b
    print('\n\tMatriz A (coeficientes) escalonada\n')
    for k in range(len(A)):
        print(A[k])
    print('\n\n\n\tVetor B, escalonada\n', b)
    calculaSolucao(A, b)


def calculaSolucao(A, b):
    vetor = [0]*len(A)
    linha = len(A) - 1
    while linha >= 0:
        x = b[linha]
        coluna = len(A) - 1
        while coluna > linha:
            x -= A[linha][coluna]*vetor[coluna]
            coluna -= 1
        x = x / A[linha][linha]
        linha -= 1
        vetor[coluna] = x
    print('\n\n\tVetor Solução\n', vetor, '\n')


def main():
    alfa = 0.7071
    A = [
        [-alfa, 0, 0, 1, alfa, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [-alfa, 0, -1, 0, -alfa, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, -alfa, -1, 0, 0, alfa, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, alfa, 0, 1, 0, alfa, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, -1, -alfa, 0, 0, 1, alfa, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, -alfa, 0, -1, 0, -alfa, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, alfa, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -alfa, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -alfa, -1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, alfa, 0, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -alfa, -1]
    ]

    b = [0, 0, 0, 10, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 10, 0]
    gaussPivoteamento(A, b)


if __name__ == '__main__':
    main()