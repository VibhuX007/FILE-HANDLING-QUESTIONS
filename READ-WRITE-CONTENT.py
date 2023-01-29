#READ A CONTENT FROM ONE FILE AND WRITE IT INTO ANOTHER FILE.
f = open("D:\\visual studio code\\python programs\\lab.txt",'r')
l = f.read()
f.close()
f = open("D:\\visual studio code\\python programs\\FILE HANDLING QUESTIONS\\LAB2.txt",'w')
f.write(l)
f.close()
    