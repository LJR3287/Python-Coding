Morse_code = ["0-", "-000", "-0-0", "-00", "0", "00-0", "--0", "0000", "00", "0---", "-0-", "0-00", "--", "-0", "---", "0--0", "--0-", "0-0", "000", "-", "00-", "000-", "0--", "-00-", "-0--", "--00" ]
X = raw_input("Please enter a letter ")
letter=X[0]
print (letter, ord(letter), ord(letter)-65, Morse_code[ord(letter)-65])

Y = raw_input("Please enter a morse code ")
for i in range(0,26):
    if Y==Morse_code[i]:
        print("Morse code is ", Morse_code[i],"letter is ", chr(65+i))
        break
print (Y)
