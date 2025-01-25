#error handling
#Zero division error and Value error
a=int(input("Enter a number : "))
b=int(input("Enter b number : "))
print(a+b)
print(a-b)
try:
	print(a/b)
except ZeroDivisionError as e:
	print("error occured")
print(a*b)
print(a**b)
print(" -"*15)
# Index error
list=[1,2,3,4,5]
print(list[0])
try:
	print(list[5])
except IndexError as e:
	print("No indexing for that number")
print(list[3])
print(" -"*15)
#Type error
c=4
d='g'
try:
	print(c+d)
except TypeError as e:
	print("interger and string can't be concatinate")
print("- "*15)
#Value error
f='hi hello'
try:
	print(int(f))
except ValueError as obj:
	print(f"exception: {obj}")
	print("string can't be a interger if its a number it can be change")
print()
#name error
name='hi'
try:
	print(nam)
except NameError as n:
	print(f"variable error do you mean name?")
	print(f"{n}")
print()
#key error
dict={'a':1,'b':2,'c':3}
try:
	print(dict['o'])
except KeyError as og:
	print(f"exception: {og}")
finally:
	print("Thank you")