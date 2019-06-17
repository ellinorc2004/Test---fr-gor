def addition(x, y):
    print(x+y)
def subtraktion(x, y):
    print(x-y)
def division(x, y):
    print(x/y)
def multiplikation(x, y):
    print(x*y)

print("Välj vad du vill göra?")
print("1. Addition")
print("2: Subtraktion")
print("3. Division")
print("4. Multiplikation")

val = input("Skriv in val (1/2/3/4): ")

num1 = int(input("Skriv det första numret: "))
num2 = int(input("Skriv det andra numret: "))

if val == "1":
    addition(num1, num2)
elif val == "2":
    subtraktion(num1, num2)
elif val == "3":
    division(num1, num2)
elif val == "4":
    multiplikation(num1, num2)
    
