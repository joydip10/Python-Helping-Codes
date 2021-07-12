with open("file.txt",'r') as rf:
    with open("file1.txt",'w') as wf:
        data=rf.read()
        wf.write(data)
        
        
        
with open('file1.txt','r') as r:
    print(r.read())