



# tuple - 변경 불가능한 리스트 같은 값. 

# 하나의 element 만 갖는 튜플일 때, (1) 이 아니라 (1,) 로 해야함

# tuple도 슬라이싱 가능.

# 튜플도 곱, 더하기 가능.

# 리스트에서 사용했던 함수도 똑같이 튜플에 적용가능. 예)len(t2)

#인덱싱 가능 []


# str형으로부터 tuple형 생성
# stri='march'
# tup_stri=tuple(stri)
# print(tup_stri)


# 리스트형>튜플형 생성
# list_s=['m','l']
# s_list_s=tuple(list_s)
# print(s_list_s)


# min or max 함수도 가능.
# li=('aanuary','zarch','iecember')
# print(max(li))

# li=(1,2,3,4,5)
# print(max(li))


# list1=['eng','math','science','social']
# list1[1]='과제'
# print(list1)






# set형={'element_1','element_2'...} 중괄호를 사용.  데이터 중복이 없다. 순서가 없다.
# 집합과 관련된 자료형이다.
# s2={1,1,2,2,3}
# print(s2)
# >>{1,2,3}                ---- 중복이안됨. index 불가(순서없음)




# 변수할당 가능. hello={"hello","hi"}
# list 나 tuple을 기반으로도 생성가능.
# set_hello=set('hello')
# print(set_hello)

#  list 와 tuple 에서 사용하는 함수도 사용가능 len

# set_hello={'hello',"hi","kind"}
# print(len(set_hello))
# >>>3


list1={"홍길동","박수지","박상민","강누리","하민우"}
late_list1={"홍길동","박수지","박상민"}
abs_list1={"박상민","하민우"}

bonus=list1-(late_list1 | abs_list1)
print('보너스를 받을 사람은',bonus)

nightwork=late_list1 & abs_list1

print('야근을 할게될 사람은',nightwork)




# 딕셔너리 dic {key:value} = key와 value 를 구한다.
# key:value

# 딕셔너리는 원소 값이 정해져있지 않다.

# 변경할 수 없는 값만 딕셔너리의 key가 될 수 있다. (튜플)
 
price={'오뎅':'3000','떡볶이':'2000'}
print(price['오뎅'])
# >>>3000


#4.새로운 항목을 딕셔너리에 추가하는 함수
d={1:"first",2:'second'}
d[3]='third'
print(d)


#5. 딕셔너리에 있는 원소를 삭제하는방법
#   키값을 통해 삭제한다.
d={1:"first",2:'second'}
d[3]='third'
del d[3]
print(d)

# 6~7. key나 value 들로만 이루어진 list 출력하는법
#    d.keys()  or d.values()

d={1:"first",2:'second'}
d[3]='third'
print(d.keys())
print(d.values())


# -----------------예제--------------------

#9
price={'americano':2000,'cafelatte':2500,"greentea":3000,"mochalatte":3500}
print(price['mochalatte'])
print(price['americano'])

# 10
# 리스트: 변경가능.   price[1]=3 , 슬라이싱 가능 price[1:3] , 함수도 가능 len(price)

# 튜플:   변경불가능. 슬라이싱가능 price[1:3]  , 함수가능 len , 덧셈 곱셈 가능 s1+s2 , s2*3

# set:  순서없이 무작위. { } 쓰고, 집합을 사용할 때 유용함. &,|,-   

# 딕셔너리: { } 사용하고, 순서 무작위. 튜플만 key값 가능 . 인덱싱 불가. key 값 을통해 삭제가능.
# 딕셔너리: 더하기 도 가능 price['오뎅']=3000 



