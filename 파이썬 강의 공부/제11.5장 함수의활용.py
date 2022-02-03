# 3가지 단어로 구성딘 wordlist
# 단어들의 길이릐 합을 나타내는 프로그램 작성.

def len_word(list):
    result=0
    for i in list:
        result+=len(i)
    return result

fruit=["apple","banana","tomato"]
animal=["lion","monkey","elephant"]
instrument=["guitar",'piano','hamonica']

fruit_length=len_word(fruit)
animal_length=len_word(animal)
ins_length=len_word(instrument)

print(f"과일 단어의 총 길이는 {fruit_length}입니다")
print(f"동물 단어의 총 길이는 {animal_length}입니다")
print(f"악기 단어의 총 길이는 {ins_length}입니다")

# 5개의 정수로 이루어진 numlist를 인자로 받아
# 평균이 60점 이상이면 Pass, 아니면 Fail 을 출력해주는 프로그램 작성

def num(numlist):
    result=0
    for i in numlist:
        result+=i
    if result / 6 >= 60:
        print(f"이 학생은 Pass 입니다.")
    else:
        print(f"이 학생은 Fail 입니다.")
         
passFail=[30,40,50,60,70,80]
num(passFail)

# 여러 개의 점수가 list로 주어졌을 때, 가장 높은 점수를 구하는 함수를
# 만들어보자. 프로그램 상세 요구사항은:
# 1. 점수들로 이루어진 list
# 2. 점수들 중 가장 높은 점수가 출력된다.

def biggest(list):
    big_number=0
    for i in list:
        if i > big_number:
            big_number=i
        else:
            big_number=big_number
    return big_number

math_score=[45,66,70,83,50,77,87,92,73,89]
max_score=biggest(math_score)
print(f"수학 점수 중 가장 큰 점수는 {max_score} 입니다.")



# 섭씨 온도를 입력으로 받아서 회씨온도로 변환하는 함수를 작성해보자.

def degree(sub_degree):
    f_degree=((9/5)*sub_degree+32)
    return f_degree

s_degree=int(input("섭씨온도 입력:"))
result=degree(s_degree)
print(f"섭씨 온도{s_degree}를 화씨 온도로 변환한 값은 {result}입니다.")


# meter를 입력받아 yard와 feet로 변환하여 출력하는 함수를 작성해보자.

def feet(meter):
    change_feet=meter/0.305
    return change_feet

def yard(meter):
    change_yard=meter*1.0936
    return change_yard

write_meter=int(input("meter 입력:"))
result_feet=feet(write_meter)
result_yard=yard(write_meter)

print(f"{write_meter}는 {result_yard} yard, {result_feet} feet 입니다.")



# 삼긱형의 밑변과 높이를 입력받아, 삼각형의 면적을 출력하는 프로그램을 작성해보자.
# 사용자가 밑변, 높이 를 입력한다. 입력받는 숫자는 정수(int)형이다.

def triangle(bottom,height):
    area=float(0.5*bottom*height)
    return area

bottom=int(input("밑변 입력:"))
height=int(input("높이 입력:"))

total_area=triangle(bottom,height)
print(f"삼각형의 밑변{bottom}cm 와 높이 {height}cm 를 입력받아 민든 삼각형의 면적은 {total_area}cm 입니다.")


# 초를 입력하면 몇 시, 몇 분, 몇 초인지를 출력하는 함수를 작성해보자.'
# 사용자가 입력받은 시간은 하루 내의 시간이어야 한다.

def hour(second):
    hours=second/3600
    return hours
    
def minute(second):
    hours=second%3600
    minutes=hours/60
    return minutes

def seconds(second):
    hours=second%3600
    secondleft=hours%60
    return secondleft

second=int(input("초 입력:"))
tot_hour=int(hour(second))
tot_min=int(minute(second))
tot_sec=int(seconds(second))
print(f"{second}초를 전체적인 시간으로 반환한 결과는 {tot_hour}시 {tot_min}분 {tot_sec}초 입니다.")


# 소비자가격을 입력받아 10프로의 부가가치세를 출력하고 , 제품가격을 출력해보자.

def tax(total_price):
    tax=total_price/10
    return tax

def product_price(total_price):
    product_price=total_price-tax
    return product_price

total_price=int(input("소비자가 입력:"))
tax=int(tax(total_price))
product_price=int(product_price(total_price))
print(f"제품가격은 {product_price})원, 부가가치세는 {tax}입니다.")






        



