num=int(input("enter how many member they are team"))
i=[]
a=0
even_count=0
odd_count=0
while a<num:
    n=int(input("enter the number")) 
    i.append(n) 
    if i[a]%2==0:
        even_count+=1
    else:
        odd_count+=1
    a+=1
print(i)
print(even_count,odd_count)
if odd_count<even_count:
    print( "READY FOR BATTLE" )
else:
    print(" NOT READY")

