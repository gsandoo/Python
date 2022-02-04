line = '=' * 20
TestCase = 1

menu = {'Americano':'2,000원', 'Cafe latte':'2,500원', 'Green Tea latte':'3,000원', 'Mocha latte':'3,500원'}

while(True):
    print(line)
    print('     Test Case: ' + str(TestCase))
    print(line)
    
    Menu = input('Menu: ')
    if Menu == 'Americano':
        print('Pirce:' + menu['Americano'])
        TestCase += 1
    elif Menu == 'Cafe latte':
        print('Pirce:' + menu['Cafe latte'])
        TestCase += 1
    elif Menu == 'Green Tea latte':
        print('Pirce:' + menu['Green Tea latte'])
        TestCase += 1
    elif Menu == 'Mocha latte':
        print('Pirce:' + menu['Mocha latte'])
        TestCase += 1
    else:
        break
