import itertools

number=raw_input("enter the number");
k=int(raw_input("enter the number of digits"))
n=len(number)
comb=[i for i in range(n)]
comb=''.join(str(i) for i in comb)
print comb
combinations=list(itertools.combinations(comb,k))
num=number
array=[]
print combinations
for i in combinations:
    num=number
    for j in i:
        j=int(j)
        num=num[:j]+num[(j+1):]
    array.append(int(num))
    print int(num)
array.sort()
print "ans",array[0]
