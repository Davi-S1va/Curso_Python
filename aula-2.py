
def multipo_de(numero,multiplo):
    resultado=numero%multiplo==0
    print(f"{numero} é multiplo de {multiplo}?",end=" ")
    print(resultado)


multipo_de(16,8)
multipo_de(15,3)