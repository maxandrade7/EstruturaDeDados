import time 

import random 

  

# Adicionar as fun��es de Ordenamento e Pesquisa. 

def BubbleSort(lista):
    trocas = 0
    if len(lista) <= 1:
        Vl = lista
    else:
        for j in range(0,len(lista)):
            for i in range(0,len(lista)-1):
                if lista[i]>lista[i+1]:
                    trocas = trocas + 1
                    Aux = lista[i+1]
                    lista[i+1] = lista[i]
                    lista[i] = Aux
        Vl = lista
    print("A quantidade de trocas foi: %d"%(trocas))
    return Vl

  
def pesquisaLinear(lista, elemento_desejado):
    posicao = 0
    cont = 0
    for item in lista:
        cont = cont + 1
        if(item == elemento_desejado):
            print("A quantidade de compara��es da pesquisa foi: %d"%(cont))
            return posicao
        posicao = posicao + 1

    return -1



  

# Programa principal 

def main():
    lista = list(range(1, 15000+1))
    random.shuffle(lista)
    print("Tamanho da lista: %d"%(len(lista)))

    inicioOrdenacao = time.time()
     
  
    BubbleSort(lista)  
  
    fimOrdenacao = time.time()  
    

    tempoTotaldaOrdenacao = fimOrdenacao - inicioOrdenacao  
    print("O tempo total da Ordena��o foi %f"%(tempoTotaldaOrdenacao))  
  
    inicioPesquisa = time.time()  
      

    posicao = pesquisaLinear(lista, 7500)  
    print("Posi��o do item � %d"%(posicao))  

    fimPesquisa = time.time()  
      

    tempoTotaldaPesquisa = fimPesquisa - inicioPesquisa 
    print("O tempo total da Pesquisa %f"%(tempoTotaldaPesquisa))  

    tempoTotal = tempoTotaldaOrdenacao + tempoTotaldaPesquisa
    print("O tempo total do codigo foi: %f"%(tempoTotal))

    print("A quantidade de compara��es da ordena��o foi: %d"%(len(lista)**2))
  
if (__name__ == "__main__"):
    main()
