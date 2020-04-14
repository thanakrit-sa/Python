
# print('Program Check Grade\n')
# name = input('Student name : ')
# # grade = int(input('Enter your grade : '))

# # while name is not "":
# if name is not "":
#     print('Hello %s' % name)
#     grade = int(input('Enter your grade : '))
#     if grade >= 80 :
#         print('Grade A')
#     elif grade >= 75 and grade <= 79:
#         print('Grade B+')
#     elif grade >= 70 and grade <= 74:
#         print('Grade B')
#     elif grade >= 65 and grade <= 69:
#         print('Grade C+')
#     elif grade >= 60 and grade <= 64:
#         print('Grade C')
#     elif grade >= 55 and grade <= 59:
#         print('Grade D+')
#     elif grade >= 50 and grade <= 54:
#         print('Grade D')
#     else:
#         print('Grade F')
    
# else:
#     print('Plese Enter your name')

# name_student = input('Enter your name : ')

# if name_student != "":
#     if name_student.isalpha() == True:
#         print('Hello %s' % name_student)
#         grade_student = int(input('Enter your score : '))
#         print('You score = %d' % grade_student)
#         if grade_student >= 80 :
#             print('Grade A')
#         elif grade_student >= 75 and grade_student <= 79:
#             print('Grade B+')
#         elif grade_student >= 70 and grade_student <= 74:
#             print('Grade B')
#         elif grade_student >= 65 and grade_student <= 69:
#             print('Grade C+')
#         elif grade_student >= 60 and grade_student <= 64:
#             print('Grade C')
#         elif grade_student >= 55 and grade_student <= 59:
#             print('Grade D+')
#         elif grade_student >= 50 and grade_student <= 54:
#             print('Grade D')
#         else:
#             print('Grade F')
#     else:
#         print('Format "a-z A-Z"')
# else:
#     print('Plese enter your name')

data_student = []
data_score = []

count = int(input('Enter your count student : '))

i = 1
while i <= count:
    name_student = input('Enter your name %d: ' % i)
    score_student = int(input('Enter your score %d: ' % i))

    data_student.append(name_student)
    data_score.append(score_student)
    i = i+1

x = 0
while x <= len(data_score)-1:
    if data_score[x] >= 80:
        print('Name : {0} Score : {1} Grade : A'.format(data_student[x],data_score[x]))
    elif data_score[x] >= 75 and data_score[x] <= 79:
        print('Name : {0} Score : {1} Grade : B+'.format(data_student[x],data_score[x]))
    elif data_score[x] >= 70 and data_score[x] <= 74:
        print('Name : {0} Score : {1} Grade : B'.format(data_student[x],data_score[x]))
    elif data_score[x] >= 65 and data_score[x] <= 69:
        print('Name : {0} Score : {1} Grade : C+'.format(data_student[x],data_score[x]))
    elif data_score[x] >= 60 and data_score[x] <= 64:
        print('Name : {0} Score : {1} Grade : C'.format(data_student[x],data_score[x]))
    elif data_score[x] >= 55 and data_score[x] <= 59:
        print('Name : {0} Score : {1} Grade : D+'.format(data_student[x],data_score[x]))
    elif data_score[x] >= 50 and data_score[x] <= 54:
        print('Name : {0} Score : {1} Grade : D'.format(data_student[x],data_score[x]))
    else:
        print('Name : {0} Score : {1} Grade : F'.format(data_student[x],data_score[x]))
    
    x = x+1
    
    

        



