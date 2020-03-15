class Fila:
  def __init__(self):
    self.f_elementos = []
  
  def enqueue(self, valor):
    
    if len(self.f_elementos) < 20:
      self.f_elementos.append(valor)
    
    else:
      return ("Quantidade maxima de pacientes atingida.")
  
  def dequeue(self):
    if (not(self.isEmpty())):
      return self.f_elementos.pop()
  
  def isEmpty(self):
    return len(self.f_elementos)==0

  def lenght(self):
    return len(self.f_elementos)
