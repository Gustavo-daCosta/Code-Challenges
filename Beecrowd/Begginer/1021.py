N = float(input())

notas = { 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, }
moedas = { 1: 0, 0.50: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0 }

dinheiro = [notas, moedas]

for tipoDinheiro in dinheiro:
    for key in tipoDinheiro.keys():
        tempValue = 0
        while N >= key:
            N -= key
            tempValue += 1
        tipoDinheiro[key] = tempValue

print("NOTAS:")
for key, value in notas.items():
    print(f"{value} nota(s) de R$ {key:.2f}")
print("MOEDAS:")
for key, value in moedas.items():
    print(f"{value} moeda(s) de R$ {key:.2f}")
