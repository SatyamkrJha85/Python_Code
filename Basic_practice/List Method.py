a=[3,4,5,2,53,32]
print("before sorting : ",a)
# sort the list in assending order
a.sort()
print("After sorting : ",a)
# reverse or sort the list in desending order
a.reverse()
print("Reverse is : ",a)
a.append(8) # Add to the element end of the list
print("Add 8 in this list ",a)
a.append(45)
print("Add 45 in this list ",a)

# Add element in specific place or index
a.insert(1,34)
print("the updated list is ",a) #add 34 in 1st index

#Deleted element from specific index :
a.pop(2) # deleted element from 2nd index
print("after deleting element and updated list is :",a)

# Delted specific element given by the user
a.remove(45)
print("delete given element : ",a)

