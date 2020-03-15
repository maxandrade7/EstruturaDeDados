def PUSH(lista, valor):
  for i in range(len(lista)):
    if lista[i] == valor:
      print("Insira outro valor, esse ja existe na pilha")
  lista.append(valor)

def POP(lista):
  if (not(ISEMPTY())):
    return lista.pop()

def ISEMPTY(lista):
  return len(lista)==0

def LENGTH(lista):
  return len(lista.lista)

def PEEK(lista):
  if (not(lista.ISEMPTY())):
      return lista[-1]

lista = [6,8]
print(PUSH(lista, 6))
