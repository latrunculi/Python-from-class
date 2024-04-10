print("This program will calculate the price of a sale item.")
print("It will also include sales tax.")
            
original_price = int(input("Input the original price: "))
discount = int(input("Input the discount (in percent terms): "))
sales_tax = int(input("Input the sales tax (in percent terms): "))

print("Your original price was", original_price)
print("Your price after discount is", original_price * (1 - discount/100))
print("Your price after tax is", original_price * (1 - discount/100) * (1 + sales_tax/100))
