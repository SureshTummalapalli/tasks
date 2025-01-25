set1={1,2,3,4,5}
set2={4,5,6,7,8}

print(set1.intersection(set2))#setintersection
print(set1.union(set2))#setunion
print(set1.difference(set2))#set difference
print(set1.symmetric_difference(set2))#set symmetric_difference

#set membership test

my_set = {1,2,3,4,5}
print(3 in my_set)

print("_"*25)
print()

# set intersection, set union, set difference & set symmetric difference.
#students names in two different colleges

college1={"Anji","Suresh","Prakash","Upender","Mahesh"}
college2={"Hareesh","Anjan","Kalyan","Suresh","Prakash"}
print(college1.intersection(college2))
print(college1.union(college2))
print(college1.difference(college2))
print(college1.symmetric_difference(college2))

print()
print(""*8,"Tuple",""*8)
print()
#create a tuples

details=("suresh","28","maroon")
print(details)

print()
#Access tuple elements

days_of_the_week=("sunday","monday","tuesday","wednesday","thusday","friday","saturday")
print(days_of_the_week[2])

print()
#tuple concatenation

odd=(1,3,5)
even=(2,4,6)
print(odd+even)

print()
#tuple unpacking

dimension_of_rectangle=(3,4)
width,length=dimension_of_rectangle
area_of_the_rectangle=width*length
print(area_of_the_rectangle)

print()
#check if an element exists
data=(1,2,3,4,5,6)
print(4 in data)

print()

items=[("Apple",99), ('Banana',99), ('Milk',49)
]
print("item       price")
print("-"*20)
total=0
for i,j in items:
#	j=float(j)
	print(f"{i}      {j:.2f}")
	total+=j
print("-"*20)
print(f"total       {total:.2f}")