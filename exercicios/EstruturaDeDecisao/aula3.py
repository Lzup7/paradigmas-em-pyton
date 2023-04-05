nome = str(input("Qual seu nome: "))
print(
  f"-ahhh... que sono... bem acho que é hora de acordar \n (você levanta...) {nome}-...temho q escovar os dentes...   "
)
escolha1 = str(input("Vai escovar os dentes? s/n: ")).upper()
#N_escovar
if escolha1 == "N":
 print(f"-ahh.... depois faço isso")
elif escolha1 == "S":
  print("Vc escova os dentes.")
else:
  print("Escreva direito disgraça!")

  