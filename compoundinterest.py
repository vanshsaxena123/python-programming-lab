P=int(input("enter the principle amount"))
R=int(input("enter the rate"))
T=int(input("enter the time"))
cp=P*((1+R/100)**T)
A=P+cp 
print(f"the compound interest is {cp} and the total amount is {A}")
