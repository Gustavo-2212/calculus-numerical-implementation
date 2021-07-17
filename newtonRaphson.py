import metodosZeros as mz

def main():
    grau = int(input('Grau da função: '))
    coeficientes = mz.definir_funcao(grau)

    x0 = float(input('Informe o valor aproximado inicial: '))
    precisao1 = float(input('Precisão 1: '))
    precisao2 = float(input('Precisão 2: '))

    print('[x\tf(x)\tITERAÇÕES]\n')
    vetor = mz.newtonRaphson(coeficientes, grau, x0, precisao1, precisao2)
    for i in range(0, len(vetor)):
        print(vetor[i])


if __name__ == '__main__':
    main()
