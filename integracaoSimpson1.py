import math

def funcao(x):
    return 1 / math.sqrt(x)

def simpson1(a, b, n): 
    if n % 2 != 0:
        return "Não são intervalos par, a regra não contempla essa possibilidade!"
    else:
        y = []
        x = []
        h = (b - a)/n
        x.append(a)
        while a < b:
            a += h
            x.append(a)
        for i, e in enumerate(x):
            y.append(funcao(e))        
        I = y[0]
        for i in range(1, (n-1)):
            if i % 2 == 0:
                I += 4*y[i]
            else:
                I += 2*y[i]
        I = (h/3)*(I + y[n])
        return I


def main():
    resultado = simpson1(2, 14, 1000000)
    # simpson: parâmetros(a = 2; b = 14; número de trapézios: 10^6)
    print("\n\nResultado: ", resultado, "\n\n")


if __name__ == '__main__':
    main()
