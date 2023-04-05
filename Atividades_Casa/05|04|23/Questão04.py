letra = str(input("Digite uma letra: ")).upper()
vogais = "AEIOU"
if not letra in vogais:
 print(f"A letra *{letra}* é Consoante")
else:
 print(f"A letra *{letra}* é Vogal")