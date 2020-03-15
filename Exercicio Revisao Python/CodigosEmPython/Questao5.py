print("Digite 5 numeros inteiros separados por um espaco: \n")
vetor = input().split()
for i in range(5):
  x = int(vetor[i])

print("")
print("Os elementos do vetor sao: %s"%(vetor))
