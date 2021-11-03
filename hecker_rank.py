Customer=int(input("enter the number of customers"))
serve_time=[]
i=0
while i<=Customer:
    order_number=int(input("enter your order number"))
    preparation_time=int(input("enter you preparation time"))
    Calculate= order_number + preparation_time
    serve_time.append(Calculate) 
    i+=1     
j=0
while j<len(serve_time):
    if serve_time[i]==serve_time[j]:
        print(serve_time.sort())
    j+=1
print(serve_time)