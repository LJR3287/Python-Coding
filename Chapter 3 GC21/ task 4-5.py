#task 4
import turtle
tess = turtle.Turtle()
tess.setheading(0)
tess.left(3645)

print("tess turns 100 and 1 quarter times and is heading south east")

#task 5
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in range (9):
    print(xs[i])

for j in range (9):
    print(xs[j],xs[j]*xs[j])

total=0
for k in range (9):
    total += xs[k]

print(total)

product=1
for l in range (9):
    product *= xs[l]

print(product)
