import metodosZeros as mz

def main():
    grau = int(input('Ordem da função: '))

    coeficientes = mz.definir_funcao(grau)
    erro = float(input('Erro do tipo 0.1, por exemplo.: '))
    a = float(input('Intervalo\na: '))
    b = float(input('b: '))
    iteracoes = mz.definir_iteracoes(a, b, erro)

    print('\t[ iterações, x, y(x), Erro Relativo, Erro Absoluto]\n')
    vetor = mz.metodo_bisseccao(coeficientes, a, b, erro, iteracoes)
    print('\tMétodo da bissecção\n')
    for i in range(0, len(vetor)):
        print(vetor[i])

    print('\n\tMétodo da posição falsa\n')
    vetor_pos_falsa = mz.posicao_falsa(coeficientes, a, b, erro)
    for i in range(0, len(vetor_pos_falsa)):
        print(vetor_pos_falsa[i])


if __name__ == '__main__':
    main()

