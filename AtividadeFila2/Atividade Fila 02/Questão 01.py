from pilha import Pilha
from fila import Fila

pilha= Pilha()
fila = Fila()

lista = ['N', 'O', 'H', 'T', 'Y', 'P']
for item in lista:
    pilha.push(item)

for i in range(pilha.length()):
    letra= pilha.pop()
    fila.ENQUEUE(letra)
    

lista_reversa = []

for i in range(fila.LENGTH()):
    letra2 = fila.DEQUEUE()
    lista_reversa.append(letra2)

print(lista_reversa)
