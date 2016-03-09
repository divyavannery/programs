def trailingzeroes(n):
    i=5
    num=0
    while n/i>=1:
        num=num+n/i
        i=i*5
    return num
n=int(raw_input("enter number"))
print trailingzeroes(n)

