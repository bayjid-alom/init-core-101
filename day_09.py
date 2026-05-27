# Boolean (True/False)  <-- (First letter capital)

overEighteen = True
print(type(overEighteen))    #<class 'bool'>

isMarried = False
print(type(isMarried))   #<class 'bool'>


x = 20
y = 15
if(x>y):
    print("x is greater than y")
else:
    print("x is less than y")


A = 10
B = 15
print(A == B)     # False


# ------------Part 9.1 --------------
# python string formatting
# prop: string er vitore mathematical kaj korte (f") dite hobe.  " all work in quotation " 
# Just for mathematical work


num1 = 20
num2 = 30
print(f"This is my super number: {num1 + num2} ")


username = "Bayjid Alom Jihad"
roll_no = "85241009"
print(f"My name is {username} & roll no is: {roll_no}")