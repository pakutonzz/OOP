import turtle as tur
import colorsys as cs
tur.setup(600,600)
tur.speed(0)
tur.tracer(100)
tur.width(2)
tur.screensize(70)
tur.bgcolor('black')
for j in range (25):
 for i in range (15) :
    tur.color('white')
    tur.right(90)
    tur.circle(200-j*4,90)
    tur.left(90)
    tur.circle(200-j*4,90)
    tur.right(180)
    tur.circle(2,54)
    tur.hideturtle()


for i in range (180):
    tur.speed(0)
    tur.color('#277BC0')
    tur.circle(190 - i, 90)
    tur.left(90)
    tur.color('#98B41A')
    tur.circle(190 - i, 90)
    tur.left(18)

tur.clear()
tur.color('white')
style = ('Comic Sans MS', 30, 'italic')
tur.write('sorry for dont have any flowers for you', font=style, align='center')
tur.clear()
tur.write('so i give you this e-flower มันพอแทนกันได้มั้ยคับ', font=style, align='center')
