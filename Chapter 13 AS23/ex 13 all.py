f = open("pythonfile.txt", "r")
xs = f.readlines()
f.close()

#Ex 13-1 Write a program that reads a file and writes out a new file
#        with the lines in reversed order (i.e. the first line in the old file
#        becomes the last one in the new file.)
h = open("reverse.txt", "w")
for i in range(len(xs)):
    h.write(xs[len(xs)-i-1])
h.close()
    
#Ex 13-2 Write a program that reads a file and prints only those lines that contain
#        the substring snake.
b = open("snakefile.txt", "r")
ss = b.readlines()
b.close()

c = open("withsnake.txt", "w")
for i in range(len(ss)):
    if (ss[i].find("snake") != -1): # lines with snake
        c.write(ss[i])
c.close()

#Ex 13-3 Write a program that reads a text file and produces an output file which is a copy of the file, except the first five columns of each line contain a four digit line number, followed by a space. Start numbering the first line in the output file at 1. Ensure that every line number is formatted to the same width in the output file. Use one of your Python programs as test data for this exercise: your output should be a printed and numbered listing of the Python program.
g = open("withnumber.txt", "w")
for i in range(len(xs)):
    str="%04d %s" % (i,xs[i])
    g.write(str)
g.close()

#Ex 13-4 Write a program that undoes the numbering of the previous exercise: it should read a file with numbered lines and produce another file without line numbers.
e = open("withnumber.txt", "r")
ys = e.readlines()

d = open("withoutnumber.txt", "w")
for i in range(len(ys)):
    str=ys[i][5:len(ys[i])]
    d.write(str)
d.close()

print ("End of programs")
