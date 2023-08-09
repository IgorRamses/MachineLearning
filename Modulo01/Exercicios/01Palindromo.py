# Escreva um programa que solicite ao usuário uma palavra e verifique se ela é um palíndromo (igual ao ler de trás pra frente).

def palindromoTrue(palavra):
	return palavra == palavra[::-1]

palavra = input("Digite uma palavra: ")

resposta = palindromoTrue(palavra)

if resposta:
	print("Essa palavra é um palíndromo")
else:
	print("Essa palavra não é um palíndromo")
