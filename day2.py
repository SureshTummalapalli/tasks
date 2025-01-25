#1
print("Suresh")
# 2.
'''
 Create a Python script with both single-line and multi-line comments 
explaining the purpose of the script.'''
print('welcome') # '#- is a single line comment' here can write the code purpose or any informations in one line
'''We have multiline comments it is used for 
incase we have more than line of code information than we use this comments '''
# 3. Define a list containing three different data types 
list=[1,1.5,'hi']# int,float,string three datatypes in list
print(list)
# 4.String Operations:
name='hi'
name1='hello'
print(name+name1) # here 2 variables between '+' is a concatenation
na='go'
print(na*3) # here 2 variables between '*' is a repeatation
# 5.Python Keywords:
# for = 'bi'
# print(for)
# 6.Declare two variables, one storing an integer and the other a string. 
# Print their values
a=10
b='ram'
print(a,b)

# 7. Type Conversions:
d=5
e=int(d) #Convert a float to an integer and print the result.
print(e)
print(type(e))
f=str(e) #Convert an integer to a string and display the output.
print(f)
print(type(f))
#8.Take the user's age as input and print a message using that input.
age=int(input('Enter your age : '))
print(f'your age is {age}')
#9.Write a program that prints a pattern using multiple print statements.
print('*')
print('**')
print('***')
print('****')
print('*****')
#10.A Python script for a simple task and adding comments to each step
num1 = 6#assigned a value to the varaible
num2 = 8#assigned a value to the variable
result = num1 + num2
print(result)
"""


to perform addition of numbers
first we have to take two variables and assign values to each variable 
use addition operator in between two varaibles 
lastly we have use print statement to display the result on the screen
 

"""

#11.Implement a program that uses a dictionary to store information about a book
book_details = {
    "title" : "python",
    "author" : "guido vanrossum" ,
    "publication year" : 1991
}
print(book_details)

#12.Write a python program that takes a string as input 35 and return float value
id= "35"
float_conversion = float(id)
print(float_conversion)

#13.Explore three Python keywords not mentioned earlier and provide examples of how they are used.
#used to represent boolean values
x = True
y = False
print(x and y)
 
#Using conditional statements

num1 = 5
num2 = 4
if num1 > num2 :
   print("True")
else :
   print("False")

#14. Develop a script that swaps the values of two variables without using a temporary variable.
person1 = "suresh"
person2 = "anji"
person1 , person2 = person2 , person1
print("person1 =" , person1)
print("person2 =" , person2)

# 15.Create a program that takes user input for their age, converts it to an integer, adds 5, and then prints the result.
your_age = input("Enter your age : ")
int_conv = int(your_age)
print(int_conv + 5 )

#16.Build a calculator program that takes two numbers as input and performs the arithmetic operation 
num_1 = int(input("enter the number1 : "))
num_2 = int(input("enter the number2 : "))
result_add = num_1 + num_2
result_sub = num_1 - num_2
result_mul = num_1 * num_2
print("addition " , result_add)
print("subtraction " , result_sub)
print("multiplication" , result_mul)