import math
numero = int(input("Digite um numero menor ou igual a 1000: "))
if numero <= 1000:
    centena = numero / 100
    centena_final = math.floor(float(centena))
    resto_centena = centena - centena_final
    resto = resto_centena * 100
    dezena = resto / 10
    dezena_final = math.floor(float(dezena))
    unidade = dezena - dezena_final
    unidade_final = unidade * 10
    print(f"Centenas: {centena_final}\nDezenas: {dezena_final}\nUnidades: {round(unidade_final)}" )
    
else:
    print("Erro\nDigite um numero valido!")