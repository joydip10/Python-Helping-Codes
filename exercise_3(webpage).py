with open("htmlfile.txt",'r') as rf:
    with open("output.txt",'a') as wf:
        
        data=rf.read()
        
        link=True
        
        while link:
            pos=data.find("<a href=")
            if pos==-1:
                break
            else:
                pos1=data.find("\"",pos)
                pos2=data.find("\"",pos1+1)
                url=data[pos1+1:pos2]
                wf.write(url+"\n")
                data=data[pos2:]
                
                
                
with open("output.txt","r") as rf:
    print(rf.read())
                
                
