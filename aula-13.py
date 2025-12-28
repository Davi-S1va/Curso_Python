pessoas={
    'nome1':'Bruno',
    'nome2':'Sergio',
    'nome3':'Brian', 

    'sobrenome1':'Henrique',
    'sobrenome2': 'Junior',
    'sobrenome3':'Moser',
}
descricao= {
    'idade1':16,
    'altura1': 1.88,
    'idade2':18,
    'altura2':1.60,
    'idade3':45,
    'altura3':'2.7',
}

pessoas_completa={**pessoas, **descricao}

def mostrar_argumentos_nomeados(*args, **kwargs):
    print("Não Nomeados",args)

    for chave, valor in kwargs.items():
        print(chave,":",valor)

mostrar_argumentos_nomeados(**pessoas_completa)
