#mode of writing: w,a,r+
#w mode should be used only on an empty file. Because if w mode is used the content of the file will be removed and new contents would be added
#w mode can also be used to create files 

#with open("file.txt",'w') as f:
#    f.write("Detective")
    
#append mode appends the string written to the existing string on the file
#it can also create files if not existing
#with open("file.txt","a") as f:
#    f.write("Sherlock Holmes")


#This mode overrides the data -> to solve this we can use the seek method to move the cursor at the end of the file
#this mode doesn't create any new files
with open("file.txt","r+") as f:
    f.seek(len(f.read()))
    f.write("\nIs he a Satyaneshi of West? ")
    
    
    