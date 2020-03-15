def PUSH(lista, valor):

  if len(lista)<7:
    lista.append(valor)
  else:
    return ("Quantidade maxima de elementos atingida")

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

lista = [1,2,3,4,5,6,7]
print(PUSH(lista,8))
print(lista)
