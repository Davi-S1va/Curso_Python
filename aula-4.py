import random
ig=""
for _ in range(9):
    ig+=str(random.randint(0,9))

str_entrada=f"{int(ig):,}".replace(',','.')
#----------------------------------------------------------
entrada=(str_entrada).replace(".","")

numero_int1=[int(caracter)for caracter in entrada]

somatori_1=[10,9,8,7,6,5,4,3,2] 
i=0
for n1, n2 in zip(numero_int1,somatori_1):
    r=n1*n2
    i+= r

digito_1=(i*10)%11
digito_1=digito_1 if digito_1<=9 else 0

#-----------------------------------------------------------------

cpf2_int=numero_int1+[digito_1]

somatori_2=[11,10,9,8,7,6,5,4,3,2]

p=0
for numero1, numero2 in zip(cpf2_int,somatori_2):
    conta=numero1*numero2
    p+=conta

digito_2=(p*10)%11
digito_2=digito_2 if digito_2<=9 else 0
#-----------------------------------------------------------------

print(f"{str_entrada}-{digito_1}{digito_2}")