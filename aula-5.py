def soma(*args):
    r=1
    for numero in args: 
        r*=numero
    return r
        
entrada=input("Digite os vlores:").replace(",","").replace("-","")
tratador=[int(numero)for numero in entrada]
somatoria=soma(*tratador)
print(somatoria)
 