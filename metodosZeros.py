import random
import math

# Encontrar zeros reais das funções
def definir_funcao(grau):
    coeficientes = []
    c = 'a'
    num = int(ord(c))
    for i in range(1, grau+1):
        coeficientes.append(float(input(f'{c}: ')))
        num += 1
        c = chr(num)
    c = chr(num)
    coeficientes.append(float(input(f'{c}: ')))
    return coeficientes

def teoremaDeBolzano(coeficientes, a, b):
    ordem = (len(coeficientes) - 1)
    f1 = 0
    f2 = 0
    for i in range(0, len(coeficientes)):
        f1 = f1 + coeficientes[i]*(a ** ordem)
        f2 = f2 + coeficientes[i]*(b ** ordem)
        ordem = ordem - 1
    return f1*f2

## Métodos úteis -----------------------------------
def calcul_fx(coeficientes, x):
    ordem = (len(coeficientes) - 1)
    f = 0
    for i in range(0, len(coeficientes)):
        f = f + coeficientes[i]*(x ** ordem)
        ordem = ordem - 1
    return f

def derivada_fx(coeficientes, grau):
    
    derivada = [0]*(len(coeficientes) - 1)
    
    if len(coeficientes) > 1:
        m = len(coeficientes) - 1
        for i in range(0, (len(coeficientes) - 1)):
            derivada[i] = coeficientes[i]*m
            m -= 1
    else:
        derivada.append(0)
    return derivada
## -----------------------------------

def metodo_bisseccao(coeficientes, a, b, e, iteracoes):
    erro_secundario = 0
    vet = []
    it = 0
    erro = abs(a - b)
    x = a
    print(iteracoes)
    while erro > e and it < iteracoes:
        x_anterior = x
        x = (a + b)/2
        if teoremaDeBolzano(coeficientes, x, a) < 0:
            b = x
        else:
            a = x
        it += 1
        erro_relativo = abs( ((x - x_anterior)/x) )
        erro = abs(b - a)
        funcao = calcul_fx(coeficientes, x)
        vet.append([it, x, funcao, erro_relativo, erro])
    return vet

def definir_iteracoes(a, b, erro):
    iteracoes = (math.log10((b - a)) + math.log10(erro)) / math.log10(2)
    iteracoes = int(round(iteracoes))
    return abs(iteracoes)

def posicao_falsa(coeficientes, a, b, e):
    erro_secundario = 0
    vet = []
    it = 0
    erro = abs(b - a)
    x = a
    while erro > e:
        x_anterior = x
        f_a = abs(calcul_fx(coeficientes, a))
        f_b = abs(calcul_fx(coeficientes, b))
        x = (a * f_b + b * f_a) / (f_b + f_a)
        if abs(calcul_fx(coeficientes, x)) < e or erro < e or f_a < e or f_b < e:
            it += 1
            erro_relativo = abs( ((x - x_anterior)/x) )
            erro = abs(b - a)
            funcao = calcul_fx(coeficientes, x)
            vet.append([it, x, funcao, erro_relativo, erro])
            break
        else:
            if teoremaDeBolzano(coeficientes, x, a) < 0:
                b = x
            else:
                a = x
            it += 1
            erro_relativo = abs( ((x - x_anterior)/x) )
            erro = abs(b - a)
            funcao = calcul_fx(coeficientes, x)
            vet.append([it, x, funcao, erro_relativo, erro])
    return vet

# Método do Ponto Fixo
def mpf(coeficientes, x0, precisao1, precisao2, equacaoIteracao):
	if abs(mz.calcul_fx(coeficientes, x0)) < precisao1:
		x = x0
	else:
		k = 1
		vet = []

		while True:
			x1 = mz.calcul_fx(equacaoIteracao, x0)

			if (abs(mz.calcul_fx(coeficientes, x1)) < precisao1) or (abs(x1 - x0) < precisao2):
				x = x1
				#vet.append([x, mz.calcul_fx(coeficientes, x), (k-1)])
				break
			else: 
				vet.append([x1, mz.calcul_fx(coeficientes, x1), k])
			x0 = x1
			k = k + 1
	return vet

# Newton Raphson
def newtonRaphson(coeficientes, grau, x0, precisao1, precisao2):
    vet = []
    derivada = derivada_fx(coeficientes, grau)

    vet.append([x0, calcul_fx(coeficientes, x0), 0])
    if (abs(calcul_fx(coeficientes, x0)) < precisao1):
        vet.append([x0, calcul_fx(coeficientes, x0), 0])
    else:
        k = 1
        while True:
            x = x0 - ( calcul_fx(coeficientes, x0) / calcul_fx(derivada, x0) )
            if (abs(calcul_fx(coeficientes, x)) < precisao1) or (abs(x - x0) < precisao2):
                vet.append([x, calcul_fx(coeficientes, x), k])
                break
            else:
                vet.append([x, calcul_fx(coeficientes, x), k])
            x0 = x
            k += 1
    return vet

# Conversão
def conversor_inteiro(num, base):
    vet = []

    while True:
        resto = num % base
        num = (int)((num - resto)/base)
        if num >= base:
            vet.append(resto)
        else:
            vet.append(resto)
            vet.append(num)
            break
    vet.reverse()
    return vet

def conversor_flutuante(num):
    vet = [0, '.']
    for i in range(0, 100):
        num *= 2
        parte_inteira = int(math.modf(num)[1])
        parte_fracionaria = float(math.modf(num)[0])
        if parte_fracionaria == 0.0 and parte_inteira == 1:
            vet.append(parte_inteira)
            break
        elif parte_inteira == 1:
            num -= parte_inteira
            vet.append(parte_inteira)
        else:
            vet.append(parte_inteira)
    return vet

