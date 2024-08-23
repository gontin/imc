peso = float(input("Seu peso: "))
altura = float(input("Sua altura: "))

imc = peso / altura

if imc <=18.4:
    print("abaixo do peso")
elif imc <= 25:
    print("peso normal")
elif imc <= 30:
    print("acima do peso")
elif imc <= 35:
    print("obesidade")
elif imc >35:
    print("obesisade acima do segundo grau")
