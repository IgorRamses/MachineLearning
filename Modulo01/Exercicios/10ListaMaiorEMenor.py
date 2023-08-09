# Dada uma lista contendo números inteiros, como você encontraria o maior número e o menor número dessa lista em uma única passagem ?

def encontraMaiorEMenor(lista):
    maior = max(lista)
    menor = min(lista)
    
    return maior, menor

listaNumerosInteiros = [17, 5, 23, 8, 12, 4, 19, 10, 2, 15, 21, 7, 6, 25, 14, 20, 9, 22, 18, 11, 3, 13, 16, 24]

maiorNumero, menorNumero = encontraMaiorEMenor(listaNumerosInteiros)

print(f"O maior número é {maiorNumero}.")
print(f"O menor número é {menorNumero}.")