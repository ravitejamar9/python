from sys import argv
sum=0
for value in argv[1:]:
    sum+=int(value)
print("The Sum:",sum)
