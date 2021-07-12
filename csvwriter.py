#Using writer
from csv import reader
from csv import writer

with open("file.csv",'w',newline='') as wf:
    csv_writer=writer(wf)
    #there are two ways to write ---> writerow & writerows
    csv_writer.writerow(["Name","Country"])
    csv_writer.writerow(["Joseph","Spain"])
    csv_writer.writerow(["Alice","Singapore"])
    csv_writer.writerow(["Ahmed","Pakistan"])
    csv_writer.writerow(["Dikshit","India"])
    csv_writer.writerow(["Raiden","America"])

with open("file.csv",'r') as rf:
    csv_reader=reader(rf)
    for i in csv_reader:
        print(i)
        
print("\n\n")      
    
with open("file1.csv","w",newline='') as wf:
    csv_writer=writer(wf)
    csv_writer.writerows([['Name','Account'],['Johny','DBBL'],['Masphy','UCL'],['Ahmed','BB'],['Liaket','DBBL'],['Mandy','UCL']])
    
with open("file1.csv",'r') as rf:
    r=reader(rf)
    for i in r:
        print(i)
        
        


#Using DictWriter
from csv import DictWriter
from csv import DictReader

with open("file2.csv","w",newline='') as wf:
    csv_writer=DictWriter(wf,fieldnames=["Firstname","Lastname","Age"])
    csv_writer.writeheader()
        #two methods---->writerow & writerows
    csv_writer.writerow({
                'Firstname':'John',
                'Lastname':'Mathews',
                'Age':26
                })
    csv_writer.writerow({
               'Firstname':'Mandy',
               'Lastname':'Brown',
               'Age':25
               })
    


print("\n\n")    
with open("file2.csv","r") as rf:
    read=DictReader(rf)
    for i in read:
        print(i)
        
print("\n\n")          
with open("file3.csv","w",newline='') as wf:
    write=DictWriter(wf,fieldnames=["Name","Age","Country"])
    write.writeheader()
    write.writerows([
            {'Name':'Johny','Age':23,'Country':'USA'},
            {'Name':'Nitin','Age':25,'Country':'India'},
            {'Name':'Neela','Age':25,'Country':'Bangladesh'},
            {'Name':'Raiden','Age':27,'Country':'Spain'},
            {'Name':'Luo Kang','Age':28,'Country':'China'}
            ])        

    
with open('file3.csv','r') as rf:
    read=reader(rf)
    for i in read:
        print(i)
        
        
with open("file3.csv",'r') as rf:
    with open("file4.csv",'a',newline='') as wf:
          read=DictReader(rf)
          write=DictWriter(wf,fieldnames=["Name","Age","Country"])
          write.writeheader()
          for i in read:
              write.writerow({
                      "Name":i['Name'],
                      'Age':i['Age'],
                      'Country':i['Country']
                      })


print("\n\n")
with open("file4.csv",'r') as rf:
    read=reader(rf)
    for i in read:
        print(i)





























        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        