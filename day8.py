#task1
#reverse the given list
list=[10,20,30,40,50,11]
list.reverse()
print(list)

#task2.common elements
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
list3=[]
for i in list1:
    if i in list2:
     list3.append(i)
print(list3)

#task3.unique elements and task4.remove duplicates from the list 
origin_list=[1,2,2,3,4,4,5]
unique_list=[]
for i in origin_list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)

#execise1.list concatenation
list=[1,2,3,4,5]
list1=[6,7,8,9,10]
list2=list+list1
print(list2)

#exercise3.remove elements at even indices
list=[2,3,4,5,6,7,8,9,1]
list1=[]
for i in list:
    if i in list[0:9:2]:
       list1.append(i)
print(list1)

#exersice2.list repetation
list=[1,2,3,4,'anji',(1,2,3,4,5)]
result=list*3
print(result)

#4list insertion
list=[13,14,15,16,17,18]
list.insert(0,10)
list.insert(1,11)
list.insert(2,12)
print(list)

#list comprehensions
#square numbers
print([i**2 for i in range(11)])

#even numbers
print([i for i in range(21) if i%2==0 ])

#length method
words=["apple","banana","cherry","date"]
print([len(word) for word in words])