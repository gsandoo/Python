def sol(n,b):
    if n==5:
        return b
    else:
        b+=b
        return sol(n+1,b)

print(sol(0,5))

# 거듭제곱
def kin(a,b):
    if b==1:
        return a
    else:           
        return a*kin(a,b-1)
    
print(kin(5,2))

