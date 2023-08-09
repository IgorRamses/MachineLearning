# Dada uma lista de strings ['banana', 'maçã', 'laranja', 'abacaxi'],
# crie uma nova lista com as palavras que têm mais de 5 letras e outra lista com as palavras que terminam com a.

frutas = ['banana', 'maçã', 'laranja', 'abacaxi']

palavrasMaiorCincoLetras = [fruta for fruta in frutas if len(fruta) > 5]
print(palavrasMaiorCincoLetras)

palavrasTerminandoEmA = [fruta for fruta in frutas if fruta[-1] == 'a']
print(palavrasTerminandoEmA)