#To print the positive nos. in a list

#first we created a list

list=[]
n=int(input("Input the length of list "))
for i in range(0,n):
	print("Enter the number ")
	element=int(input())
	list.append(element)
print("The list is",list)

#now we print the positive numbers in list
print("Following are the positive nos. in above list")
for i in list:
	if i>=0:
		print(i)
