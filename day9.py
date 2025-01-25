#  Problem: You are given a string sentence . Print the characters at even indices.

sentence = "Python is amazing"
print(sentence[::2]) #This is going to print characters at even indices like (0,2,4,6 etc)

#Problem:You are given a string s . Replace all spaces in the string with underscores ( _ )and print the modified string.
s = "Python is fun and powerful"
print(s.replace(' ','')) # This is going to check for spaces and replace with Underscores()

#Problem: You are given a string s . Check if the string contains only digits.

s = "12345"
if s.isdigit():
    print(f"{s} contains only digits")
else:
    print(f"{s} doesn't contains only digits")

#Problem: You are given a string s . Print the string in reverse order.
s = "Python is amazing"
print(s[::-1])#negative indexing starts from -1. So prints in reverse

#Problem:You are given a string s . Capitalize the first letter of each word in the string and print the modified string.

s = "python programming is fun"
joined_string = []
split_str = s.split(" ") # Splitting string by space 
for i in split_str:
    joined_string.append(i.capitalize()) # capitalizing each word
capitalized_string = " ".join(joined_string) # Joining each string
print(capitalized_string)

#**another way***
print(s.title()) # This is going to capitalize first letter in each word