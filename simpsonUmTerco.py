import math

def funcao(x):
    return (1 / math.sqrt(x))

def umTercoSimpson(a, b, n):
    x = []
    y = []
    h = (b - a) / (2*n)
    #x.append(a)
    while a < b:
        #a += h 
        x.append(a)   
        a += h
    for i, e in enumerate(x):
        y.append(funcao(e))
    I = 0
    for i in range(1, (n-1)):
        I += (y[2*i] + 4*y[2*i + 1] + y[2*i + 2])

    I = I * (h/3)
    return I


def main():
    resultado = umTercoSimpson(2, 14, 1000000)
    # umTercoSimpson: parâmetros(a = 2; b = 14; número de trapézios: 10^6)
    print("\n\nResultado: ", resultado, "\n\n")


if __name__ == '__main__':
    main()

