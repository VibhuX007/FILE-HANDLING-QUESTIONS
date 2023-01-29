#TO COPY EVEN WORDS OF ONE FILE TO ANOTHER.
f = open("D:\\visual studio code\\python programs\\FILE HANDLING QUESTIONS\\lab.txt",'r')
l = ((f.readlines()))
f.close()
f = open("D:\\visual studio code\\python programs\\FILE HANDLING QUESTIONS\\LAB3.txt",'w')
c = 0
for i in l:
    for j in i.split():
        if c%2==0:
            f.write(j+' ')
        c += 1
f.close()