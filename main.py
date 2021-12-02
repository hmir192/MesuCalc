import math

print("""\nWelcome to mensuration-calculator. Mensuration is the branch of geometry that deals with the measurement
of area, length, or volume in 2D and 3D shapes. Please select Numbers infront of the given shapes to procceed.\n""")
print("""

--------- 2D Shapes ---------
[1] Quadrilaterals
[2] Circles
[3] Triangles
--------- 3D Shapes ---------
[1] Cuboids
[2] Cylinder
[3] Hemisphere
[4] Sphere

""")

shape = int(input())
if shape == 1:
    len = int(input("Enter its length: "))
    wid = int(input("Enter its width: "))
    unit = input("Enter its unit: ")
    print("what kind of calculation do you want to do?\n")
    print("""
    [1] Calculate Area
    [2] Calculate Perimeter
    """)
    oper = int(input())
    if (oper == 1):
        res = (len*wid)
        print(str(res) + " " "sq" + str(unit))
    elif (oper == 2):
        res = (2*len + 2*wid)
        print(str(res) + " " + str(unit))

elif shape == 2:
    r = int(input("Enter its radius: "))
    unit = input("Enter its unit: ")
    pi = 3.14159265358979323846264338327950288419716939937510
    print("what kind of calculation do you want to do?\n")
    print("""
    [1] Calculate Area
    [2] Calculate Circumference
    """)
    oper = int(input())
    if (oper == 1):
        res = (pi*(r**2))
        print(str(res) + " " "sq" + str(unit) + " is the area")
    elif (oper == 2):
        res = (2*pi*r)
        print(str(res) + " " + str(unit) + " is the circumfrence")


elif shape == 3:
    a = int(input("Enter length of 1st side: "))
    b = int(input("Enter length of 2nd side: "))
    c = int(input("Enter length of 3rd side: "))
    unit = input("Enter its unit: ")
    p = a + b + c
    print("what kind of calculation do you want to do?\n")
    print("""
    [1] Calculate Area [# heron's formula]
    [2] Calculate Perimeter
    [3] Calculate Area [base*height/2 method]
    """
    )
    oper = int(input())
    if (oper == 1):
        s = ((p/2))
        res = (math.sqrt(s * (s - a) * (s - b) * (s - c))) #heron's formula as it would be easier for user to get both results from same
                                                         #wasnt able to write heron's formula w/o the inbuilt math library, had to use it 
        if (res <= 0):
            print("such type of triangle does not exist ") #as when a+b>c is not true, a triangle cannot be formed
        else:
            print(str(res) + " " "sq" + str(unit) + " is the area " )
    elif (oper == 2):
        print(str(p) + str(unit) + " is the perimeter ")
