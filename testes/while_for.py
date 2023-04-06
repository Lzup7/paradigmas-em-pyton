numero_user = int(input("Informe um número para calcular sua\n respectiva tabuada de multiplicação:"))
#loop com for variavel de execução in range( especifique aqui o range rsrs)
for contador in range(1, 11):
  mult = int(numero_user * contador)
  print(f"{numero_user} X {contador} = {mult}")

print("\n")
#loop com while, precisa que você controle a execução
contador = 1
while contador <= 10:
  mult = int(numero_user * contador)
  print(f"{numero_user} X {contador} = {mult}")
  #incrementado o meu contador, para poder parar o fluxo de repetição
  #contador = contador + 1 isso é a mesma coisa do que o que está abaixo:
  contador += 1
