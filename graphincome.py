n=int(raw_input("enter number of nodes"))
graph=[]
count=[0 for i in range(n)]
for i in range(n):
   index=int(raw_input());
   graph.append(index)
   count[index]=count[index]+1
   
maxc=0;

for i in range(n):
    if count[i]>maxc:
        maxc=count[i]
        indexstore=i
print " maximum incoming for",indexstore
