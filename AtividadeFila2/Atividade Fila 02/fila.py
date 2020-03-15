class Fila:
    def __init__(self):
        self.f_elementos = []
        
    def IsEMPTY(self):
        return len(self.f_elementos) == 0

    def ENQUEUE(self, item):
        self.f_elementos.append(item)

    def DEQUEUE(self):
        if (not(self.IsEMPTY())):
            return self.f_elementos.pop(0)

    def LENGTH(self):
        return len(self.f_elementos)

    def PEEK(self, elemento):
        if (not(self.IsEMPTY())):
            return self.f_elementos[0]
