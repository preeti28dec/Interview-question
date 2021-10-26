# write a simple shipping service.
# A person should be able to run this from the command line.
Country_code=(input("Enter the country code:- "))
Product_code=(input("Enter the product code:-"))
Weight_in_kg=float(input("Enetr the weight in kg:-"))
if Country_code=="UK":
    if Weight_in_kg<5.0:
        if Product_code in "123" :
            print("Yor currency is",5*1.2*(1+0.18))
        elif Product_code in "234" :
                print("Yor currency is",5*1.5*(1+0.18)) 
        else:
            print(5*(1+0.18), "INR")    
    elif Weight_in_kg>=5.0:
        if Product_code in "123" :
            print("Yor currency is",15*1.2*(1+0.18))
        elif Product_code in "234" :
                print("Yor currency is",15*1.5*(1+0.18)) 
        else:
            print(15*(1+0.18), "INR") 
elif Country_code=="US":
    if Weight_in_kg<10.0:
        if Product_code in "123" :
            print("Yor currency is",5*1.2*(1+0.18))
        elif Product_code in "234" :
                print("Yor currency is",5*1.5*(1+0.18)) 
        else:
            print(5*(1+0.18), "INR")    
    elif Weight_in_kg>=10.0:
        if Product_code in "123" :
            print("Yor currency is",15*1.2*(1+0.18))
        elif Product_code in "234" :
                print("Yor currency is",15*1.5*(1+0.18)) 
        else:
            print(15*(1+0.18), "INR") 
