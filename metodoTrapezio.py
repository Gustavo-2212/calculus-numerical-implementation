import math

def funcao(x):
    return 1 / math.sqrt(x)

# n: número de intervalos
def integral(a, b, n):
    # cálculo da base do trapézio
    x = []
    y = []
    h = (b - a)/n
    x.append(a)
    while a < b:
        a += h
        x.append(a)
    for i, e in enumerate(x):
        y.append(funcao(e))
    
    I = y[0]
    for i in range(1, n-1):
        I += I + 2*y[i]
    I = (y[n] + I)*h/2
    return I


def main():
    resultado = integral(2, 14, 1)
    print(resultado)


if __name__ == '__main__':
    main()
    