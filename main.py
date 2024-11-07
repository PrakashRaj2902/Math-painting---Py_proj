from Canvas import Canvas
from Shapes import Square, Rectangle

canvas_width = int(input("Enter Canvas width: "))
canvas_heigth = int(input("Enter Canvas height: "))

color = {"white" : (255,255,255), "black" : (0,0,0)}
canvas_color= input("Enter Canvas color (white or black):")

canvas = Canvas(width=canvas_width, height=canvas_heigth, color=color[canvas_color])

while True:
    shape_type = input("What do you like to draw(rectangle or square)? Enter quit to quit. ")
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x value of the rectangle: "))
        rec_y = int(input("Enter y value of the rectangle: "))
        rec_width = int(input("Enter width value of the rectangle: "))
        rec_height = int(input("Enter height value of the rectangle: "))
        rec_red = int(input("How much red should the rectangle have (0 - 255): "))
        rec_green = int(input("How much green should the rectangle have (0 - 255): "))
        rec_blue = int(input("How much blue should the rectangle have (0 - 255): "))

        r1 = Rectangle(x=rec_x, y=rec_y, width=rec_width, height=rec_height, color=(rec_red, rec_green, rec_blue))
        r1.draw(canvas)

    if shape_type.lower() == "square" :
        squ_x = int(input("Enter x value of the square: "))
        squ_y = int(input("Enter y value of the square: "))
        squ_side = int(input("Enter side value of the square: "))
        squ_red = int(input("How much red should the square have (0 - 255): "))
        squ_green = int(input("How much green should the square have (0 - 255): "))
        squ_blue = int(input("How much blue should the square have (0 - 255): "))

        s1 = Square(x= squ_x, y= squ_y, side= squ_side, color=(squ_red, squ_green, squ_blue))
        s1.draw(canvas)

    if shape_type == "quit":
        break

canvas.make('canvas.png')


