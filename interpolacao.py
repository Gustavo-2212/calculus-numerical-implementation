import eliminacaoGaussPivoParcial as ep

def matriz(x, grau):
    matriz = []
    vet = []
    n = len(x)
    for j in range(0, n):
        for i in range(0, (grau+1)):
            vet.append(x[j]**i)
        matriz.append(vet) 
        vet = []       
    return matriz


x = [0.1, 0.2, 0.3, 0.4]
f = [5, 13, -4, -8]
# Grau = 2
grau = 3
A = matriz(x, grau)
resultado = ep.gaussPivoteamento(A, f)
print(resultado)


