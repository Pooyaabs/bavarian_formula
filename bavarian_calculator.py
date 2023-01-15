#Take input from user 
a = int(input("Enter the maximum score in the grading system: "))
b = int(input("Enter the minimum score in the grading system: "))
c = int(input("Enter the current grade of the student: "))

#Calculate the bavarian formula
result = (a-c/a-b)*3+1

#Print the result
print("The result of the Bavarian formula is: ", result)
