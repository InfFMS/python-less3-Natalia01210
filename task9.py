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
    if(now % 3 == 0 and now > 9 and now < 100):
        if(mn % 3 == 0 and mn > 9 and mn < 100):
            mn = min(mn, now)
        else:
            mn = now
        if(mx % 3 == 0 and mx > 9 and mx < 100):
            mx = max(mx, now)
        else:
            mx = now

if(mn % 3 != 0 or mn < 10 or mn > 99):
    print("нет")
    exit()
print("Минимальное двузначное число, делящееся на 3:", mn)
print("Максимальное двузначное число, делящееся на 3:", mx)
