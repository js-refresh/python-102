age = (5, -7, 10, -50)
mult_numbers = [index * 5 for index in age]
print(mult_numbers)


#HELP!
age = [5, -7, 10, -50]
multi_list = []
counter = 0
while counter < len(age):
    age.append((age[counter])*4)
    counter +=1

print