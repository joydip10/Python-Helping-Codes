f=open('textfile.txt','r',encoding="utf-8")  #open function
print(f"Cursor position: {f.tell()}") #tell function() to tell the cursor's current position
print(f.read())   #read function
print(f"Cursor position: {f.tell()}\n")
f.seek(0) #seek function moves the cursor position at user's choice
print(f"Cursor position: {f.tell()}")
print(f.read())    # this will not work without seek(0) since the cursor is at the end of the file
print(f"Cursor position: {f.tell()}")


print("\n\nReadLine method: ")
f.seek(0)
print(f.readline())  #Readline method reads the text file line by line
print(f.readline())
print(f.readline())




print("\n\n\nReadLines Method:")
f.seek(0)
lines=f.readlines()
for i in lines:
    print(i)
print(lines)
print(f"Number of lines: {len(lines)}")



print(f"Name of the file : {f.name}")
print(f"Our file is closed? is it ?: {f.closed}")
f.close() #close function

print(f"Our file is closed? is it ?: {f.closed}")



#withblock-> contex manager
with open('textfile.txt','r',encoding="utf-8") as r:
    print(r.encoding)
    data=r.read()
    #print(data)
    for i in data:
        print(i,end='')



