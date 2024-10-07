# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное и максимальное из введённых чисел.
now = int(input())
if(now == 0):
    print("Нет чисел для анализа.")
    exit()
mn, mx = now, now
while(now != 0):
    if(now > mx):
        mx = now;
    elif(now < mn):
        mn = now
    now = int(input())

print("Минимальное число:", mn)
print("Максимальное число:", mx)
