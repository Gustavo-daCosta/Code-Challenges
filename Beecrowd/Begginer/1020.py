ageInDays = int(input())

anos, meses, dias = 0, 0, 0

while ageInDays >= 365:
    anos += 1
    ageInDays -= 365

while ageInDays >= 30:
    meses += 1
    ageInDays -= 30

dias = ageInDays

print(f"{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)")