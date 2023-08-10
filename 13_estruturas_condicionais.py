MAIORIDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe a sua idade: "))

#if simples
if idade >= MAIORIDADE:
    print("Maior de idade, pode irar a CNH")

if idade < MAIORIDADE:
    print("Ainda não pode tirar a CNH")

#if else
if idade >= MAIORIDADE:
    print("Maior de idade, pode irar a CNH")
else:
    print("Ainda não pode tirar a CNH")

#elif
if idade >= MAIORIDADE:
    print("Maior de idade, pode tirar a CNH")
elif idade >= 12:
    print("Pode fazer as aula teoricas, mas não pode fazer aulas praticas")

else:
    print("Ainda não pode tirar a CNH")