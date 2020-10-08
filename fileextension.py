filename = input("input the filename: ")
index=0
for i in range(len(filename)):
    if filename[i]=='.':
        index=i
if(filename[index+1: ]=='py'):
    print("python")
else:
    print(filename[index+1: ])        
