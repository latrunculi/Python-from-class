while True:

    while True:
        try:
            print("This program will calculate the price of a sale item.")
            print("It will also include sales tax.")
            
            original_price = int(input("Input the original price: "))
            
            discount = int(input("Input the discount (in percent terms): "))
            sales_tax = int(input("Input the sales tax (in percent terms): "))
                                    
            print("")
                                    

            if original_price <= 0:
                print("Please input a correct value. That makes no sense!")

                continue
                
            if discount < 0 or discount > 100:
                print("The discount must be between 0 and 99 percent.")
                print("")

                continue

            if sales_tax < 0 or sales_tax > 100:
                print("The sales tax must be between 0 and 99 percent.")
                print("")
                                    
                continue
        
        except ValueError:
            print("Please input acceptable values!")
            print("")

        else:
            print("Your input has been accepted.")
            print("")
            break
    
    print("Your original price was", original_price)
    print("Your price after discount is", original_price * (1 - discount/100))
    print("Your price after tax is", original_price * (1 - discount/100) * (1 + sales_tax/100))
    print("")
  
