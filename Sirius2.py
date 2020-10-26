
print("Введите время горения левого прожектора.")
A=int(input())
print("Введите время горения среднего прожектора.")
B=int(input())
print("Введите время горения правого прожектора.")
C=int(input())
x=min(A,B//2,C)
A-=x
B-=2*x
C-=x
if A==0:
    print(x*4)
elif B==0:
    print(x*4+1)
elif C==0:
    print(x*4+2)
else:
    print(x*4+3)




