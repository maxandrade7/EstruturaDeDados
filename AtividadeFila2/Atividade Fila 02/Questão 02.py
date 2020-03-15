from fila import Fila
from random import randint
from time import sleep
import sys

filaImpressao = Fila()

def adicionarFilaImpressao(documento):
    print("Adicionando documento a fila de impressao, aguarde...")
    filaImpressao.ENQUEUE(documento)

def imprimir():
    for i in range(filaImpressao.LENGTH()):
        documento = filaImpressao.DEQUEUE()
        
        tempo_impressao = randint(1,10)
        print("Imprimindo...\n")

        sleep(tempo_impressao)
        print("Documento impresso!\n")
        print("A impressão levou: %ds"%(tempo_impressao))
    
        

def sair():
    print("Saindo...")
    sys.exit()

def main():  
    print("-------------- IMPRESSORA--------------\n")
    print("TECLE: \n", "1- Adicionar documento na fila de impressão\n", "2- Imprimir\n","3- Sair.\n")

    comando = int(input("Tecle o número do comando que quer utilizar: \n"))

    
    while comando !=3:
        if comando == 1:
            documento = input("Digite o nome do documento: ")
            adicionarFilaImpressao(documento)
    
        comando = int(input("Tecle o número do comando que quer utilizar: \n"))
        

        if comando == 2:
            imprimir()

        elif comando == 3:
            sair()
            
if __name__ == '__main__':
    main()
