def findMax(a,b,c):
    if a>b:
        big=a
    else:
        big=b
        
    if c>big:
        big=c

    return big


a=int(input("첫번째 숫자: "))
b=int(input("두번째 숫자: "))
c=int(input("세번째 숫자: "))

biggest=findMax(a,b,c)
print(a,b,c,"중 가장 큰 수는" , biggest,  "입니다.")
