class Pilha:
  def __init__(self):
    self.lista = []
  
  def PUSH(self, valor):
    self.lista.append(valor)
  
  def POP(self):
    if (not(self.ISEMPTY())):
      return self.lista.pop()
  
  def ISEMPTY(self):
    return len(self.lista)==0

  def LENGTH(self):
    return len(self.lista)
  
  def PEEK(self):
    if (not(self.ISEMPTY())):
      return self.lista[-1]
