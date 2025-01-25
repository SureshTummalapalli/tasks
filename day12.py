#1.Add function
def add(a,b):
	return a+b
c=add(3,5)
print(c)
print()
#2.Square function
x=int(input("Enter a number of x : "))
def square(x):
	return x**2
y=square(x)
print(f"The suare of {x} is : ", y)
print()
#3.Factorial function
#pending
#4.Maximum function
def maximum(list):
	print(f"the maximum number in the list is: ",max(list))
list=[52,28,94,48,66]
maximum(list)
print()
#5.Reverse function
def reverse(name):
	print(name[::-1])
name=input("Enter your name : ")
reverse(name)
print()
"""
#6.prime function
#pending
def is_prime(num):
	if num<=1:
		print(f"{num} is : False")
	else:
		for i in range(2,num+1):
			if (num%i)==0:
					print(f"{num} is : False")
					break
		else:
				print(f"{num} is : True")
num=int(input("Enter the number : "))
is_prime(num)
print()#Mistake """

#7.Fibonacci function
def fibonacci(n):
	num1=0
	num2=1
	if n<0:
		print("Enter a valid number")
	elif n==0:
		print(num1)
	elif n==1:
		print(num2)
	else:
		for i in range(2,n+1):
			num3=num1+num2
			num1=num2
			num2=num3
		print(num3)
n=int(input("Enter a positive number : "))
a=fibonacci(n)
print()
#8.Palindrome Function
def is_palindrome(Name):
	if name==name[::-1]:
		print("True")
	else:
		print("False")
name = input("Enter your name : ")
is_palindrome(name)
print()
#9.sum of squares function
def sum_of_squares(list1):
	total=0
	for i in list1:
			sum=i**2
			total+=sum
	print(f"The sum_of_squareses is : {total}")
list1=[2,3,4,5]
sum_of_squares(list1)
#Average function
def AVerage(list2):
	total = 0
	for i in list2:
		total +=i
		avg=total/len(list2)
	print(avg)
list2=[2,3,3,5,7]
AVerage(list2)