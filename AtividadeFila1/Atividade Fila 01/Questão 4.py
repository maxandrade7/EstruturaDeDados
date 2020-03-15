class LINK:
  def __init__(self):
    self.sites = ["Google", "Youtube", "UOL", "Instagram"]
    
  def Pegar(self, sites):
    return self.sites[sites]
  
  def Tamanho(self):
    return (len(self.sites))

pesquisa = ()
links = LINK()
print("Lista dos Sites:\n")
for i in range(0, links.Tamanho()):
  print ("%s"%((links.Pegar(i))))

print("")
pesquisa = str(input("Digite o nome do site correspondente ao qual você deseja obter o link: "))

if pesquisa in links.sites:
      if pesquisa in links.sites[0]:
        site = ("\nwww.%s.com.br"%((pesquisa)))
      print (pesquisa)
      if pesquisa in links.sites != [0]:
        links.sites.insert(0,pesquisa)
        links.sites.reverse()
        links.sites.remove(pesquisa)
        links.sites.reverse()
        pesquisa = ("www.%s.com.br"%((pesquisa)))
        print ("\nO link do respectivo site pesquisado eh: ", pesquisa.lower())

else:
  print ("\n O site que você pesquisou não foi encontrado ou foi digitado incorretamente.")
