# stores name and corresponding salaries
salary = {"raj" : [(50000, 10), (25000, 15)], "striver" : [(55000, 10), (15000, 15), (3000, 2)], "vikram" : [(52000, 10), (15000, 15)]}
salary2 = {"raj" : 50000, "striver" : 60000, "vikram" : 5000}
lenses = {0: ['rn', 1, 'cm', 2], 1: ['qp', 3], 3: ['pc', 4, 'ot', 9, 'ab', 5, 'pc', 6, 'ot', 7]}
 
# stores the salaries only
list1 = list(zip(*salary.values()))[0]
list2 = list(salary2.values())
print(list1)
print(list2)

list3 = list(zip(*salary["striver"]))
list4 = lenses[3]

print(list3)
print(list4)

if 'ab' in list4:
    index = list4.index('ab')
    list4[index+1] = 7
print(list4)