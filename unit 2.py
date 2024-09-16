""" print("Give me a number")
int(input(""))
v = int(input(""))
if v % 2 == 0:
    print('Even')
else:
    print('Odd')
 """
print("What was the bill?")
b=int(input(""))
print("how was the service?" " bad, okay, good or great?")
q= input("")

if q == "bad":
    print ("your bill is" ,b*1,  ("no tip included"))

if q == "okay":
    print ("your bill is" ,b*1.15, ("15 percent tip included") )

if q == "good":
    print ("your bill is" ,b*1.20, ("20 percent tip included"))

if q == "great":
    print ("your bill is" ,b*1.25, ("25 percent tip included"))