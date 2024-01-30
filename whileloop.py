print("Enter the number")
n1 = int(input()) # 5
s1 = 0
i = 1
while i < n1:
    s1 = s1 + i # (s1=0,i=1)=1; (s1=1,i=2)=3; (s1=3,i=3)=6; (s1=6,i=4)=10
    i = i + 1
    print("sum",s1)