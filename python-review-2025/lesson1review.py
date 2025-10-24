#Part one: For each line of code below, write what type of variable is being stored (string, integer, or float). Write your answer as a comment next to each line of code.

first_name = "Bro" # for example: this is a string
food = "pizza"      #This is string
email = "Bro123@fake.com"   #This is string
age = 25    #This is integer
quantity = 3    #This is integer
price = 10.99   #This is float
gpa = 3.2   #This is float
distance = 5.5  #This is float

#Part 2 – Predict the Output

#Without running the code, predict what each line will print:
print(f"Hello {first_name}") # for example: Hello Bro
print(f"You like {food}") # for example: You like pizza
print(f"Your email is: {email}")    #Your email is: lsanchez96cps.edu
print(f"You are {age} years old")   #You are 16 years old
print(f"You are buying {quantity} items")   #You are buying 3 items
print(f"The price is ${price}")     #The price is $40
print(f"Your GPA is {gpa}")     #Your GPA is 3.8
print(f"You ran {distance} km")     #You ran 20 km


# Part 3 – Fix the Errors

# The following code has two mistakes.
# Find and fix them so it runs correctly.

name = "Bro"
food = "pizza"
print(f"Hello {name}")
print(f"You like {food}")

# Missing quotes and wrong variable name
food = "pizza"
print(f"You like {favorite_food}")

# Wrong f-string format
age = 17
print(f"You are {age} years old")

# Mismatched parentheses
price = 12.99
print(f"The total price is ${price}")
      

# Variable name spelled incorrectly
name = "Bro"
print(f"Hello {name}")

# Using + instead of commas
name = "Bro"
print(f"Hello, {name}" )

# Mixing single and double quotes incorrectly
email = "Bro123@fake.com"
print(f"Your email is: {email}")

# Forgot to include the f before the string
age = 21
print(f"You are {age} years old")

# Trying to use a number as a variable
cool = "yes"
print(f"Am I cool? {cool}")

# Missing curly braces
quantity = 3
print(f"You are buying {quantity} items")

# Using a reserved keyword
clas = "ECS"
print(f"You are in {clas}")
#rules for variable name state that they
#cannot start with a number
#another rule is that variable names canno have spaces
#another rule is that variable names
#cannot have special characters like !,@,#,$,%,^,&,*,(,)
#cannot use reserved keywords like class, def, return, etc.

# Part 4 – Create Your Own

# Write a short Python program that:

# Creates at least three variables (a string, an integer, and a float)

# Prints a formatted message using f-strings that combines all three.
#  Example:
movie = "Inception"
rating = 9.5
year = 2010
print(f"My favorite movie is {movie}, released in {year}, rated {rating}/10!")

show = "One piece"
rate = 10
yer = 1998
print (f"My favorite show is {show}, released in {yer}, rated {yer}/10!")