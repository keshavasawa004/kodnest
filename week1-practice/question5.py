def calculate_salary(basic_salary,bouns_percent=5):
    a=input("empolyee name")
    bonus=b*(bouns_percent/100)
    final_salary=basic_salary+bonus
    print(f"Employee Name: {a}")
    print(f"Basic salary: {b}")
    print(f"Bonus percentage: {bouns_percent}")
    print(f"Bonus Amount: {bonus}")
    print(f"Final Salary: {final_salary}")

b=int(input("basic salary"))
c=input("does employee has special bonus percent yes or no").lower()

if c=="yes":
    s=int(input("enter the bonus percent"))
    calculate_salary(b,s)
else:
    calculate_salary(b)


