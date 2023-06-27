
x = 'The quick Brow Fox'
upper_case = 0
lower_case = 0
for i in x:
    if i.isupper():
        upper_case +=1
    elif i.islower():
        lower_case +=1
print("No of upper case:",upper_case)
print("No of lower case:",lower_case)