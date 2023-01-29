f = open("FILE HANDLING QUESTIONS\\lab.txt",'r')
l = f.read()
ls = l.split()
print("No. of words: ",len(ls))