

# 반복문-하나이상의 문제를 여러번반복하는 구성을 가진문장

# while문 

# 오믈렛 재료가 있을때 "모든재료를 한번 씩" 출력하기.
# 출력할값=ingre
# 모든재료를 한번씩 = index
# 인덱스를 올려줘야 리스트에 있는 재료들을 차례대로 출력할 수 있다.




# omelet=['egg','meat','onion','carrot']
# index=0
# while index<len(omelet):
#     ingre=omelet[index]
#     print(ingre)
#     index=index+1

# while문의 break 사용

# while(True):
#     n=int(input("put a number:"))
#     if n==0:
#         print("EXIT")
#         break
#     elif n%2==0:
#         print(n,"짝수 number")
#     else:
#         print(n,"홀수 number")


# 1부터 n까지 의 합이 1000보다 크다
# n은 위 조건을 만족하는 수 중 가장 작은 값이다.
# sum=0
# n=0  
# while sum < 1000:
#     n+=1
#     sum+=n
# print(n)


# sum=0
# n=0
# while(True):
#     n+=1
#     sum+=n
#     if sum >1000:
#         break
# print(n)



# for문 -보통 range함수랑 많이쓴다. ~~일 때, 그밑에 조건문.

# range범위 내의 variable 각각에 대해서 조건문의 조건을 확인한 후, 
# 조건이 참일 경우 True_statemens를 수행함.


# 구성
# for variable in range(num):   
# if조건:
    #  True_statements


# for i in range(10,20):          
#     if i %2==0:
#         print(i)


# mixlist=['apple',5,'banana',3,8,6,'melon']
# for i in mixlist:
#     if type(i)==str:
#         print(i,"str type\n")
#     else:
#         print(i,'number\n')



