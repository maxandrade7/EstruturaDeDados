class Fila:
  def __init__(self):
    self.fila_atendimento = []
  
  def EhVazia(self):
    return len(self.fila_atendimento)==0
  
  def Tamanho(self):
    return len(self.fila_atendimento)

  def Agendamento(self, paciente):
    if (self.Tamanho()) < 20:
      self.fila_atendimento.append(paciente)
      return "Agendamento realizado com sucesso!"
    
    else:
      return "Capacidade máxima de agendamentos atingida."

  def Atendimento(self):
    if (not(self.EhVazia())):
      return self.fila_atendimento.pop(0) , "Atendimento realizado."

F = Fila()
for i in range(1,20+1):
  F.Agendamento("Paciente %d"%(i))

print(F.Agendamento("Paciente 21"))
print("")
print(F.Atendimento())
