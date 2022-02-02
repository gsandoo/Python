# a="my dad's computer\n works at night"

# i = 0

# while(i < 10):
#     i = i + 1
#     print(i)
#     print("한번")
# print("한번")

# # a="my mom's name is \"혜순\""
# print("my dad's computer\n works at night")

# a="life is too short to enjoy"

# print(a[5:])
# a="%10s" % "hi"
# print(a)

# a=("san","kim","han","oh")
# print(a*3)
# dic={'name':'eric','age':15}
# print(dic['name'])

# a={1:'a'}
# a['name']='익명'
# print(a)

# a= {1:'파랑',2:'노랑',3:'은채',4:'초록'}
# for v in a.items():
#     print(v)

# a= {1:'파랑',2:'노랑',3:'은채',4:'초록'}
# print(a.keys())
# print(a.values())
# print(a.items())

# a= {1:'파랑',2:'노랑',3:'은채',4:'초록'}
# for k, v in a.items():
#     print("키는:" + str(k))
#     print("값은:" + v)

# s1=set([1,2,3,4,5])
# print(s1)

# s1=set([1,2,3,4,5,6])
# s2=set([3,4,5,6,7,8])
# print(s1 | s2)

# s1=set([1,2,3,4,5,6])
# s1.add(7)
# print(s1)

# a=[1,2,3]
# b=a
# a[1]=4
# print(id(a))
# print(id(b))

# a=1
# b=2
# if a!=b:
#     print("조응쨩")
# else:
#     print("산아")    

# money=2000
# card=1
# if (money >= 3000) | card:
#     print("응쨍")
# else:
#     print(123) 

# pocket=['iphone','watch']
# if 'iphone' in pocket:
#     pass
# elif 'money' not in pocket:
#     print('주머니에 돈이 없다')
# else:
#     print('주머니에 돈이 있다')

# treeHit=0
# while treeHit<10:
#     treeHit += 1
#     print('나무를 %d 번 찍었습니다' % treeHit)

    
#     if treeHit==10:
#         print('나무가 넘어갔습니다')

# a=0
# b = 0
# while b < 5:
#     while a <10:
#         a = a + 1
#         b = b + 1
#         if (a % 2) == 0:  #if문 실행조건 == 나머지가 0
#             break
#         # print(a)
#         print(b)
    
    # 나머지가 1일때 실행할 코드 아래에 작성

# marks=[90,65,20,45]
# number=0
# for mark in marks:
#     number+=1
#     if mark>=60:
#         print('%d번 학생은 합격입니다' % number )
#     else:
#         print('%d번 학생은 불합격입니다' % number)


# sum=0
# for i in range (1,11):
#     sum=sum + i
# print(sum)

# money = 61

# if money >= 60:
#     print("success")
# else:
#     print("failure")

# print("success") if money >= 60 else print ("failure")
     
# def sum(a,b):
#     result=a+b
#     return result
# print(sum(1,2))

# def sum_many(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
# print(sum_many(1,2,3))

# def hi(name,old,man=True):
#     print("내 이름은 %s 입니다" %name )
#     print("내 나이는 %d 입니다" %old )
#     if man:
#         print("남자입니다")
#     else:
#         print("여자입니다")
# hi("강산아",24)

# a=1
# def lebron(a):
    # a=a+1
# lebron(a)
# print(a)

# def print_kwargs(**kwargs):
#     for k in kwargs.keys():
#         if(k == "name"):
#             print("당신의 이름은:" + k)
# print(print_kwargs(name="int 조수", b="2"))

# sync=(lambda a,b : a+b, lambda a,b : a*b) 
# print(sync[1](1,3))

# for i in range(10):
#  print(i,end="")


# def positive(x):           ---- 많이 쓰이는 외장 함수
#     return x>0

# a=list(filter(positive,[1,2,3,-1,-2]))
# print(a)

# number_1=5
# number_2=number_1
# number_1=number_1+2
# number_2=number_13
# print(number_1)
# print(number_2)

# x=1
# x-=2
# # print(x)

# # print(type(x))

# y = input("입력해주세요")
# print(type(y))

# "" ''                               -------문자열 string
# name='3+2'
# country='호주'
# print("제 이름은 " , name , "입니다. 저는 " + country + "에서 태어났습니다.")

# string1="hello"                   ------------문자열 string
# string2="python"
# string3="***"
# print(string3+string1+string2+string3)

# str1="mountain"                 ---------index 
# print(str1[2])

# fruit="banana"
# fruit2="apple"
# print(fruit+fruit2)

# name = input("name:")                ------input함수
# age = input("age:")
# print(name, age)
# pencil=3000
# pen=4000
# num_pencil=input()
# num_pen=input()



