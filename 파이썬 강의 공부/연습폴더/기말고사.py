# a의b승 을 계산하는 순환함수 exp(a,b) 작성하기

def exp(a,b):
    if b==1:
        return a
    else:
        return a*exp(a,b-1)

a=int(input("밑수 입력"))
b=int(input("지수 입력"))
print(f"{a}의 {b}승은 {exp(a,b)}입니다.")


# 2진수를 10진수로 변환해서 반환하는 순환함수 작성
