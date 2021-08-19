def gaussSeidel(A, b, vetorSolucao, iteracoes):
    iteracao = 0
    while iteracao < iteracoes:
        for i in range(len(A)):
            x = b[i]
            for j in range(len(A)):
                if i != j:
                    x -= A[i][j]*vetorSolucao[j]
            x /= A[i][i]
            vetorSolucao[i] = x
        iteracao += 1
    return vetorSolucao


def main():
    A = [[8,2,-1,0], [2,-4,0,0], [0,-2,8,-1], [0,0,-1,4]]
    b = [1,1,1,1]
    vetorSolucao = [0,0,0,0]
    iteracoes = 20

    resultado = gaussSeidel(A, b, vetorSolucao, iteracoes)
    print(resultado)    


if __name__ == '__main__':
    main()            