# Usando Input
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

# Usando Input + Print
print(nome, idade)

# Usando Print + Argumento end
print(nome, idade, end="...\n") # \n quebra a linha

# Usando Print + Argumento sep
print(nome, idade, sep=" $ ")

# Usando Print + Argumento sep e end
print(nome, idade, sep="#", end="@")
