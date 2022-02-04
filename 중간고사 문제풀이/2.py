line = '=' * 20
TestCase = 1

print(line)
print('     Test Case')
print(line)

dec1 = input('2진수 첫 번째 숫자 입력: ')
dec2 = input('2진수 두 번째 숫자 입력: ')
    
    
#2진수 첫 번째 숫자를 10진수로
    
index = 1
num10 = 0
ex = 0    
    
while ex != len(dec1):
    num = len(dec1) - index
    n10 = int(dec1[num]) * (2 ** ex)
        
    num10 += n10
 
    index +=1
    ex += 1

sum = int(num10)

#2진수를 두 번째 숫자를 10진수로
    
index = 1
num11 = 0
ex = 0    
    
while ex != len(dec2):
    num = len(dec2) - index
    n10 = int(dec2[num]) * (2 ** ex)
        
    num11 += n10
 
    index +=1
    ex += 1

sum = int(num10) + int(num11)

#10진수를 2진수로
str1 = ""

if(sum == 0):
    print("0")

while((sum / 2) > 0):
    str1 += str(sum % 2)
    sum = sum // 2

num2 = ""
lenth = len(str1)

while(lenth > 0):
    num2 += str1[lenth - 1]
    lenth -= 1

print('합:', str(num2))
