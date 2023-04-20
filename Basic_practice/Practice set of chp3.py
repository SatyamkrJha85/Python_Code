# write a program to display a user entered name followed by Good Afternoon using input() function
'''a=input("Enter your name \n")
print(a,"good afternoon")'''

# Write a program to fill in a letters templete given below with name and date.
letter=''' Dear <|name|>,
Greeting from ABC coding house . I am happy to tell you about your selection have a 
great day ahead! 
thanks and regard below. 
Date: <|date|>
'''
'''name=input("enter your name ")
date=input("enter your date")
letter=letter.replace("<|name|>",name)
letter=letter.replace("<|date|>",date)
print(letter)'''

# Write a program to delect double spaces in a string
k='''and happy to see you here my name is satyam jha and i am a student in techno india university and i just
to tell your about my self because the communication is very important to knowing each other in this field
so i am a student to pursuing bca in kolkata because my state does not given many oppurtunity to grow 
my self in their so i choose kolkata for compliting my drgree here and many more other excuses . thanks you so much 
  for giving this oppurtunity regard and loves '''
print(k)
print(k.find("  "))

# replace the double space from problem 3 with single space.
d="hello   buddy what's is your   today's plan "
print(d.replace("  ",""))

# wap to format the following letter using escape sequence characters .
# letter= "Dear harry , This python course is nice. thanks!"

letter= "Dear harry , \nThis python course is nice.\nthanks!"
print(letter)

