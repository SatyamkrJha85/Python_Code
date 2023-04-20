myDist={
    "fast": "In a quick manner","Satyam": "A Coder",
    "marks":[1,2,4],"hlw":{"seraa": "sanbidhan"},"number":[45,34,53]
}
print(myDist['fast'])
print(myDist['Satyam'])
print(myDist['marks'])

# Nested Disctionary
'''satya={
    "hlw":{"seraa": "sanbidhan"}
}'''

print(myDist['hlw'] )
#print(satya['serra'])
print(myDist['number'])

# we can change the any specific value example and it is mutable
myDist["serra"]=[4,3,2]
print(myDist["serra"])