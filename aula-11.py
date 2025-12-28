#  Exemplo:
#         [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
#         [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
#         [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
#     Se não encontrar duplicados na lista, retorne -1

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]
# for listas in lista_de_listas_de_inteiros:
#     ...



lista=[5, 3, 1, 8, 5, 7, 1, 8, 8, 7]




lista_1=list( lista[0:5])
lista_2=list(lista[5:])

for valores in lista_1:
        numeros_str=[str(valores)for valores in lista_1]
        s1={*numeros_str}

        for caracter in lista_2:
            numeros_str_2=[str(caracter)for caracter in lista_2]
            s2={*numeros_str_2}



    # s3={ } & {lista_2}


    # s1 = {1, 2, 3}More actions
    # s2 = {2, 3, 4}
s4 = s1 | s2
s3 = s1 & s2
    # s3 = s2 - s1

print(lista_1,"\n", lista_2)
print("S1=",s1)
print("s2=",s2)
if s3== set():
        print("Não houve rpetição")
else:
        print(f"O primeiro número a se repetir foi:{s3}")
