from math import floor

N = int(input()) # número de diretores
K = int(input()) # duração máxima da reunião (em minutos)

tempoSemPausa = K - floor(N / 2)
tempoDeFala = floor(tempoSemPausa / N)

print(tempoDeFala)
