string=raw_input("enter the string")
words=string.split(" ")
string=" "
count=-1
for i in words:
    string=string+words[count]+" "
    count=count-1

print string
