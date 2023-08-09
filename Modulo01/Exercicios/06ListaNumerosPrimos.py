# Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

novaLista = [num for num in numeros if num > 1 and all(num % i != 0 for i in range(2, num))]

print(novaLista)