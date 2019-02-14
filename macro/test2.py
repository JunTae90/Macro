



a0 = 0
a1 = 0


while True:
    b = 0
    for i in range(2):
        if globals()['a{}'.format(i)]:
            print(globals()['a{}'.format(i)])
            b = b + globals()['a{}'.format(i)]
    print(b)
    if b == 0:
        break




print(a0+a1+3)

