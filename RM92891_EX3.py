print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
numero_alunos = 50
total_notas_pares = 0
for Numero_chamada in range(2, numero_alunos + 1, 2):
    nota_par = input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}. Nota:".format(Numero_chamada))
    total_notas_pares = total_notas_pares + int(nota_par)
    print("Soma das notas dos alunos pares: {}".format(total_notas_pares))
média_par = total_notas_pares / Numero_chamada
print("A média de nota dos alunos pares é {}".format(média_par))

print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
numero_alunos = 50
total_notas_Inpares = 0
for Numero_chamada in range(1, numero_alunos + 1, 2):
    nota_impar = input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}. Nota:".format(Numero_chamada))
    total_notas_Inpares = total_notas_Inpares + int(nota_impar)
    print("Soma das notas dos alunos Ímpares: {}".format(total_notas_Inpares))
média_ímpar = total_notas_Inpares / Numero_chamada
print("A média de nota dos alunos ímpares é {}".format(média_ímpar))

if média_ímpar > média_par:
    print("A média dos alunos ímpares é maior que dos alunos par, por {} a {}".format(média_ímpar, média_par))

elif média_par > média_ímpar:
    print("A média dos alunos pares é maior que dos alunos ímpares, por {} a {}".format(média_par, média_ímpar))
