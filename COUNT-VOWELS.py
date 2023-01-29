f = open("D:\\visual studio code\\python programs\\FILE HANDLING QUESTIONS\\lab.txt",'r')
l = f.read()
nv = 0
v = 'AEIOUaeiou'
for i in l:
    if i in v:
        nv += 1
print("Number of vowels in the file are:",nv)