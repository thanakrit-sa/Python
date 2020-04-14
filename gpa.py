
print('Program Check Grade\n')
name = input('Student name : ')
# grade = int(input('Enter your grade : '))

# while name is not "":
if name is not "":
    print('Hello %s' % name)
    grade = int(input('Enter your grade : '))
    if grade >= 80 :
        print('Grade A')
    elif grade >= 75 and grade <= 79:
        print('Grade B+')
    elif grade >= 70 and grade <= 74:
        print('Grade B')
    elif grade >= 65 and grade <= 69:
        print('Grade C+')
    elif grade >= 60 and grade <= 64:
        print('Grade C')
    elif grade >= 55 and grade <= 59:
        print('Grade D+')
    elif grade >= 50 and grade <= 54:
        print('Grade D')
    else:
        print('Grade F')
    
else:
    print('Plese Enter your name')
