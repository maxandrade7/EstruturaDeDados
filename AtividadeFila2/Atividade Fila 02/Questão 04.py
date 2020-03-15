from fila import Fila
from random import randint
from time import sleep
import sys

filaBanco = Fila()

def EntrarNaFila(cliente):
    print("Cliente entrando na fila do caixa...")
    filaBanco.ENQUEUE(cliente)

def Atender():
    for i in range(filaBanco.LENGTH()):
        cliente = filaBanco.DEQUEUE()
        
        tempo_Atendimento = randint(1,10)
        print("Cliente sendo atendido...\n")

        sleep(tempo_Atendimento)
        print("Atendimento terminado!\n")
        print("O atendimento demorou %d minutos. "%(tempo_Atendimento))
    
        

def Sair():
    print("Saindo...")
    sys.exit()

def main():  
    print("-------------- BANCO--------------\n")
    print("TECLE: \n", "1- Entrar na fila do caixa de atendimento\n", "2- Atendimento\n","3- Sair.\n")

    comando = int(input("Tecle o número do comando que voce deseja utilizar: \n"))

    
    while comando !=3:
        if comando == 1:
            cliente = input("Informe o nome do cliente: ")
            EntrarNaFila(cliente)
    
        comando = int(input("Tecle o número do comando que quer utilizar: \n"))
        

        if comando == 2:
            Atender()

        elif comando == 3:
            Sair()
            
if __name__ == '__main__':
    main()
