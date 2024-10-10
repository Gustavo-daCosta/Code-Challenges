N = int(input())

possibleNotes = [100, 50, 20, 10, 5, 2, 1]
bankNotes = [0, 0, 0, 0, 0, 0, 0]

NCopy = N
for i in range(len(bankNotes)):
    noteValid = True
    while noteValid:
        noteValid = NCopy >= possibleNotes[i]
        if noteValid:
            NCopy -= possibleNotes[i]
            bankNotes[i] += 1

print(N)
for i in range(len(bankNotes)):
    print(f"{bankNotes[i]} nota(s) de R$ {possibleNotes[i]},00")
