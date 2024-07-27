n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
n3=int(input("Enter Third Number:"))

if(n1>n2):
    if(n1>n3):
        print("The Greater Number is ",n1)
    else:
        print("The greater number is ",n3)
elif(n2>n3):
    print("The greater is ",n2)
else:
    print("The greater is ",n3)
    
    