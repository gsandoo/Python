

# 제6장 5주차

# if 조건문은 참/거짓 판별에 쓰이는 조건문이다.






# age=int(input("당신의 나이는 몇살입니까?"))

# if age > 20:
#     print("20살이상입니다.")
# else:
#     print("청소년입니다.")

# a="tommorrow"
# if a=="tommorrow":
#     print("yes")

# height=150
# age=19
# if height > 140 and age < 19:
#     print("탑승 가능")
# else:
#     print("탑승 불가능")

# g=int(input("구매 할 포도의 갯수는?"))
# apple=1000
# grape=3000
# bae=2000
# gyul=500
# g=grape*g
# if g >=3:
#     sum=(apple+g+bae+gyul)*(0.9)
#     sum=int(sum)
#     print(sum)

# math=90
# eng=70
# sci=50

# if (math >=60 and eng >= 60 and sci >=60) or (math+eng+sci)/3 >=70:
#     print("합격입니다.")
# else:
#     print("불합격입니다.")



# eng=80
# math=70
# if eng >=80:
#     if math>=80:
#         print("두 과목 다 합격입니다.")                  -----------중첩 조건문..---
#     else:
#         print("수학 점수가 낮아 불합격입니다.")
# else:
#     print("영어 점수가 낮아 불합격입니다.")




# eng=80
# math=70
# if math >=80:
#     print("수학 ㅅㅌㅊ")
# else:                                                  -----------중첩 조건문----
#     if eng>=80:
#         print("수학이 헬입니다. 그러므로 불합")                  
#     else:
#         print("그냥 둘다 불합")



# id=input("id를 입력해 주세요.")
# password=input("비밀번호를 입력해 주세요.")

# if len(id) >10:
#     print('회원가입 실패:id 길이 10을 초과')              -------중첩조건문 심화문제(1)
# else:
#     if len(password) >10:
#         print("회원가입 실패: password 길이 10을 초과")
#     else:
#         print("회원가입 성공.")




# org_id="abc"
# org_pass=123
# id=input("아이디를 입력해주세요.")
# password=input("비밀번호를 입력해주세요.")
# password=int(password)
# n="오류입니다."
# if org_id != id:                                         -------심화문제(2)
#     print(n)
# else:
#     if org_pass !=  password:
#         print(n)
#     else:
#         print("로그인 성공.")



# plus_num=input(" 숫자를 입력해주세요.")
# minus_num=input(" 숫자를 입력해주세요.")

# plus_num=int(plus_num)
# minus_num=int(minus_num)

# if plus_num > 0:
#     if minus_num >0:
#         print("양수입니다.")                 - --- - -- - 심화문제 (3)
#     else:
#         print("음수입니다.")

# else:
#     if minus_num > 0 :
#        print("음수입니다.")
#     else:
#         print("양수입니다.")


# math=90
# if math ==89:
#     print("y")
# elif math ==88:
#     print("y")            ---elif는 조건문이 거짓일 때 else 여러개 쓰기위함.
# elif math == 90:
#     print("yes")


# score=input("성적 입력란")
# score=int(score)
# if score >=90:
#     print("A학점")
# elif score >=80:                     ----문제1
#     print("B학점")
# elif score >= 70:
#     print("C학점")
# else:
#     print("F")



# age=input("나이")
# age=int(age)
# if age >=20:
#     print("성인")
# elif age >= 10 and age < 20 :          ----문제2
#     print("청소년")
# else:
#     print("유아")


# age=int(input("나이"))
# if age >=20:
#     print("성인")
# else:                                   ---문제2 변형
#     if age >=10:
#         print("청소년")
#     else:
#         print("유아")


# channel=int(input("숫자를 입력해주세요"))

# if channel ==5:
#     print("sbs")
# elif channel ==7:
#     print("kbs")
# elif channel ==11:
#     print("mbc")
# else:
#     print("채널 다시 입력")


# num=int(input("손가락 마디 적어"))

# if num >51 and num <=52:
#     print("9호")
# elif num  > 52 and num <=53:
#     print("10호")
# elif num > 53 and num <=54:
#     print("11호")
# elif num <= 51 or num > 55:
#     print("반지 제작 불가능")
# else:
#     print ("반지 제작 불가능")








