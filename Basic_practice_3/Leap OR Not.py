def leap(year):
    if(year%4==0):
          if(year%100==0):
                if(year%400==0):
                    print("leap Year")
                else:
                    print("Not a leap Year")
          else:
              print("Leap Year")
    print("Not a Leap Year")

leap(2000)