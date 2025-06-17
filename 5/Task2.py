list_number=[]
for i in range(1,11):
    list_number.append(i)
print("Original list: ",list_number)
extractrd_list=list_number[0:5]
print("Extracted First Five elements: ",extractrd_list)
reversed_list=extractrd_list[::-1]
print("Reversed extracted list: ",reversed_list)