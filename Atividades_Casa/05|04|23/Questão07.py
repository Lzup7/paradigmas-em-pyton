lista_numeros = list()
for i in range(0,3):
  while True:
    try:
        numero = int(input("Digite um numero: "))
        lista_numeros.append(numero)

        maior_numero = max(lista_numeros)
        menor_numero = min(lista_numeros)
        
        break
    except:
      print("Valor invalido")

print(f"O maior numero é {maior_numero},ja o menor numero é {menor_numero}")
      