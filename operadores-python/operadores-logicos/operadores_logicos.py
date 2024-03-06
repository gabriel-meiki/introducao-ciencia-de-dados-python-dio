saldo = 1000
saque = 250
limite = 200
conta_especial = True

# AND = para ser True, tudo precisa ser True
# OR = para ser True, apenas im tem que ser True
print(True and True)
print(True and False)
print(True or True)
print(True or False)

expressao = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expressao)