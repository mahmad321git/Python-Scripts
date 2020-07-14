import math

#There are feet in a mile. Write a Python statement that calculates and prints the number of feet
#in miles. Miles to feet template ­­­ Miles to feet solution ­­­ Miles to feet (Checker)

x = 13
y = 5280
z = x * y
print("total# of feet in 13 miles is ")
print(z)


#Write a Python statement that calculates and prints the number of seconds in hours, minutes
#and seconds

hours, minutes, seconds  = 7, 21, 37

Seconds_In_Hours = hours * 60 * 60
Seconds_In_Minutes = 21 * 60
Seconds = seconds
Total_Seconds = Seconds_In_Hours + Seconds_In_Minutes + Seconds
print("Total# of seconds")
print(Total_Seconds)

#The perimeter of a rectangle is , where and are the lengths of its sides. Write a Python
#statement that calculates and prints the length in inches of the perimeter of a rectangle with sides of
#length and inches

Length = 4
Inches = 7
Perimeter = (2 * Length * Inches) + (2* Length * Inches)
print('Total Perimeter in inches')
print(Perimeter)

#The area of a rectangle is , where and are the lengths of its sides. Note that the
#multiplication operation is not shown explicitly in this formula. This is standard practice in
#mathematics, but not in programming. Write a Python statement that calculates and prints the area in
#square inches of a rectangle with sides of length and inches

Area = (Length * Inches) * (Length * Inches)
print("Area of Rectangle")
print(Area)

#The circumference of a circle is where is the radius of the circle. Write a Python statement that
#calculates and prints the circumference in inches of a circle whose radius is inches. Assume that
#the constant

Radius = 8
Pi = 3.14
Circumference = 2 * Pi * Radius
print("Total Circumference")
print(Circumference)

#The area of a circle is where is the radius of the circle. (The raised in the formula is an
#exponent.) Write a Python statement that calculates and prints the area in square inches of a circle
#whose radius is inches. Assume that the constant

Area_of_Circle = Pi * (Radius * Radius)
print("Area of Circle is")
print(Area_of_Circle)

#Given dollars, the future value of this money when compounded yearly at a rate of percent
#interest for years is . Write a Python statement that calculates and prints the value
#of dollars compounded at percent interest for years

Dollars = 1000
Years = 10
Interest = 7
Value_of_Dollars = Dollars*(1 + 0.01*Interest)*Years

print("Value Of Dollars")
print(Value_of_Dollars)

#Write a single Python statement that combines the three strings , and
#(plus a couple of other small strings) into one larger string
#and prints the result

String1 = "My name is "
String2 =  "Joe "
String3 = "Warren"
print(String1 + String2 + String3)

#Write a Python expression that combines the string from the
#string and the number and then prints the result (Hint: Use the function to
#convert the number into a string.)

Number = 54
String4 = "Joe Warren is "
print(String4 + str(Number) + " years old")

#The distance between two points and is . Write a
#Python statement that calculates and prints the distance between the point

Point1_Cordinate1 = 2
Point1_Cordinate2 = 2

Point2_Cordinate1 = 5
Point2_Cordinate2 = 6

Two_Point_Distance = math.sqrt((Point2_Cordinate1-Point1_Cordinate1)**2 + (Point2_Cordinate2-Point1_Cordinate2)**2)
print("Total Distance between two points: ")
print(Two_Point_Distance)
