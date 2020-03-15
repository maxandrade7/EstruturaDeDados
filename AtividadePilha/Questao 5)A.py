def ValoresEmpilhados(lista):
  empilhados = []
  for valor in lista:
    if valor%3==0:
      empilhados.append(valor)

  print("valores empilhados", end = ": ")
  return empilhados

lista = list(range(1,17))

print(ValoresEmpilhados(lista))
