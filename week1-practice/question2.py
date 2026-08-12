a=input("Enter your name")
b=list(map(int,input("enter your marks").split()))
n=len(b)
total=0
failed=0
passed=0
for i in range(n-1):
    total=total+b[i]

avg=total/5
high=max(b)
low=min(b)
for i in range(n):
    if b[i]<=40:
        failed+=1
    elif b[i]>=41:
        passed+=1
print(f"Total Marks {total}")
print(f"Average Marks {avg}")
print(f"Highest Marks {high}")
print(f"Lowest Marks {low}")
print(f"number of subject Passed {passed}")
print(f"number of subject Failed {failed}")
if avg>=90:
    print("grade=A")
elif 75<=avg<=89:
    print("grade=B")
elif 60<=avg<=74:
    print("grade=C")
elif 40<=avg<=59:
    print("grade=D")
else:
    print("grade=F")

for i in range(n-1):
    if b[i]>avg:
        print(b[i],end=',')