ticket = input("введите билет: ")

length = len(ticket)
half = length // 2

sum1 = 0
sum2 = 0

i = 0
while i < half:
    sum1 = sum1 + int(ticket[i])
    i = i + 1

i = half
while i < length:
    sum2 = sum2 + int(ticket[i])
    i = i + 1

if sum1 == sum2:
    print(True)
else:
    print(False)