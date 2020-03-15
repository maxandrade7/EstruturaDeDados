class Fila:
  def __init__(self):
    self.listaElementos = []

  def ENQUEUE(self, item):
    self.listaElementos.append(item)

  def ISEMPTY(self):
    return len(self.listaElementos)==0

  def DEQUEUE(self):
    if self.ISEMPTY():
      return False
    return self.listaElementos.pop(0)

  def PEEK(self):
    tamanho = len(self.listaElementos)
    return self.listaElementos[0]

  def LENGTH(self):
    return len(self.listaElementos)

F= Fila()

palavra = "Python"
for item in palavra:
  F.ENQUEUE(item)
print(F.listaElementos)
