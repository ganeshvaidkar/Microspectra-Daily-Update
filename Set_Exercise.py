#Add a list of elements to a given set
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleSet.update(sampleList)
print(sampleSet)

#Return a set of identical items from a given two Python set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))

#Returns a new set with all items from both sets by removing duplicates
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))

#Given two Python sets, update first set with items that exist only in the first set and not in the second set.
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(set1)

#Remove 10, 20, 30 elements from a following set at once
set1 = {10, 20, 30, 40, 50}
set1.difference_update({10,20,30})
print(set1)