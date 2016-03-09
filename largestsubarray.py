n=int(raw_input("enter limit"))
numbers=[]
for i in range(n):
    numbers.append(int(raw_input()))
prevsum =-999
prevlist=[]
curlist=[]
for i in range(n):
    curlist=[]
    for j in range(i,n):
        curlist.append(numbers[j])
        cursum=sum(curlist)
        if cursum>prevsum:
            prevlist=curlist[0:]
            prevsum=cursum
print "largest subarray",prevlist
print "sum",prevsum
            
