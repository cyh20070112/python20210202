import random
n = random.randint(1,20)
while  True:
    ans = int(input('number'))
    if n == ans:
        print('答對')
        break
    else:
        print('答錯')