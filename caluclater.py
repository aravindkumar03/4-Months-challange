a=float(input("enter value"))
c=input("enter symbol for caluclation")
b=float(input("enter value"))
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='/':
    print(a/b)
elif c=='*':
    print(a*b)
elif c=='%':
    print(a%b)
else:
    print("incorrect response")
