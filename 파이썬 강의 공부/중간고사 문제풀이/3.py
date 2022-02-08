line = '=' * 20
TestCase = 1

while(True):
    print(line)
    print('     Test Case', TestCase)
    print(line)

    N = input('NN 입력 : ')
    M = N[0]

    num = int(M)

    for i in range(0, int(M) + 1, 1):
        print(i, num, '+', num, i, '=', N)
        num -= 1

        if num == -1:
            break
    
    TestCase += 1
