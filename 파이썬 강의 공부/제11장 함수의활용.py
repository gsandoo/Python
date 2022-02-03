#  반복되는 statement를 하나의 코드로 정의하기
def score(scorelist):
    if scorelist>=90:
        grade="A"
    elif scorelist>=80:
        grade="B"
    elif scorelist>=70:
        grade="C"
    else:
        grade='F'
    
    return grade

# 각 과목 점수를 입력 받고 프로그램에 대입시키기
korscore=int(input("국어 점수를 입력하세요:"))
mathscore=int(input("수학 점수를 입력하세요:"))
engscore=int(input("영어 점수를 입력하세요:"))

korgrade=score(korscore)
mathgrade=score(mathscore)
enggrade=score(engscore)

# 출력하기
print("국어 점수는",korgrade,"입니다")
print("수학 점수는",mathgrade,"입니다")
print("영어 점수는",enggrade,"입니다")

# -----------------------------------------------
# 한가지 함수는 한가지 기능만을 포함하는 것을 권장
# -----------------------------------------------

#문제) 길이가 서로 다른 3개의 단어를 입력받아, 가장 길이가 길고 짧은 함수를 찾아라.

def longgest(str1,str2,str3):
    longgest=str1
    if len(longgest)<len(str2):
        longgest=str2 
    if len(longgest)<len(str3):
        longgest=str3
    return longgest

def shortest(str1,str2,str3):
    shortest=str1
    if len(shortest)>len(str2):
        shortest=str2
    if len(shortest)>len(str3):
        shortest=str3
    return shortest

print(longgest("one","second","three"))
print(shortest("one","second","three"))



