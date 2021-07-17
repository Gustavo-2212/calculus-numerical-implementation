import metodosZeros as mz

def main():
    inteiro = False
    flutuante = False
    if inteiro:
        print('Informe um valor: ')
        num = int(input())
        print('Informe uma base de conversão: ')
        base = int(input())

        vetor = mz.conversor_inteiro(num, base)
        print(vetor)

    if flutuante:
        print('Informe um valor com ponto flutuante, de modo que seja menor que 1: ')
        num = float(input())

        vetor_float = mz.conversor_flutuante(num)
        print(vetor_float)


if __name__ == '__main__':
    main()
