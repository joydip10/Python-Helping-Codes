import os

print(os.getcwd()) #returns current working directory
#os.mkdir("Movies/Genre") #creating folder--> no multiple folders
print(os.path.exists("Movies")) # Returns whether the folder Movies preexists or not
#open("file.txt",'a').close()  #creates file

#os.mkdir(r"F:\STUDY\Codings\PYTHON CODES\Movies\Genre\Comedy/hindi")


#os.chdir(r"C:\Users\JOY STARK\Desktop") #changing the current working directory
#print(os.getcwd())


#os.chdir(r"F:\STUDY\Codings\PYTHON CODES")
#print(os.getcwd())

print(os.listdir())

print("\n\n")

for item in os.listdir("C:\\Users\\JOY STARK\\Desktop"):
    print(r"C:\Users\JOY STARK\Desktop"+f"\\{item}")

print("\n\n")

for item in os.listdir():
    print(os.path.join(os.getcwd(),item))
    
print("\n\n")

for item in os.listdir("C:\\Users\\JOY STARK\\Desktop"):
    print(os.path.join("C:\\Users\\JOY STARK\\Desktop",item))