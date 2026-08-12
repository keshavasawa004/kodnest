def calculate_bill(price, quantity):
    a=input("product name")
    total=price*quantity
    if total>=2000:
        discount=total*0.10
        totalamount=total-discount
    else:
        totalamount=total
    
    print(f"Product Name: {a}")
    print(f"price: {price}")
    print(f"quantity: {quantity}")
    print(f"Total amount: {total}")
    print(f"Discount: {discount}")
    print(f"Final Amount: {totalamount}")


calculate_bill(100,220)

