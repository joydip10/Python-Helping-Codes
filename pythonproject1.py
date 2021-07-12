import os,shutil

dictionary={
'audio_extension':['mp3','m4a','wav','flac'],
'video_extension':['mp4','mkv','MKV','flv','mpeg'],
'document_extension':['doc','pdf','txt']
}

path=input('Enter the folder path: ')

for item in os.listdir(path):
    if item.endswith('mp3') or item.endswith('m4a') or item.endswith('wav') or item.endswith('flac'):
        file,extension=item.split('.')
        if os.path.exists(path+'\\audio'):
            shutil.move(f'{path}\\{item}',f'{path}\\audio/{item}')
        else:
            os.mkdir(f'{path}/audio')
            shutil.move(f'{path}\\{item}',f'{path}\\audio/{item}')
            
    if item.endswith('mp4') or item.endswith('mkv') or item.endswith('MKV') or item.endswith('flv') or item.endswith('mpeg'):
        file,extension=item.split('.')
        if os.path.exists(path+'\\video'):
            shutil.move(f'{path}\\{item}',f'{path}\\video/{item}')
        else:
            os.mkdir(f'{path}/video')
            shutil.move(f'{path}\\{item}',f'{path}\\video/{item}')
            
    
    if item.endswith('doc') or item.endswith('pdf') or item.endswith('txt'):
        file,extension=item.split('.')
        if os.path.exists(path+'\\text'):
            shutil.move(f'{path}\\{item}',f'{path}\\text/{item}')
        else:
            os.mkdir(f'{path}/text')
            shutil.move(f'{path}\\{item}',f'{path}\\text/{item}')
            

    if item.endswith('jpg') or item.endswith('png') or item.endswith('jpeg') or item.endswith('bmp') or item.endswith('gif'):
        file,extension=os.path.splitext(item)
        if os.path.exists(path+'\\pictures'):
            shutil.move(f'{path}\\{item}',f'{path}\\pictures/{item}')
        else:
            os.mkdir(f'{path}/pictures')
            shutil.move(f'{path}\\{item}',f'{path}\\pictures/{item}')
    
        