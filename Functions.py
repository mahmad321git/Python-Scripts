import math
import random

#Write a Python function that takes a parameter and returns the number of
#feet in miles

def miles_to_feet(miles):
    Number_Of_Feet = miles * 5280
    print("Number of Feet in Miles: " + str(Number_Of_Feet))

miles_to_feet(13)

#Write a Python function that takes three parameters , and
#and returns the total number of seconds for hours, minutes and
#seconds

def total_seconds(hours, minutes, seconds):
    hours = hours * 60 * 60
    minutes = minutes * 60
    Total_Seconds = hours + minutes + seconds
    print("Total# of seconds for hours minutes and seconds:" + str(Total_Seconds))

total_seconds(7,8,32)

#Write a Python function that takes two parameters and
#corresponding to the lengths of the sides of a rectangle and returns the perimeter of the
#rectangle in inches

def rectangle_perimeter(width, height):
    Perimeter_Of_Rectangle = (2 * width) + (2 * height)
    print("Perimeter of Rectangle  is " + str(Perimeter_Of_Rectangle))

rectangle_perimeter(20, 10)


#Write a Python function that takes two parameters and
#corresponding to the lengths of the sides of a rectangle and returns the area of the
#rectangle in square inches

def rectangle_area(width, height):
    Area_Of_Rectangle = width * height
    print("Area of Rectangle: " + str(Area_Of_Rectangle))

rectangle_area(20, 25)

#Write a Python function that takes two parameters and
#corresponding to the lengths of the sides of a rectangle and returns the area of the
#rectangle in square inches

def circle_circumference(radius):
    Circumference_Circle = 2 * 3.14 * radius
    print("Circle circumference: " + str(Circumference_Circle))

circle_circumference(10)


#Write a Python function that takes a single parameter
#corresponding to the radius of a circle in inches and returns the the circumference of a
#circle with radius in inches. Do not use , instead use the module to supply a
#higher­precision approximation to

def circle_area(radius):
    Circle_Area = math.pi * (radius ** 2)
    print("Area of Circle is: " + str(Circle_Area))

circle_area(20)

#Write a Python function that takes three parameters ,
#and and returns the future value of dollars invested at
#percent interest, compounded annually for years

def future_value(present_value, annual_rate, years):
    Future_Present_Value = present_value * (1 + 0.01 * annual_rate)**years
    print("Future Present Value: " + str(Future_Present_Value))

future_value(1000, 7, 10)

#Write a Python function that takes as input the parameters and
#(strings) and returns a string of the form where the percents are
#the strings and . Reference the test cases in the provided template for
#an exact description of the format of the returned string

def name_tag(first_name, last_name):
    print("My name is " + first_name + " " + last_name)

name_tag("Ahmad", "Idrees")

#Write a Python function that takes as the parameters , , and
#returns the distance between the points

def point_distance(xo,yo,x1,y1):
    Total_point_distance = math.sqrt((xo - x1)**2 + (yo - y1)**2)
    print("Total point Distance: " + str(Total_point_distance))

point_distance(2,2,5,6)

#Challenge1, Find the area of
#Write a Python function that takes the parameters , , , ,
#and , and returns the area of the triangle with vertices

def triangle_area(xo,yo,x1,y1,x2,y2):
    Ab = math.sqrt((xo - x1)**2+(yo-y1)**2)
    Bc = math.sqrt((xo - x2)**2+(yo-y2)**2)
    Ca = math.sqrt((x1 - x2)**2+(y1-y2)**2)
    Total_Side = 1/2 * (Ab + Bc + Ca)
    Total_Area = math.sqrt(Total_Side*(Ab)*(Bc)*(Ca))
    print("Area of triangle is: " + str(Total_Area))

triangle_area(1,2,3,4,5,6)

#Challenge2, Python function that print digits 10's and 1's digit

def print_digits(number):
    if number >= 0 or number < 100:
        unit = number%10
        ten = (number/10)%10
        print("The tens digit is " + str(ten) + "and the ones digit is " + str(unit))



new_number = random.randrange(100)
print_digits(new_number)

#Challenege3, Python function that ottery game in which 6 numbers are drawn at random. Players can
#purchase a lottery ticket with a specific number combination and, if the number on the ticket matches
#the numbers generated in a random drawing, the player wins a massive jackpot. Write a Python
#function that takes no arguments and prints the message

def powerball():
    Powerball_number = random.randint(1, 36)
    print("Today's numbers are ")
    for x in range(5):
        Drawn_Number = random.randint(1, 60)
        print(Drawn_Number)

    print("The Powerball number is " + str(Powerball_number))

powerball()