# class Kenny:
#     def __init__(self,first,second):
#         self.first=first
#         self.second=second
#     def setdata(self,first,second):
#         self.first=first
#         self.second=second
#     def add(self):
#         result=self.first+self.second
#         return result

# a=Kenny(1,2)
# a.setdata(1,2)
# print(a.add())



# class  FourCal:
#     def setdata(self,first,second):
#         self.first=first
#         self.second=second
#     def add(self):
#         result=self.first+self.second
#         return(result)
# a=FourCal()
# a.setdata(1,2)

# print(a.add())
    
# class  FourCal:
#     def __init__ (self,first,second):
#         self.first=first
#         self.second=second
#     def setdata(self,first,second):
#         self.first=first
#         self.second=second
#     def add(self):
#         result=self.first+self.second
#         return result

# a=FourCal(4,2)
# a.setdata(4,2)

# print(a.add())


# class MoreFourCal(FourCal):
#     pass

# a=MoreFourCal(4,2)
# print(a.add())



# class MoreFourCal(FourCal):
#     pass

# a=MoreFourCal(1,2)
# print(a.add())


# class  FourCal:                       -     -----클래스에 FourCal 지정
#     def __init__ (self,first,second):          --- init 함수는 무조건 먼저 실행
#         self.first=first                     
#         self.second=second
#     def setdata(self,first,second):
#         self.first=first
#         self.second=second
#     def add(self):
#         result=self.first+self.second
#         return result
#     def div(self):
#         result=self.first/self.second
#         return result

# a=FourCal(1,2)                ---init 함수 지정 (self는 a, 그러니까 FourCal 함수 그대로 써놓은것)
# # print(a.add())      
# # print(a.mul())


# FourCal  에 이어서 자식 클래스 생성


# class MoreFourCal(FourCal):    ------ 상속하는 자식 폴더
# class MoreFourCal(FourCal):
#     def div(self):
#         if self.second==0:
#             return 0
#         else:
#             self.first/self.second

# a=MoreFourCal(4,0)
# print(a.div())                        ----- 똑같은 div 함수라도 자식 함수가 출력된다.
