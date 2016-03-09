import itertools

n=int(raw_input("enter the limit"))
numbers=[]
for i in range(n):
    numbers.append(int(raw_input()))
sum_num=9999
for i in numbers:
    for j in numbers:
        if i==j:
            break
        if abs(i+j)<abs(sum_num):
            sum_num=i+j
            x=i
            y=j
print "sum",sum_num
print "numbers",x,y
        
