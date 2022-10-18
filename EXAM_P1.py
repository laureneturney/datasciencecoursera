# Lauren Turney
# Python Exam
# Problem 1

salary = int(input("Enter the beginning salary: "))
#put the original input as starting salary
starting_salary = salary
#for 5 years starting at year 1 (while i < 6), multiply by the 1.04 multiple
#to increase by 104% from previous year's salary
i = 1 
multiple = 1.04
while i < 6:
    salary = salary*multiple
    i += 1

#just get the decimal from the percent change
change_multiple = ((salary/starting_salary)-1)*100
percent_change = round(change_multiple, 2)

#round the new salary to two decimals
new_salary = round(salary,2)

print("${:,.2f}".format(new_salary))
print(f"Change: {percent_change}%")



