new_produtos=[{}]

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
def organiza(x):
 return sorted(x,key=lambda item: item['nome'],reverse=True)
produtos_ordenados = organiza(produtos)

# Exibindo o resultado
for produto in produtos_ordenados:
    preco=float(produto['preco'])
    desconto=(preco*10)/100
    aplicado=preco+desconto
    produtos_ordenados = organiza(produtos)
    todos=produto['nome'],aplicado
    new_produtos.append(todos)
    # print(f"{produto['nome']}: R$ {aplicado:.2f}")


