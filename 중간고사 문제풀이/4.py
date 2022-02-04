line = '=' * 20
TestCase = 1

while(True):
    print(line)
    print('     Test Case', TestCase)
    print(line)

    N = input('NNN 입력 : ')
    M = N[0]

    num = int(M) - 1

    for i in range(0, int(M), 1):
        print(i, i+1, i+2, '+', i+1, num, i, '+', num, i, i+1, '=', N)
        num -= 1

        if num == 0:
            break
    
    TestCase += 1
