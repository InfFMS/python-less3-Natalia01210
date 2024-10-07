# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено простых натуральных чисел
# (которые делятся только сами на себя и на 1), и сколько составных.
def F(n):
    if(n < 2):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if(n % i == 0):
            return False
    return True
p, o = 0, 0
now = int(input())
while(now != 0):
    if(F(now)):
        p += 1
    elif(now > 1):
        o += 1
    now = int(input())
print('Простых чисел:', p, 'и Составных чисел:', o)

