l=["Pintu","Mohit","Rajveer","Kalam","Sakib"]

chk=0
for pos,val in enumerate(l):
    if val=='Kalam':
        print(f"{pos}:-> {val}")
        chk=0
        break;
    else:
        chk=1


if(chk==1):
    print("Nothing found")
    
    
