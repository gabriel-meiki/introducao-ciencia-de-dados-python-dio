MAIOR_IDADE = 18
IDADE_ESPECIAL= 12

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Pode tira sua CNH")
else:
    print("Você ainda não pode tirar sua CNH")


if idade >= MAIOR_IDADE:
    print("Pode tira sua CNH")
elif idade >= IDADE_ESPECIAL:
    print("Você pode fazer aulas teóricas, mas não pode fazer aulas práticas")
else:
    print("Você ainda não pode tirar sua CNH")