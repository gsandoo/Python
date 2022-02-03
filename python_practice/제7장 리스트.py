


# 리스트

# 리스트를 만들때는 대괄호로 감싸줌
# 리스트 안에는 어떠한 type도 가능함 .. ex 문자열,정수,실수,empty...
# 리스트는 [] 안에있는 요소들을 변경가능함. str형은 변경 불가.







# name=["a",2,3,4,]
# print(name[2])              -----리스트의 index 기능 출력


# season=['spring','summer','fall','autumn']    -----리스트의 index 기능 출력
# print(season[2])




# name=[1,2,3,4,5]
# numbers=["lee","kim","kang"]
# empty_list=[]                    -----출력

# print(name,numbers,empty_list)




# list_odd=[1,3,5,7,9,11,13,15]
# print(list_odd[0])                     ---- 출력 여러개 (인덱싱 리스트)
# print(list_odd[7])



# list=[5,9,301,714,3776,9614]
# high=5
# low=3
                                    #  ---리스트 연산 가능 단, 나눗셈은 불가
# print(list[high-low])
# print(list[3+2])



# num=[0,10,20,30,40,50,60,70,80,90]
# temp=3

# print(num[temp*3])                     ----예제
# print(num[temp%2])
# print(num[temp+5])


# num=[1,2,3,4,6,12]
# print(1 in num)               ---- in ,not in (1 이 리스트 안에 있는가)
# print(5 not in num)


# list=['lee','park','ha']
# print('lee' in list)
# print("hoong" not in list)

 
# name=["kim su ji"]
# print(len(name[0]))    ---- 첫번째 리스트의 글자 수 구하기!


# num=[301,1,2,567,904]
# if len(num) < 5:
#     print(True)
# elif len(num) <= 5:
#     print(False)      ---if문 활용
# else:
#     print(numnum)



# num=["lee",9,["kim","park"],11,"hong",'gu']   - --- list 안의 list는 하나의 element로 간주한다.
# print(len(num))


# list1=["risk","issue","test","maintenance"]
# list2=["security","plan","design","systematic","safety"]
# list3=["maintenance","verification",'validation','length','math']

# if ("maintenance" in list1) and (len(list1) >=5):
#         print("list1")
# if ("maintenance" in list2) and (len(list2) >=5):
#         print("list2")
# if ("maintenance" in list3) and (len(list3)>=5):
#         print("list3")


# numa=[1,2,3]             -----덧셈
# numb=[4,5,6]
# print(numa+numb)

# numa=[1,2,3]             -----곱셈 (리스트를 n번만큼 곱해준다.)
# numc=numa*3
# print(numc)


# numa=[1,2,3]
# numb=numa[1]*3         ---특정 리스트 인덱싱 넘버를 곱하기
# # print(numb)
# # =6

# numa=[1,2,3,4,5,6,7,8,9,10]
# print(numa[1:5])                  ----리스트의 슬라이싱 기능. 
# print(numa[:])                    ----[:] 는 리스트안에 있는 모든 elements 출력



# numa=[1,2,3,4,5,6,7]
# numa[1:3]=[3,3,3]               ----리스트안에 있는 요소를 슬라이싱으로 교체
# print(numa)


winner=['박민아','정민호','김철수','이영희','손수정']
if "정수지" in winner:
    print("정수지가 수상하였습니다")
else:
    print("정수지가 수상하지 못했습니다")
if "김철수" not in winner:
    print("철수가 수상하지 못했습니다")
else:
    print("철수가 수상하였습니다")

if "박민아" in winner:
    print("박민아가 수상하였습니다")
else:
    print("박민아가 수상하지 못했습니다")


score=['peter=100','john=0','mina=55','tim=75','cony=95']
print(score[3])

spell=['j','e','s','u','s']
spell[2:]=['l','l','y']
print(spell)


num=int(input('0부터 5까지의 숫자를 입력하세요. 운세를 알려드립니다.'))

goodsay=['happy','love','sad','hot','angry','fortunate']


print(goodsay[num])

team=['민지','경희','상구','지민']
if len(team) > 3:
    print("팀원이 많습니다. 줄이세요")

    


