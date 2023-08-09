# Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.

def segundoMaior(lista):
    listaOrdemDecrescente = sorted(lista, reverse = True)
    segundoMaior = listaOrdemDecrescente[1]
    
    return segundoMaior

listaNumerosInteiros = [17, 5, 23, 8, 12, 4, 19, 10, 2, 15, 21, 7, 6, 25, 14, 20, 9, 22, 18, 11, 3, 13, 16, 24]

resultadoFinal = segundoMaior(listaNumerosInteiros)

print(f"O segundo maior número é: {resultadoFinal}.")