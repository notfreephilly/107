

# assign a variablee
fork = "utencil"
print(fork)

first_name = 'philip'
last_name = 'yoder'
age = 113
height = '5ft 9in'
weight = '168lbs'
is_single = True
is_admin = False

# if/else statement
if age < 100:
    print('baby')
elif age >= 100:
    print('you are so old...')
else:
    print('do you exist??')


# functions

def say_hello():
    print('hi i guess')

def say_goodbye(name):
    print('bye' + name)

say_hello()
say_goodbye(' felipe')

print("Hello  my name is" + first_name + " and I am" + str(age) + " years old.")

# arrays aka list
winning_numbers = [21, 42, 69,  777, 10]

color = ["white", "yellow", "blue"]
# add to the list
color.append("red")
print(color)

# travel the list
for colors in color:
    print(colors)

# dictionary
me = {
    "first_name": "Philip",
    "last_name": "Yoder",
    "age": 30

}
print(me["first_name"])