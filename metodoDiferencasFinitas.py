import eliminacaoGaussPivoParcial as eg
import gaussSeidel as gs
import gaussJacobi as gj
import os
from math import e

def construirMalhas(a, b, N):
    x = []
    h = (b - a)/(N - 1)

    while(a<=b):
        x.append(a)
        a += h
    return x, h


def construitProblemaDiscreto(N, h, malha):
    A = []
    for i in range(N):
        A.append([0]*N)
    b = [0]*N

    A[0][0] = 1
    #b[0] = f(a)
    b[0] = 0
    for i in range(1, (N - 1)):
        # Depende da função na EOD
        A[i][i-1] = 1
        A[i][i] = -2
        A[i][i+1] = 1
        #b[i] = f(xi, ui)h^2
        b[i] = -200 * (h**2) * e**(-1*malha[i] + 1)
    #Depende dos valores informados
    #b[N-1] = f(b)
    A[N-1][N-1] = 1
    b[N-1] = 100

    return A, b


def main():
    N = 201
    a = 0
    b = 2
    malha, h = construirMalhas(a, b, N)

    print("Malha: ",malha)

    A, B = construitProblemaDiscreto(N, h, malha)
    resultado = eg.gaussPivoteamento(A, B)

    vet = []
    for i in range(N):
        vet.append(0)
    print(vet)
# IMPRESSÃO DOS RESULTADOS
    print("-"*140)
    print("\tEliminação de Gauss com Pivotemanto Parcial\nVetor Solução: \n\t", resultado)

    resultadoGaussSeidel = gs.gaussSeidel(A, B, vet, 20)
    print("\n\tGaussSeidel\nVetor Solução: \n\t", resultadoGaussSeidel)

    resultadoGaussJacobi = gj.gaussJacobi(A, B, vet, 0) # Máximo de 9 iterações
    print("\n\tGauss-Jacobi\nVetor Solução: ")
    print("\t",resultadoGaussJacobi)


if __name__ == '__main__':
    main()