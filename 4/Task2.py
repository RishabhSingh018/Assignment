def write(filename):
    with open(filename,'w') as file:
        content=input('Enter the text: ')
        file.write(content)
        print("Data is successfully writen to", filename)
def append(filename):
    with open(filename,'a') as file:
        append_data=input('Enter addtional text to append: ')
        file.write(append_data)
        print("Data Succesfully appended")
def read(filename):
    with open(filename,'r') as file:
        print("Final Content of", filename)
        content=file.read()
        print(content)
choice=int(input('Enter 1->Read:\n2->Write:\n3-Append:'))
if choice==1:
    read('output.txt')
elif choice==2:
    write('output.txt')
elif choice==3:
    append('output.txt')
else:
    print('Enter valid choice')