# 순환(recursion) - 함수가 자기 자신을 호출하여 문제를 해결하는 프로그래밍

# 팩토리얼 함수
# 1부터 n까지의 수를 모두 곱하는 함수
def factorial(n):
    if n ==1:
        return 1
    else:
          return n * factorial(n-1)

print(factorial(5))


def factorial(n):
    if n ==1:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("정수입력:"))
print(f"{n}!= {factorial(n)}")



# 피보나치 수열
# 맨 처음 두 항을 0,1로 두고 다음 항은 전 두항의 합으로 채우는 수열.
def fib(n):
    if(n==0):
        return 0 
    elif (n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(8)) 



# 1부터 n 까지 수를 더하는 순환함수를 작성하여 보자.
def add(n):
    if n==1:
        return 1
    else:
        return n+add(n-1) 

print(add(3))