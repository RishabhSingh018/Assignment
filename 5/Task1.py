def display_data(Student_data={}):
    while True:
        ch = input("If you want to check the details marks of the student type 'yes' or 'no': ").lower()
        if ch == 'yes':
            search = input("Enter the marks Student's name: ")
            if search in Student_data:
                print(f"{search}'s marks is {Student_data[search]}")
            else:
                print('Student Not found')
        else:
            break
s_data={}
while (True):
    choice=input("If you want to add the details of the students marks type 'yes' or 'no': ").lower()
    if choice=='yes':
        name_of_student=input('Enter the name of the student: ')
        marks_of_student=int(input('Enter the marks of the student: '))
        s_data[name_of_student]=marks_of_student
    else:
        break
display_data(s_data)
    
