n=int(raw_input("enter the limit"))
numbers=[]
for i in range(n):
    numbers.append(int(raw_input()))
    if numbers[i]==i:
        num=numbers[i]
    
print "output",num
