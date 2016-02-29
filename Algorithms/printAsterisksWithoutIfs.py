num = 1223112
for i in range(0, 6):
    print (num % 10) * '*'
    num = (num - (num % 10)) / 10
