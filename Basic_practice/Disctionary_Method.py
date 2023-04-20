myDist={
    "fast": "In a quick manner","Satyam": "A Coder",
    "marks":[1,2,4],"hlw":{"seraa": "sanbidhan"},"number":[45,34,53],1: 234
}
# Discotionary method
print(len(myDist))
print(type(myDist))
print(myDist.values()) # prints the value of the dictionary
print(myDist.keys()) # prints the value of the dictionary
print(myDist.items()) # prints the (keys and value) for all item of the dictionary
mynewdist={"hello":"just a formality","hi":"just a sending"}
myDist.update(mynewdist)
print(myDist)

# update function uses is add new string in privious string
hi={"show": "sunn","hi": "toto"}
hlw={"no":"hunda","shi":"shie"}
hi.update(hlw)
print("updated hi is ",hi)

print(myDist.get("marks2"))
print(myDist.get("marks"))