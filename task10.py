# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".
def F(n):
    if(n == 1):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if(n % i == 0):
            return False
    return True

N = int(input())
if(N == 0):
    print("нет")
    exit()
now = int(input())
mx, mn = now, now
for i in range(N - 1):
    now = int(input())
    if(F(now)):
        if(F(mn)):
            mn = min(mn, now)
            mx = max(mx, now)
        else:
            mn = now
            mx = now
if(not F(mn)):
    print("нет")
    exit()
print("Минимальное простое число:", mn)
print("Максимальное простое число:", mx)


