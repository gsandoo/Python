



# 함수의 정의

# def 함수이름(n1,n2...)
    # statements
    # return ResultValue

# 함수 이름- 함수가 수행하는 작업을 요약하는 단어로 이름을 정의
            # - 맨처음 단어는 문자로 작성
            # -문자,숫자,언더바 만사용
            # -키워드에 있는 이름은 사용 불가능 if,while,def 등

# 인자      -여러개 가능, 없을 수도있음
#           -없으면 괄호로만 놔둠

# return문  - 결과값을 변환해주는 문장
            # -수행 시 함수가 종료됨
            # -반드시 있을필요는 없다


def ken(x):
    result=(x*x)+x+1
    return result
a=ken(5)

print (a)


# def square(w,l,h):
#     result=w*l*h
#     return result

# vol=square(4,4,5)
# print(vol)


# num=int(input("숫자 1입력:"))
# def big_three(num): 
#     result=num+3
#     return result

# num_three=big_three(1)
# print(num_three)


# math=[90,80,70,60,50]
# a=len(math)
# for i in math:
#     b = b + math[i]
# b=b/a


# 숫자를 입력받아 , 숫자에 3을 더하는 문제
# def number(increase3):
#     result=increase3+3
#     return result

# num=5

# answer=number(num)
# print(answer)



# 숫자들을 입력받아 평균값을 구하는 식 만들기


def number(numbers):
    result=0
    for i in numbers:
        result=result+i
    return result

numlist=(50,40,30,20,10)
lennum=len(numlist)
answer=number(numlist)/lennum
print(int(answer))


# 두 수를 입력받아 차 구하는 식

def num(num1,num2):
    result=num1-num2
    return result

answer=num(33,2)
print(answer)
# ---------------------------------------------------------------------

# 양의 정수 n을 입력하면 1부터 n까지 곱해주는 fact함수를 작성하시오

def fact(n):
    one=1
    for i in range(1,n+1):
        one=one*i
    return one

t_fact=fact(10)
print(t_fact)

# -------------------------------------------------------------

# 점수를 받아 홀수인지 짝수인지를 출력하는 함수를 return문없이 정의하기

def oddoreven(num):
    if num%2==0:
        print("even")
    else:
        print("odd")

oddoreven(3)

# -----------------------------------------

# 인자가 존재하지 않는 함수
def hello():
    return "hello , how are you?"

greeting=hello()
print(greeting)





 




