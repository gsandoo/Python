
# ---- 1부터 999까지 숫자중에서 4와 6의 배수를 구해서 더하시오.
#범위 1~999
#4와 6의 배수
#더하는것

# result=0                                일단 4와 6의배수를 더하기위해 변수하나 생성.
# for i in range(1,1000):                 i 함수 의 범위 생성
#     if i%4==0 or i%6==0:                i가 4랑 6으로 나누었을 때 나머지가 0, 즉 배수일 때
#         result+=i                       변수result 와 i를 더해줘라 

# print(result)



# result=0                           ------- 1000이하 수중에 3과5의 배수를 더한 값 구하기
# for i in range(1,1000):
#     if i %3 ==0 or i %5==0:
#        result+=i
# print(result)




# def Gugu(n):                           ---------구구단 공식
    
#     result=[]
#     i=1
#     while i <10:
#         result.append(n*i)
#         i=i+1
#     return result
# print (Gugu(2))
