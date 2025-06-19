from turtle import Turtle, done

tospa = Turtle()
tospa.fillcolor("red")
tospa.begin_fill()

for x in range(1,5):
    tospa.forward(100)
    tospa.right(90)

tospa.write("Kaplumbağayım ben")
done()