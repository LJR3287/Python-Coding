First_number=0
second_number=1
for i in range(0,50):
    Third_number=(First_number+second_number)
    print(First_number, second_number, Third_number)
    First_number=second_number
    second_number=Third_number

