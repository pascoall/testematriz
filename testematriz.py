#Criar (ler e exibir) uma matriz M 3x3)
M=[ [], [], [] ]
#cada lista interna é uma linha
for i in range(3):
    for j in range(3):
        M[i].append(int(input("Linha (0) Coluna(1)".format(i,j))))
for i in range(3):
    for j in range(3):
        print(M[i][j],end="\t")
    print("")
