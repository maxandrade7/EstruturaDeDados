from random import randint
import time


class Cliente:
    def __init__(self):
        self.nomes = []
        self.horas = []
        
    def IsEMPTY(self):
        return len(self.nomes) == 0

    def ENQUEUE(self, nome, hora):
        self.nomes.append(nome)
        self.horas.append(hora)

    def DEQUEUE(self):
        if (not(self.IsEMPTY())):
            return self.nomes.pop(0)
            return self.horas.pop(0)

    def LENGTH(self):
        return len(self.nomes)

def main(): 
    FilaClientes = Cliente()

    for i in range(1,5):
        FilaClientes.nomes.append("Cliente %d"%(i))
        FilaClientes.horas.append("07:%d5 AM"%(i))

    print("------- Clientes na fila -------")
    print(FilaClientes.nomes, "\n")

    print("------- Hora de chegada na fila -------")
    print(FilaClientes.horas, "\n")


    somaTempo = 0

    for i in range(1,5):
        print("Atendimento do Cliente %d sendo realizado..."%(i))
        print("Atendimento realizado com sucesso!\n")
        intervaloTempo = randint(2, 10)

        tempoInicial = time.time()
        time.sleep(intervaloTempo)
        FilaClientes.DEQUEUE()
        tempoFinal = time.time()

        tempoTotal = tempoFinal-tempoInicial

        somaTempo+=tempoTotal

    mediaTempo = somaTempo/len(FilaClientes.horas)
    print("A media total de atendimento é de %d minutos."%(mediaTempo))

if __name__ == "__main__":
    main()



    
