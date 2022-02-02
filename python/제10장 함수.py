



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


math=[90,80,70,60,50]
a=len(math)
for i in math:
    b = b + math[i]
b=b/a

# '''
# dasdwasd
# '''

