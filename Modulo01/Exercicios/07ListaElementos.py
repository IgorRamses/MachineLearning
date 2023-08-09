# Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.

listaUm = [3, 8, 12, 15, 20, 22, 25, 28, 30, 35, 40]
listaDois = [3, 15, 21, 22, 25, 28, 30, 32, 35, 38, 42]

numerosUnicosLista = []

for unidade in listaUm:
    if unidade not in listaDois:
        numerosUnicosLista.append(unidade)
        
for unidade in listaDois:
    if unidade not in listaUm:
        numerosUnicosLista.append(unidade)
        
print(numerosUnicosLista)