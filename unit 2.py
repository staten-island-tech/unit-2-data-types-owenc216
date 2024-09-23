""" print("Give me a number")
int(input(""))
v = int(input(""))
if v % 2 == 0:
    print('Even')
else:
    print('Odd') """
""" 
print("What was the bill?")
b=int(input(""))
print("how was the service?" " bad, okay, good or great?")
q= input("")

if q == "bad":
    print ("your bill is" ,b*1,  ("no tip included"))

elif q == "okay":
    print ("your bill is" ,b*1.15, ("15% tip included") )

elif q == "good":
    print ("your bill is" ,b*1.20,2 ("20% tip included"))

elif q == "great":

    print ("your bill is" ,b*1.25, ("25% tip included"))

print ("give me a number")
Factors = []

number = int (input(""))
for i in range(number):
    if number % (i+1)==0:
        Factors.append(i+1)

print (Factors)  """

print ("give me a number")
a = int(input(""))
print ("give me another number")
b = int(input(""))

if a > b:
        smaller = b
else:
        smaller = a
for i in range(1, smaller+1):
    if(a, 1 % i == 0) and ( b % i == 0):
        gcf = i


print("the gcf is" , (gcf))
