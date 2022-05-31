a=int(input("Enter first number : "))
b=int(input("Enter second number : "))

print('''
choices
1. Add
2. Subtract
3. Multiplication
4. Divide
''')

choice=int(input("Enter the choice : "))

if choice==1:
    print("Result : ", a+b)
elif choice==2:
    print("Result : ", a-b)
elif choice==3:
    print("Result : ", a*b)
elif choice==4:
    print("Result : ", a/b)
else:
    print("Invalid choice")
