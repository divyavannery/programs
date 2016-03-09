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
combinations=sorted(combinations)
for i in combinations:
    num=number
    count=0
    for j in i:
        j=int(j)
        j=j-count
        num=num[:j]+num[(j+1):]
        count=count+1
    array.append(int(num))
array.sort()
print "ans",array[0]
