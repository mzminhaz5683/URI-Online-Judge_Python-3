list = input().split(" ")
N1, N2, N3, N4 = round(float(list[0]), 1), round(float(list[1]), 1), round(float(list[2]), 1), round(float(list[3]), 1)

#average with weights 2, 3, 4 e 1 respectively
avarage = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10
print("Media: {0}".format(round(avarage, 1)))

if (avarage >= 7.0):
    print("Aluno aprovado.")

elif (5.0 <= avarage <= 6.9):
    print("Aluno em exame.")
    s = float(input())
    print("Nota do exame: {0}".format(round(s, 1)))
    avarage = (avarage + s) / 2

    if (avarage >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado")

    print("Media final: {0}".format(round(avarage, 1)))

elif (avarage < 5.0):
    print("Aluno reprovado.")