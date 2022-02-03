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




        



