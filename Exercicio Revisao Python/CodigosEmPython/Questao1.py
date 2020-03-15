nota1 = int(input("Digite a primeira nota do aluno: "))
nota2 = int(input("Digite a segunda nota do aluno: "))
nota3 = int(input("Digite a terceira nota do aluno: "))

mediaAluno = (nota1+nota2+nota3)/3

if mediaAluno == 10:
  print("Aprovado com Distinção")

elif mediaAluno >= 7:
  print("Aprovado")

else:
  print("Reprovado")
