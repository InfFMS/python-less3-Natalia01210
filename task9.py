# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить минимальное и максимальное среди двузначных чисел,
# которые делятся на 3. Если таких чисел не было, вывести "нет".
N = int(input())
if(N == 0):
    print('нет')
    exit()
now = int(input())
mn, mx = now, now
for i in range(N - 1):
    now = int(input())
    if(now % 3 == 0):
        if(mn % 3 == 0):
            mn = min(mn, now)
        else:
            mn = now
        if(mx % 3 == 0):
            mx = max(mx, now)
        else:
            mx = now
if(mn % 3 != 0):
    print("нет")
    exit()
print("Минимальное число:", mn)
print("Максимальное число", mx)
