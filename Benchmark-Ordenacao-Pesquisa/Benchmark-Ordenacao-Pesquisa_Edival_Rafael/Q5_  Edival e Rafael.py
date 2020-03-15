import time 

import random 

  

# Adicionar as fun��es de Ordenamento e Pesquisa. 


def MergeSort(lista):

    if len(lista) > 1:

        meio = len(lista)//2

        listaDaEsquerda= lista[:meio]
        listaDaDireita = lista[meio:]

        MergeSort(listaDaEsquerda)
        MergeSort(listaDaDireita)

        i = 0
        j = 0
        k = 0

        while i < len(listaDaEsquerda) and j < len(listaDaDireita):

            if listaDaEsquerda[i] < listaDaDireita[j]:
                lista[k]=listaDaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDaDireita[j]
                j += 1
            k += 1

        while i < len(listaDaEsquerda):

            lista[k]=listaDaEsquerda[i]
            i += 1
            k += 1

        while j < len(listaDaDireita):
            lista[k]=listaDaDireita[j]
            j += 1
            k += 1

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

    print("Tamanho da lista: %d"%(len(lista)))

    inicioOrdenacao = time.time()
    print("Tempo inicial da Ordena��o: %f"%(inicioOrdenacao))

    MergeSort(lista)

  
    fimOrdenacao = time.time()  
    print("Tempo final da Orden��o: %f"%(fimOrdenacao))

    tempoTotaldaOrdenacao = fimOrdenacao - inicioOrdenacao
    
    print("O tempo total da Ordena��o foi %f"%(tempoTotaldaOrdenacao))  
  
    inicioPesquisa = time.time()  
    print("Tempo inicial da Pesquisa: %f"%(inicioPesquisa))  

    posicao = pesquisaLinear(lista, 7500)   
    print("Posi��o do item � %d"%(posicao))  

    fimPesquisa = time.time()  
    print("Tempo final da Pesquisa: %f"%(fimPesquisa))  

    tempoTotaldaPesquisa = fimPesquisa - inicioPesquisa 
    print("O tempo total da Pesquisa %f"%(tempoTotaldaPesquisa))  

    inicioOrdenacaoPesquisa = time.time()  
    print("Tempo inicial: %f"%(inicioOrdenacaoPesquisa))

    MergeSort(lista)

        
    

    fimOrdenacaoPesquisa = time.time()  
    print("Tempo final: %f"%(fimOrdenacaoPesquisa))  

    tempoTotal = fimOrdenacaoPesquisa - inicioOrdenacaoPesquisa  
    print("O tempo total foi %f"%(tempoTotal))
  
if (__name__ == "__main__"):
    main()  


