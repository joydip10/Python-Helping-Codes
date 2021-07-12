from csv import reader
from csv import DictReader

#With reader function
print("With reader Function\n")
with open("csvcsv.csv","r") as rf:
    csv_reader=reader(rf)
    l=list(csv_reader)
    print(l)
        
    rf.seek(0)
    print("\n")
    for i in csv_reader: #this will not run without seek(0) function 
        print(i)
    
    print("\n")
    
    print(l)
    
    print("\n")
    
    rf.seek(0)
    
    next(csv_reader)#using this line we omit the first line to be printed

    for i in csv_reader:
        print(i)
        
        
print("\n\nWith DictReader Function\n")        

        
#with DictReader function -> reading the csv file as an ordered dictionary
with open("csvcsv.csv","r") as rf:
    csv_reader=DictReader(rf,delimiter=',')
    
    for i in csv_reader:
        print(i)
        
    print("\n")
    
    print("Just printing the names:")
    rf.seek(0)
    for i in csv_reader:
        print(i['Name'])
    
    print("\n")
    
    print("Just printing the loans:")
    rf.seek(0)
    next(csv_reader)
    for i in csv_reader:
        print(i['Loan'])

    
    print("\n")
    
    

































        