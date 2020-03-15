class Fila:
  def __init__(self):
    self.f_elementos = []
  
  def enqueue(self, valor):
    self.f_elementos.append(valor)
  
  def dequeue(self):
    if (not(self.isEmpty())):
      return self.f_elementos.pop()
  
  def isEmpty(self):
    return len(self.f_elementos)==0

  def lenght(self):
    return len(self.f_elementos)
