#write a function that takes the radius of a circle as input and returns the area of the circle. Use the formula A = πr^2, where A is the area and r is the radius. You can use the math module to get the value of π.
def area_of_circle():
    radius=float(input("enter radius of circle: "))
    area=3.14*radius**2
    return area
print(area_of_circle())