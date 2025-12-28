#verificador de CPF
cpf=input("Digite seu CPF: ")
entrada=(cpf).replace(".","").replace("-","").strip()
selecao_de_numeros=entrada[:9]
cpf1_int=[int(digito)for digito in selecao_de_numeros]
somatori_1=[10,9,8,7,6,5,4,3,2]
i=0
for n1, n2 in zip(cpf1_int,somatori_1):
    r=n1*n2
    i+=r

digito_1=(i*10)%11
digito_1=digito_1 if digito_1<=9 else 0


cpf2_int=cpf1_int+[digito_1]
somatori_2=[11,10,9,8,7,6,5,4,3,2]
p=0
for numero1, numero2 in zip(cpf2_int,somatori_2):
    conta=numero1*numero2
    p+=conta

digito_2=(p*10)%11
digito_2=digito_2 if digito_2<=9 else 0

cpf_true=selecao_de_numeros+ str(digito_1)+ str(digito_2)

if entrada != cpf_true :
    print("O seu CPF é ínvalido ")

elif cpf_true==entrada:
    print("CPF valído")
#adicionar verificação
#criar um gerador