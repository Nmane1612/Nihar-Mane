year=int(input("Enter A Year : "))

if(year%4)==0:
    if(year%100)==0:
        if(year%400)==0:
            print("Leap Year")
        else:
            print("Not A Leap Year")
    else:
        print("Not A Leap Year")
else:
     print("Not A Leap Year")
    
