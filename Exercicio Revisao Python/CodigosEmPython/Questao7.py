impares = []
pares = []

for i in range(1,11):
  impar=  int(input("Digite um valor impar X[%d]: "%(i)))
  print("")
  par=  int(input("Digite um valor par X[%d]: "%(i)))
  print("")

  impares.append(impar)
  pares.append(par)

vetor_unido = []

for i in range(10):
  a = impares[i]
  b = pares[i]

  vetor_unido.append(a)
  vetor_unido.append(b)

print (vetor_unido)
