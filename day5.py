#exercise 1
vowel = input("enter vowel")
if vowel in "aeiou":
    print(f"you have entered {vowel} and it is a vowel character from letters")
else:
    print(f"you have entered {vowel} and it is a non vowel letter")

#exercise 2
user_age = int(input("your age: "))
if user_age >= 0 and user_age <= 12:
    print("you are a child")
elif user_age >= 13 and user_age <= 17:
    print("you are a teenager")
elif user_age >= 18 and user_age <= 64:
    print("you are an adult")
else:
    print("you are an senior")

#exercise 3
number = int(input("enter number: "))
if number > 0:
    print("you have entered positive value")
elif number < 0:
    print("you have entered negative number")
else:
    print("you have entered zero")

#exercise 4
year = int(input("year: "))
if year%4 == 0 or year%100 != 0 and year%400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#exercise 5
number1 = int(input("num_1: "))
number2 = int(input("num_2: "))
operator = input("arthematics operation:")

if operator == "+":
    print (number1+number2)
elif operator == "-":
    print (number1-number2)
elif operator == "/":
    print(number1/number2)
elif operator == "*":
    print(number1*number2)

#exercise 6
#x=9
x = int(input("enter_number: "))
print('even' if x%2==0 else 'odd') #dynamic data

print("even" if 8%2==0 else "odd") #static data

#exercise 7
price = int(input("price of an item: "))
discount = int(input("discount given by store: "))
discount_percent = discount/100*price 
final_price = price - discount_percent
print (final_price)

#exercise 8
weight = int(input("your weight(kg): "))
height = float(input("your height(m): "))
BMI = weight/(height**2)
print (BMI)