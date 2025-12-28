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
for listas in lista_de_listas_de_inteiros:



        lista=listas
        vistos=set()
        

        for valor in lista:
            tamanho= len(vistos)
            if tamanho>6:
                 valor=-1
                   
            if valor in vistos:
                
                print("Não repetiu"if valor==-1 else"O primeiro valor a se repetir foi:"f"{valor}" )
            
                break
          
            vistos.add(valor) 
        
            #digito_2=digito_2 if digito_2<=9 else 0
        
    



# if s3== set():
#         print("Não houve rpetição")
# else:
#         print(f"O primeiro número a se repetir foi:{s3}")
