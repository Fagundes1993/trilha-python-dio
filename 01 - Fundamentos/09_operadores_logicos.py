# Na condição AND todas as sentenças precisam ser verdadeiras
# Na condição OR basta uma sentença ser verdadeira

print(True and True)
print(True and False)
print(True or True)
print(True or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp_1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp_1)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

saldo_conta_normal = saldo >= saque and saque <= limite
saldo_conta_especial = conta_especial and saldo >= saque

exp_3 = saldo_conta_normal or saldo_conta_especial
print(exp_3)