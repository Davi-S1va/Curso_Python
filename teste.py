# # entrada=input("Digite os vlores:").replace(",","").replace("-","")
# # tratador=[int(numero)for numero in entrada]
# # print(tratador)
# pessoa = {}

# ##
# ##

# chave = 'nome'

# pessoa[chave] = 'Luiz Otávio'
# pessoa['sobrenome'] = 'Miranda'


# print(pessoa[chave])

# pessoa[chave] = 'Maria'

# del pessoa['sobrenome']
# print(pessoa)
# print(pessoa['nome'])

# # print(pessoa.get('sobrenome'))
# if pessoa.get('sobrenome') is None:
#     print('NÃO EXISTE')
# else:
#     print(pessoa['sobrenome'])

# Exercício - sistema de perguntas e respostas


# # 


# from types import SimpleNamespace

# texto=('timestamp=1746785319 devname="1001-3260-25" devid="FGT40FTK23095012" vd="root" date=2025-05-09 time=10:08:39 eventtime=1746796118774022660 tz="-0300" logid="0100044547" type="event" subtype="system" level="information" logdesc="Object attribute configured" user="ADM-Adriano.Menegass@bancoob.br@For" ui="fgfm_tunnel" action="Delete" cfgtid=1037172738 cfgpath="user.radius" cfgobj="RADIUS-SICOOB" msg="Delete user.radius RADIUS-SICOOB"').replace("=",":").replace('"', '')


# # obj=SimpleNamespace(*texto)
# # print(obj.vd)
# for espaco in texto:
#  espaco=" "
#  texto_v2=texto.replace(espaco,"\n")
# #  print(texto_v2)

# biblioteca = {}
# for linha in texto_v2.strip().splitlines():
#     if ':' in linha:
#         chave, valor = linha.split(':', 1)
#     elif '=' in linha:
#         chave, valor = linha.split('=', 1)
#     else:
#         continue  # pula se não tiver : ou =
#     biblioteca[chave.strip()] = valor.strip()

# print(biblioteca)
 
# lista=[1,77,4,33,8,54,3]
# print(sorted(lista))

# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'Ciranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Boreira'},
#     {'nome': 'Aline', 'sobrenome': 'Almeida'},
# ]

# l1= sorted(lista,key=lambda item: item['sobrenome'])

# print(l1)

# def soma(x,y):
#     return x + y

# x1=soma(1,3)

# print(x1)
# while True:
#         def numero_par(x):
#             if x % 2==0:
#                 print('Numero é par')
                
                
#             else:
#                 print('O numero é ímpar') 
                
            
#         # if numero_par(entrada):

#         def verifica_numero(digito):
#             if digito.isnumeric()==False or digito== None:
#                 print('Numero não reconhecido... tente novamente')
            
            
                
            
#         #     
#         # else:
#         digita_numero=input('Digite um numero,para verficar se ímpar ou par:')

#         verifica_numero(digita_numero)


#         numero_inteiro=int(digita_numero)

#         numero_par(numero_inteiro)
# for numero in range(1,101):
#     if numero>1000:
        
#         continue
#     print(numero)
# lista=[]
# for numero in range(10):
#     lista.append(numero)
# lista=[
#     numero*2
#     for numero in range(10)
# ]
# # print(list(range(10)))
# # print(lista)

# i=0
# for n1,n2 in zip(range(11),range(11)):
#     soma=n1*n2
    
#     print(n1,"x",n2,"=",soma)
import random

print(random.choice(1,2))