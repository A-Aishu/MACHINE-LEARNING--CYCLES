fPtr =open('Sample_1.txt', 'x')


fPtr.write("New file has created!")
fPtr.close()


fPtr = open('Sample_1.txt', 'r')
print('The content of Sample_1.txt is: ')
print(fPtr.read())
fPtr.close()
