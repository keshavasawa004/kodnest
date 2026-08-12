a=input("Enter customer name")
b=int(input("number of units consumed"))
surge=0
if 0<b<=100:
    bill=(b*2)
elif 101<=b<=200:
    bill=(b*3)
else:
    bill=(b*5)

if bill>1000:
    surge=(0.05*bill)
    finalbill=bill+surge
else:
    finalbill=bill
print(f"Customer name:{a}")
print(f"Units Consumed:{b}")
print(F"Electricity Charge:{bill}")
print(f"Surcharge:{surge}")
print(f"Final Bill:{finalbill}")
