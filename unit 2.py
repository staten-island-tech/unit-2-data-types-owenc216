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
def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = a
num2 = b

print("The GCF is", compute_hcf(num1, num2))



""" number = int(input("give me a number"))
number2= int(input("give me another number"))
Factors = []
Factors = []
gcf = []
for i in range(number):
    if number % (i+1)==0:
        Factors.append(i+1)

Factors2 = []
for i in range(number2):
    if number % (i+1)==0:
        Factors2.append(i+1)

for i in Factors and Factors2:
    Factors.append(i)
print ((gcf))
 """


