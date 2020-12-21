# Print multiplication table of given number

n=2
for i in range(0,11,2):
    product= n*i
    print(product)

#Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for item in list1: 
    if(item > 150):break
    if(item % 5 == 0):print(item)   
    
# Reverse the following list using for loop

list2 = [10, 20, 30, 40, 50]
start=len(list2)-1
stop=-1
step=-1
for i in range(start,stop,step):
    print(list2[i],end=' ')


#Display -10 to -1 using for loop

for i in range(-10,0,1):
    print(i)

#Prime numbers between 25 and 50 are:29,31,37,41,43,47

start=25
end=49

for num in range(start,end + 1):
    if num > 1:
        for i in range(2,num):
            if(num % i == 0):
                break
        else:
                print(num,end=' ')

# Use a loop to display elements from a given list which are present at even positions

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in my_list[1::2]:
    print(i,end=' ')

#Find the sum of the series 2 +22 + 222 + 2222 + .. n terms    

number_of_terms = 5
start = 2
sum = 0
for i in range(0,number_of_terms):
    print(start,end=' ')
    sum += start
    start = (start * 10) + 2
print(sum)