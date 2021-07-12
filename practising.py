import os
import shutil

audio=('wav','mp3','flac')
video=('mp4','wmv','m4a', 'm4v','mov','webm')
text=('doc','pdf','text','txt')
picture=('jpg','png','jpeg','tif')

for i in os.listdir(r'F:\STUDY\Codings\PYTHON CODES\movies'):
    if '.' not in i:
        continue;
    a,b=i.split('.')
    if b.lower() in audio:
        if os.path.exists(r'F:\STUDY\Codings\PYTHON CODES\movies\audio'):
            shutil.move(f'F:\\STUDY\\Codings\\PYTHON CODES\\movies\\{i}',f'F:\\STUDY\\Codings\\PYTHON CODES\\movies\\audio/{i}')
        else:
            os.makedirs(r'F:\STUDY\Codings\PYTHON CODES\movies/audio')
            shutil.move(f'F:\\STUDY\\Codings\\PYTHON CODES\\movies\\{i}',f'F:\\STUDY\\Codings\\PYTHON CODES\\movies\\audio/{i}')
    if b.lower() in video:
        if os.path.exists(r'F:\STUDY\Codings\PYTHON CODES\movies\video'):
            shutil.move(f'F:\\STUDY\\Codings\\PYTHON CODES\\movies\\{i}',f'F:\\STUDY\\Codings\\PYTHON CODES\\movies\\video/{i}')
        else:
            os.makedirs(r'F:\STUDY\Codings\PYTHON CODES\movies/video')
            shutil.move(f'F:\\STUDY\\Codings\\PYTHON CODES\\movies\\{i}',f'F:\\STUDY\\Codings\\PYTHON CODES\\movies\\video/{i}')
    
    if b.lower() in text:
        if os.path.exists(r'F:\STUDY\Codings\PYTHON CODES\movies\text'):
            shutil.move(f'F:\\STUDY\\Codings\\PYTHON CODES\\movies\\{i}',f'F:\\STUDY\\Codings\\PYTHON CODES\\movies\\text/{i}')
        else:
            os.makedirs(r'F:\STUDY\Codings\PYTHON CODES\movies/text')
            shutil.move(f'F:\\STUDY\\Codings\\PYTHON CODES\\movies\\{i}',f'F:\\STUDY\\Codings\\PYTHON CODES\\movies\\text/{i}')
            
    if b.lower() in picture:
        if os.path.exists(r'F:\STUDY\Codings\PYTHON CODES\movies\picture'):
            shutil.move(f'F:\\STUDY\\Codings\\PYTHON CODES\\movies\\{i}',f'F:\\STUDY\\Codings\\PYTHON CODES\\movies\\picture/{i}')
        else:
            os.makedirs(r'F:\STUDY\Codings\PYTHON CODES\movies/picture')
            shutil.move(f'F:\\STUDY\\Codings\\PYTHON CODES\\movies\\{i}',f'F:\\STUDY\\Codings\\PYTHON CODES\\movies\\picture/{i}')
            