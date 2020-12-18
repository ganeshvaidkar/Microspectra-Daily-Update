#Given a Python list you should be able to display Python list in the following order

aLsit = [100, 200, 300, 400, 500]
aLsit=aLsit[::-1]
print(aLsit)

#Concatenate two lists index-wise

list1 = ["M", "na", "i", "Gan"] 
list2 = ["y", "me", "s", "esh"]
List3 = [i + j for i, j in zip(list1 , list2)]
print(List3)

#Given a Python list. Turn every item of a list into its square

aList = [1, 2, 3, 4, 5, 6, 7]
square = [x * x for x in aList]
print(square)

#Concatenate two lists in the following order

list1 = ["Hello ", "Ganesh "]
list2 = ["Hi", "Rajat"]
# list3 = ["Hi", "Ganesh"]
list4 = [x + y for x in list1 for y in list2 ]
print(list4)

#Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x ,y in zip (list1 , list2[::-1]):
	print(x,y)

#Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
newlist =  list (filter(None,list1))
print(newlist)	

#Add item 7000 after 6000 in the following Python List

list1 = [10, 20,30, [300, 400, [5000, 6000], 500],40,50]
list1 [3][2].append(7000)
print(list1)

# Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the following list

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
Sub_List = ["h", "i", "j"]
list1[2][1][2].append(Sub_List)
print(list1)

#Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] = 200
print(list1)

#Given a Python list, remove all occurrence of 20 from the list

list1 = [5, 20, 15, 20, 25, 50, 20]
def removeValue(sampleValue,val):
		return[value for value in sampleValue if value != val]
newList = removeValue(list1,20)
print(newList)