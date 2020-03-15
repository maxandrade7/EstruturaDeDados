class Fila:
  def __init__(self):
    self.fila_avioes = []

  def Enfileirar(self,valor):
    self.fila_avioes.append(valor)
    
  def EhVazia(self):
    return len(self.fila_avioes)==0
  
  def Decolar(self):
    if(not(self.EhVazia())):
      self.fila_avioes.pop(0)
      
  def Tamanho(self):
    return len(self.fila_avioes)

avioes = Fila()

modelos_disponiveis = ["Boeing 747 - 2012", "Airbus A320 - 2009", "Renegade - 2013", "TL 2000 - 2014"]

print("Lista dos modelos:\n")
for i in range(len(modelos_disponiveis)):
  print ("%s"%((modelos_disponiveis[i])))

print("")

for i in range(3):
  aviaoX = str(input("Informe o modelo do avião: "))
  avioes.Enfileirar(aviaoX)

print("a) O número de aviões na fila de decolagem é: %d\n"%(avioes.Tamanho()))
print("b) Autorizando o primeiro avião da fila a decolar...\n")
avioes.Decolar()
print("c) Adicionando um avião à fila de espera...\n")
avioes.Enfileirar("F22 - 2010")
print("d) Listando todos os avioes na fila de espera...\n")
for i in range(avioes.Tamanho()):
  print(avioes.fila_avioes[i])
print("e) Caracteristcas do primeiro avião da fila: ")
print(avioes.fila_avioes[0])
