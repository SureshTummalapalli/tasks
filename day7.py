#1.numbers=[25,30,20,40,15,25]
numbers = [25,30,20,40,15,25]
current_sum = 0
for num in numbers:
    current_sum += num
    if current_sum > 100:
        print("sum exceeded 100")
        break 
    else:
     print("sum:", current_sum)

# 2.Problem 2: Using continue in a For Loop
for num in range(1,601):
   if num % 2 == 0:
      continue
   print(num)


# 3.Problem 3: Using pass in Conditional Statements
number = int(input("enetr a number: "))
if number % 2 == 0:
   print("even")
else :
   pass
#Problem 4: Combining Transfer Statements
words = ["hello", "break", "world", "skip", "script"]
for word in words:
   if word == "break":
      break
   elif word == "skip":
      continue
   print(words)