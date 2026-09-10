#OPERATORS
age = 19
height = 1.76
complex_num = 1 + 1j
base = int(input("enter base: "))
height = int(input("enter height: "))
area_of_tri = 0.5 * base * height
print(f"the area of the triangle is {area_of_tri}")
side_a = int(input("enyer side a: "))
side_b = int(input("enter side b: "))
side_c = int(input("enter side c: "))
perimeter_of_tri = side_a + side_b + side_c
print(f"the perimeter of the triangle is {perimeter_of_tri}")
lenght = int(input('enter lenght: '))
width =  int(input('enter width: '))
area_of_rect = lenght * width
print(f"area of rectangle = {area_of_rect}")
perimeter_of_rect = 2 * (lenght + width)
print(f"the perimiter of rectangle = {perimeter_of_rect}")
radius = float(input("enter radius: "))
area_of_circle = 3.142 * radius **2
print(f"area of circle = {area_of_circle}")
circumfrence = 2 * 3.142 * radius
print(f"circumfrence = {circumfrence}")

print("jargon" in "i hope this course is not full of jargons")
print(len("python") != len("dragon"))
print(("on" in 'pyhton')and ('on' in "dragon"))
lenght = len('python')
lenght_float = float(lenght)
lenghht_str = str(lenght_float)
print(lenght, lenght_float, lenghht_str)

print(7 // 3 == int(2.7))
print('10' == 10)
print(int(float('9.8')) == 10)
hours = int(input("enter hours: "))
rate_per_hour = int(input("enter rate per hour: "))
weekly_earnings = hours * rate_per_hour
print(f"your weekly earnings is = {weekly_earnings}")

years = int(input("enter number of years: "))
seconds_lived = years * 3153600
print(f"you have lived for {seconds_lived} seconds")
for i in range(1, 6):
    print(i, i**0, i**1, i**2, i**3)

