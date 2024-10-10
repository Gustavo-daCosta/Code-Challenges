N = int(input())

time = [0, 0, 0]

for i in range(0, 2):
    rest = N % 60
    time[i] += (N - rest) / 60

print(time)