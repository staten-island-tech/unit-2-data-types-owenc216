""" print("Give me a number")
int(input(""))
v = int(input(""))
if v % 2 == 0:
    print('Even')
else:
    print('Odd') """

print("What was the bill?")
b=int(input(""))
print("how was the service?" " bad, okay, good or great?")
q= input("")

if q == "bad":
    print ("your bill is" ,b*1,  ("no tip included"))

elif q == "okay":
    print ("your bill is" ,b*1.15, ("15% tip included") )

elif q == "good":
    print ("your bill is" ,b*1.20, ("20% tip included"))

elif q == "great":

    print ("your bill is" ,b*1.25, ("25% tip included"))

