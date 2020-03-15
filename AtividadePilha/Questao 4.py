def PUSH(lista, valor):
  lista.append(valor)

def POP(lista):
  return lista.pop()

def PEEK(lista):
  return lista[len(lista)-1]

def ISEMPTY(lista):
  if(len(lista) == 0):
    return True

  return False

def LENGTH(lista):
  return len(lista.lista)

def PEEK(lista):
  if not(ISEMPTY(lista)):
      return lista[-1]

def SUM(lista):
  soma = 0

  while(not(ISEMPTY(lista))):
    soma+=PEEK(lista)
    POP(lista)
  
  return soma

lista = [1,2,3,4,5]
print("A soma dos valores da lista eh: %d"%(SUM(lista)))
