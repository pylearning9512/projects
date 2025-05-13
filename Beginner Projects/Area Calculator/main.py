"""

this is a beginner level project to showcase fundamentals
of programming through the python language

the design of this program is done with a functional 
programming approach

"""


#area calculator
print("available operations: ")
print("1- square or rectangle" )
print("2-triangle" )
print("3- circle")
print(" ")#empty spaces for human readability on the terminal
print(" ")

user_choice= int(input("please choose the operation to perform: "))


#functions containing the individual formula
#for getting the area
def square_rectangle():
    lenght=float(input("what is the length of your figure in cm's?: "))
    height=float(input("what is the height?: "))
    area=lenght*height
    print(f"the area of the shape is {area} cm")
def triangle():
    base= float(input("what is the base in cm?: "))
    height=float(input("what is the height in cm?: "))
    area= (base*height)/2
    print(f"the area of the shape is {area} cm")
def circle():
    radius= float(input("enter the radius of the circle in cm: "))
    pi=3.1416
    area= pi*radius**2
    print(f"the area of the shape is {area} cm")

#this is the functionality to call the other
#functions with the user input
def calling__function():
    if user_choice in operations:
        result=operations[user_choice]()
        return result
    
        

#dictionary with the option keys, and functions as the values
operations={ 
    1:square_rectangle, 
    2: triangle,
    3:circle
    }

calling__function()