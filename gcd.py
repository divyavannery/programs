a=int (raw_input("enter number 1"))
b=int (raw_input("enter number 2"))
if b>a:
   a=a+b
   b=a-b
   a=a-b
while b!=0:
    r=a%b
    if r==0:
        break
    a=b
    b=r
print "gcd",b
