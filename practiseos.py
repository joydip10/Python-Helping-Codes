import os

print(os.getcwd())
#os.mkdir(r'Folders\\Fold')
#os.chdir(r"C:\Users\JOY STARK\Desktop")
print(os.path.exists(r"C:\Users\JOY STARK\Desktop"))
#for i in os.listdir():
#    print(os.path.join(os.getcwd(),i))

for c,f,fl in os.walk(os.getcwd()):
    print(c)
    print(f)
    print(fl)
    
#os.rmdir(r'Folders\Fold')
#os.makedirs('Folders\\movies\\Thrillers\\Korean')
import shutil
shutil.copytree(r"Folders\movies",'C:\\Users\\JOY STARK\\Desktop/mov/newmov/thrill')
shutil.copy(r"Folders\movies\movielist.txt",'C:\\Users\\JOY STARK\\Desktop/mov/newmov/thrill/new.txt')
