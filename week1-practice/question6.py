def analyze_numbers(numbers):
    total=0
    count_odd=0
    count_even=0
    for i in range(n):
        total=total+numbers[i]
    avg=total/n
    a=max(numbers)
    b=min(numbers)
    for i in range(n):
        if numbers[i]%2==0:
            count_even+=1
        elif numbers[i]%2!=0:
            count_odd+=1

    print(f"Sum of numbers {total}")
    print(f"Average {avg}")
    print(f"Highest number {a}")
    print(f"Lowest number {b}")
    print(f"even number count {count_even}")
    print(f"odd number count {count_odd}")

def numbers_above_average(numbers,avg):
    for i in range(n):
        if n[i]>analyze_numbers.avg:
            count_avg+=1

numbers=list(map(int,input("enter the number").split()))
n=len(numbers)
analyze_numbers(numbers)


    

