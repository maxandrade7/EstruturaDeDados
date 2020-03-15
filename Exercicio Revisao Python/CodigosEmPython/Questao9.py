lista_veiculos = []

lista_consumo = []

litros_10km = []

consumo10km = 0

lista_precos = []

precoGasolina = 0

for i in range(1,6):
  veiculoX = str(input("Informe o veiculo %d: "%(i)))
  consumoX = float(input("Informe o consumo do veiculo %d: "%(i)))
  print("")

  lista_veiculos.append(veiculoX)
  lista_consumo.append(consumoX)

  consumo10km = float(1000/consumoX)
  litros_10km.append(consumo10km)

  precoGasolina = float(consumo10km*3.5)
  lista_precos.append(precoGasolina)


print("Relatorio Final:\n")
print("Modelo        KM/L         1000KM         PRECO")
for i in range(5):
  print("%s ------ %.1f ------ %.1f litros ----- R$ %.2f" %(lista_veiculos[i], lista_consumo[i], litros_10km[i], lista_precos[i]))

print("")

menorConsumo = min(litros_10km)

consumoCarro = 0

melhorConsumo = 0

for j in range(len(litros_10km)):
  consumoCarro = litros_10km[i] 

  if consumoCarro == menorConsumo:
    melhorConsumo = i

print("O menor consumo é do %s"%(lista_veiculos[melhorConsumo]))
