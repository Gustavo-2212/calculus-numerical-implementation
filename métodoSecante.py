import metodosZeros as mz

def metodoSecante(coeficientes, grau, x0, x1, precisao1, precisao2):
    vet = []

    if abs(mz.calcul_fx(coeficientes, x0)) < precisao1:
       vet.append([0, x0, mz.calcul_fx(coeficientes, x0)])
    elif abs(mz.calcul_fx(coeficientes, x1)) < precisao1 or abs(x1 - x0) < precisao2:
        vet.append([0, x1, mz.calcul_fx(coeficientes, x1)])
    else:
        k = 1
        while True:
            x = x1 - ( (mz.calcul_fx(coeficientes, x1) / ( mz.calcul_fx(coeficientes, x1) -  mz.calcul_fx(coeficientes, x0) ))*(x1 - x0) )

            if abs(mz.calcul_fx(coeficientes, x)) < precisao1 or abs(x - x1) < precisao2:
                vet.append([k, x, mz.calcul_fx(coeficientes, x)])
                break
            else:
                vet.append([k, x, mz.calcul_fx(coeficientes, x)])
            x0 = x1
            x1 = x
            k += 1
    return vet


def main():
    grau = int(input('Grau da função: '))
    coeficientes = mz.definir_funcao(grau)

    x0 = float(input('Informe o primeiro valor aproximado inicial: '))
    x1 = float(input('Informe o segundo valor aproximado inicial: '))
    precisao1 = float(input('Precisão 1: '))
    precisao2 = float(input('Precisão 2: '))

    print('\t[ITERAÇÕES\tx\tf(x)]\n')
    vetor = metodoSecante(coeficientes, grau, x0, x1, precisao1, precisao2)
    for i in range(0, len(vetor)):
        print(vetor[i])


if __name__ == '__main__':
    main()
