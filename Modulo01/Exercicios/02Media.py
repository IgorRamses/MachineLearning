# Escreva um programa que leia números digitados pelo usuário e para quando o número 0 for digitado.
# No final, imprima a média de números digitados.

quantidadeDeNumeros = 0
somaDosNumeros = 0

while True:
    num = int(input("Digite um numero: "))

    if num == 0:
        break
    
    quantidadeDeNumeros = quantidadeDeNumeros + 1
    somaDosNumeros = somaDosNumeros + num
    
print(f"Quantidade de números digitados: {quantidadeDeNumeros}")
print(f"Média geral: {somaDosNumeros / quantidadeDeNumeros}")