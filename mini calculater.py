print("=" * 40)
print("                      CALCULATER                  ")
print("=" * 40)
a = int(input("Enter your number a: "))
b = int(input("Enter your number b: "))
print("Operation [ + , - , * , / ] ")
operation = input("Enter your opration")
if operation == "+":
  add = a + b
  print("Addition of number",a ,"and", b,"is : ", add)
elif operation == "-":
  sub = a - b
  print("Subtraction of number", a, "and" , b,"is : " , sub)
elif operation == "*":
  mult = a*b
  print("Multiplaction of number", a, "and", b,"is : ", mult)
elif operation == "/":
  div = a/b
  print("Divisition of number", a, "and", b,"is : ", div)
else:
  print("INVILADE OPERATION")
  
