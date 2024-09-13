
def fibo(n):
    if n< 0 :
        print("Please enter terms greater than zero!!")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

if __name__=="__main__":
    n = int(input("Enter the number of terms: "))
    for i in range(n):
        print(fibo(i))
        