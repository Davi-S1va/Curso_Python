tentativa=0
while True:
  quiz={
    "Perguta-1":"Quantas champions CR7 tem?",
    "alternativa-1":['7','9','4','5'],
    "resposta-1":'5'
} 
  
  print(quiz['Perguta-1'])
  
  i=0
  for opcao in quiz['alternativa-1']:
    print(f"{i}){opcao}")
    i+=1
    
 
  
  resposta_do_usuario=input("Digite a alternativa:")


  if resposta_do_usuario != "3":
    print("\nA resposta está ERRADA :( \n Tente Novamente")
    print(f"Número de tentativas= {tentativa}\n\n")
    tentativa+=1
    continue
  
  
  elif resposta_do_usuario == "3":
    print(f"\n \n A resposta está CORRETA!! \nMeus parabéns!! \n A resposta era: {quiz['resposta-1']} ;)\n \n")
    print(f"Número de tentativas= {tentativa}")
  break