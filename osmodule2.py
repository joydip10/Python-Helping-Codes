import os
import shutil

print(os.walk('C:\\Users\\JOY STARK\\Desktop')) #It goes deep down the files and folders inside the files and folder and its an iterator

for current_path,folder_names,file_names in os.walk(os.getcwd()):
    print(f"Current Path: {current_path}")
    print(f"Folder names: {folder_names}")
    print(f"File names: {file_names}")
    print("\n")

print(os.getcwd())    
#os.rmdir("F:\STUDY\Codings\PYTHON CODES"+r"\Movies") #won't delete the folder movies , since it isn't empty
#os.rmdir("F:\STUDY\Codings\PYTHON CODES"+r"\Movies\Genre\Comedy")

os.makedirs('news/movies/genre/comedy/hulchul') #for creating multiple folders

#shutil.rmtree('new\movies') #this deletes the folders with inner folders but doesn't send to the recycle bin i.e. parmanent deletion

#shutil.copytree(r'F:\STUDY\Codings\PYTHON CODES\Movies','C:\\Users\\JOY STARK\\Desktop/mov') #copying a folder to another path

os.makedirs("C:\\Users\\JOY STARK\\Desktop/mov/pictures")
#shutil.copy(r'F:\STUDY\Codings\PYTHON CODES\new\movies\genre\comedy\hulchul\hulchul.mp4','C:\\Users\\JOY STARK\\Desktop\\mov\\comedy/hulchul.mp4')

#shutil.move(r'F:\STUDY\Codings\PYTHON CODES\new\movies\genre\comedy\hulchul\hulchul.mp4','C:\\Users\\JOY STARK\\Desktop\\mov/newmovie.mp4')
#used to move files and folders
shutil.move(r'F:\STUDY\Codings\PYTHON CODES\new\picture_Files\download.jpg','C:\\Users\\JOY STARK\\Desktop\\mov\\pictures/newpicture.jpg')
