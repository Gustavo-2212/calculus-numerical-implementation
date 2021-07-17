import metodosZeros as mz

def main():
	grau = int(input('Digite o grau da sua função: '))
	coeficientes = mz.definir_funcao(grau)

	grauIteracao = int(input('Digite o grau da sua função de iteração: '))
	equacaoIteracao = mz.definir_funcao(grauIteracao)  # x = f(x)

	x0 = float(input('Aproximação inicial: '))
	precisao1 = float(input('Precisão 1: '))
	precisao2 = float(input('Precisão 2: '))

	print('\t[x\tf(x)\titerações]')
	vetor = mz.mpf(coeficientes, x0, precisao1, precisao2, equacaoIteracao)
	for i in range(0, len(vetor)):
		print(vetor[i])


if __name__ == '__main__':
	main()

