lista_numeros = list()
for n in range(0,3):
  while True:
    try:
        n = int(input(f"Digite o numero {n+1}: "))
        lista_numeros.append(n)
        break
    except:
      print("Valor invalido")
lista_numeros.sort(reverse = True)
print(lista_numeros)