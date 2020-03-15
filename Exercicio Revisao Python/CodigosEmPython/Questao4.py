print("Informe qual tipo de carne voce deseja comprar:\n")
print("Digite 1 para comprar File Duplo.")
print("Digite 2 para comprar Alcatra.")
print("Digite 3 para comprar Picanha.\n")


compra = int(input("Vou comprar o tipo de carne: "))
peso = float(input("O peso da carne vai ser: "))

tipo_carne = ""

if compra == 1:
  tipo_carne = "File Duplo"

elif compra == 2:
  tipo_carne = "Alcatra"

elif compra == 3:
  tipo_carne = "Picanha"

desconto = 0
compra_feita = 0

pagamento = str(input("Deseja pagar no cartao Tabajara?: "))
print("")
pagamento = pagamento.upper()

file_duplo = 0
alcatra = 0
picanha = 0

if compra == 1 and peso<=5:
  file_duplo = float(int(peso)*4.9)

elif compra == 1 and peso>5:
  file_duplo = float(int(peso)*5.8)

elif compra == 2 and peso<=5:
  alcatra = float(int(peso)*5.9)

elif compra == 3 and peso>5:
  alcatra = float(int(peso)*6.8)

elif compra == 3 and peso<=5:
  picanha = float(int(peso)*6.9)

elif compra == 3 and peso>5:
  picanha = float(int(peso)*7.8)

if file_duplo > 0:
  compra_feita = file_duplo

elif alcatra > 0:
  compra_feita = alcatra

elif picanha > 0:
  compra_feita = picanha


forma_pagamento = " "
if pagamento == "SIM":
  desconto = float(0.05*compra_feita)
  forma_pagamento = "Cartao Tabajara"

else:
  forma_pagamento = "A vista"

print("Informacoes do CUPOM FISCAL: \n")
print("------------------------------------------------")
print("O tipo de carne eh: %s."%(tipo_carne))
print("O quantidade de carne eh: %.2f kg"%(peso))
print("O preco total eh: R$ %.2f"%(compra_feita))
print("A forma de pagamento eh: %s"%(forma_pagamento))
print("O valor do desconto eh: R$ %.2f"%(desconto))
print("O valor total a pagar eh: R$ %.2f\n"%(compra_feita-desconto))

print("Boas compras e volte sempre! ;)")
