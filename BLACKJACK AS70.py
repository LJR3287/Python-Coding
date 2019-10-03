
Cardvalue=(1,2,3,4,5,6,7,8,9,10,10,10,10)
Cards =raw_input("Enter cards you have (10 is entered as T) ")
CardLen=len(Cards)
Total = 0
has_ace = 0
for i in range(0,CardLen):
    if Cards[i] == "A":
        has_ace += 1
    if Cards[i].isdigit():
        V=int(Cards[i])
        Total+=V
    else:
        Total += 10
for j in range(0,has_ace):
    if Total > 21:
       Total -= 9

    pass
print("Cards= ",Cards,"Card total= ", Total)



