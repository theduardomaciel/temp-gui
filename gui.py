print("Insira os atributos para realizar o cálculo: ")
F = float(input("Força: "))
D = float(input("Destreza: "))
R = float(input("Resistência: "))
PV = float(input("Pontos de Vida: "))
E = float(input("Energia: "))
M = float(input("Mente: "))
PK = float(input("Pontos de Ki: "))
N = float(input("Nível: "))

# Formato do cálculo: ([F * D * R + PV] + [E * M * PK] * N) * 10
resultado = ((F * D * R + PV) + (E * R * PK) * N) * 10
print("O resultado do cálculo é: ", resultado)
