while True:
    numero = int(input("Informe um numero: "))

    if numero == 10:
        break
        
    print(numero)

#Exibição de numeros impares com o continue
for numero in range(100):
    if numero % 2 == 0:
        continue
    print(numero, end=" ")