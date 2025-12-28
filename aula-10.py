
import string
perguntas = [ {
            'pergunta':'Pergunta 1- Quanto é 2+2?',
            'opção':['1', '3', '4', '5'],
            'resposta':'C',
        },
        {    "pergunta":"Pergunta 2- Quantas champions CR7 tem?",
            "opção":['7','4','9','5'],
            "resposta":'D'
        },
        {    'pergunta':'Pergunta 3- Quantas copa o Brasil tem?',
            'opção':['5','8','4','6'],
            'resposta': "A"
        
        },]
tentativa=0
for pergunta in perguntas:
        print( pergunta['pergunta'])
        print()

        opcoes=pergunta['opção']
        for letra,opcao in zip(string.ascii_uppercase,opcoes):
            print(f'{letra})',opcao)

        escolha = input('Escolha uma opção: ').title()

        qtd_opcoes = len(opcoes)
        acertou=False
        qtd_escolha=len(escolha)

        if escolha == pergunta['resposta']:
                        acertou = True

  
        if acertou:
            print('Acertou 👍')
        else:
            tentativa += 1
            print('Errou ❌')

        print(f"Quantidade de tentativa: {tentativa}")
    
    
      

            
           