Input_String=raw_input("Enter bit string (7 bits)")
Number_of_ones = 0
for i in range(0,7):
    if Input_String[i]=='1':
        Number_of_ones += 1
if (Number_of_ones %2) == 0:
    parity_bit = 0
else: parity_bit = 1
print("Input = ", Input_String,"Parity = ", parity_bit)
