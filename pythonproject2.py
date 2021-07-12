import os,shutil
dictionary={
'audio_extension':('mp3','m4a','wav','flac'),
'video_extension':('mp4','mkv','MKV','flv','mpeg'),
'document_extension':('doc','pdf','txt'),
'picture_extension':('jpg','jpeg','png','bmp','gif')
}

path=input('Enter the desired path: ')
def file_finder(folderpath,file_extension):
    return [ file for file in os.listdir(folderpath) for ex in file_extension if file.endswith(ex)]


for extension,extension_tuples in dictionary.items():
    foldername=extension.split('_')[0]+'_Files'
    folderpath=os.path.join(path,foldername)
    if not os.path.exists(folderpath):
        os.mkdir(folderpath)
    for item in file_finder(path,extension_tuples):
        itempath=os.path.join(path,item)
        itemnewpath=os.path.join(folderpath,item)
        shutil.move(itempath,itemnewpath)
        