name=input()
score=int(input())

if score >= 90:
    print(name,"의 학점 : A")

elif score in range(80,90):
    print(name,"의 학점 : B")

elif score in range(70,80):
    print(name,"의 학점 : C")

elif score in range(60,70):
    print(name,"의 학점 : D")

else:
    print(name,"의 학점 : F")
