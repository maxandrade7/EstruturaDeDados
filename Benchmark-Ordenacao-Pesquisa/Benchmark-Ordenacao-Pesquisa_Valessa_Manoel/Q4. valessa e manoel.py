import time 

import random 

  

# Adicionar as fun��es de Ordenamento e Pesquisa. 

def BubbleSort(lista):
    Comparacoes = 0
    trocas = 0
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            Comparacoes += 1
            if(lista[j] < lista[i]):
                trocas += 1
                Aux = lista[i]
                lista[i] = lista[j]
                lista[j] = Aux
    print("O numero de comparacoes na ordenacao foi: %d"%(Comparacoes))
    print("O numero de trocas na ordenacao foi: %d"%(trocas))

    return lista
    

  
def pesquisaBinaria(lista, item):

    Inicio = 0
    final = len(lista)-1
    posicao = -1
    cont = 0

    while(Inicio<=final):
        meio = (Inicio+final)//2

        if(lista[meio] == item):
            cont += 1
            posicao = meio
            break
        elif(lista[meio] > item):
            cont += 1
            final = meio-1
        else:
            cont += 1
            Inicio = meio+1

    print("O numero de comparacoes na pesquisa foi: %d"%(posicao))

    return posicao




  

# Programa principal 

def main():
    lista = list(range(1, 15000+1))

    print("Tamanho da lista: %d"%(len(lista)))

    inicioOrdenacao = time.time()
    print("Tempo inicial da Ordena��o: %f"%(inicioOrdenacao))  
  
    BubbleSort(lista)  
  
    fimOrdenacao = time.time()  
    print("Tempo final da Orden��o: %f"%(fimOrdenacao))

    tempoTotaldaOrdenacao = fimOrdenacao - inicioOrdenacao  
    print("O tempo total da Ordena��o foi %f"%(tempoTotaldaOrdenacao))  
  
    inicioPesquisa = time.time()  
    print("Tempo inicial da Pesquisa: %f"%(inicioPesquisa))  

    posicao = pesquisaBinaria(lista, 7500)   
    print("Posi��o do item � %d"%(posicao))  

    fimPesquisa = time.time()  
    print("Tempo final da Pesquisa: %f"%(fimPesquisa))  

    tempoTotaldaPesquisa = fimPesquisa - inicioPesquisa 
    print("O tempo total da Pesquisa %f"%(tempoTotaldaPesquisa))  

    inicioOrdenacaoPesquisa = time.time()  
    print("Tempo inicial: %f"%(inicioOrdenacaoPesquisa))  
 
    BubbleSort(lista) 
    posicao = pesquisaBinaria(lista, 7500)

    fimOrdenacaoPesquisa = time.time()  
    print("Tempo final: %f"%(fimOrdenacaoPesquisa))  

    tempoTotal = fimOrdenacaoPesquisa - inicioOrdenacaoPesquisa  
    print("O tempo total foi %f"%(tempoTotal))
  
if (__name__ == "__main__"):
    main()  
