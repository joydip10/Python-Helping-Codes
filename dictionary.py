dictt={
   "name":"JOY",
   "age":26,
   "cars":["Ferrari","Mercedes","BMW"]
}

print(dictt)
print(dictt["cars"])
print(dictt.get("age"))
#print(type(dictt))


#dict() method

user_info=dict(name="Chandler Bing",wife="Monica Geller Bing", car_model="Mercedes100",parking_slot="gate-4")
print(user_info)


building_info=dict(owner="JOY",age=26,users=user_info,share_partner_info={"name":"Dr.Ross Geller","Profession":"Paleontologist","share":"20%"})
print(building_info.get("users").get("name"))

#adding to dictionary
building_info["number_of_flats"]=40
print(building_info.get("number_of_flats"))



#looping through a dictionary
print("\nLooping--> \n")
count=0
for i in building_info:
        print(building_info[i])
        
for i in building_info.values():
        print(i)
        
        

print("\n\nItems() method\n\n")

for k,v in building_info.items():
    print(k,':',v)
    
    
           
    
    
    
    
# we can use del["key"] , pop("key") to remove the items from a dictionary
# we can use clear() to clear the dictionary
    
    
    
    
#copying dictionary
    
new_dict=building_info.copy();
new=dict(building_info)

keys=building_info.keys()
values=building_info.values()
items=building_info.items()
print("keys: "+str(keys)+"\n")
print("values: "+str(values)+"\n")
print("ItemsL "+str(items)+"\n")


del new
#print(new) #error


#update() method

dict1=dict(name="JOY",age=24,hobbies=["football","Cricket","Dancing"],Level_of_education="H.S.C")
dict2={
    "Level_of_education":"Bachelors",
    "Employment_status":"Employed",
    "Job_position_ifany":"Sr.Software Engineer"
}

print("\n\n Before update\n")
print(dict1.keys())
print(dict2.keys())

print("\n\nAfter update\n")
dict1.update(dict2)
print(dict1.keys())
print(dict1)


#fromkeys() method

new_dict=dict.fromkeys(["name","age","marital_status"],"unknown")
new_dict1=dict.fromkeys("abcda","unknown")
print(new_dict)
print(new_dict1)




#Exercise

cube={}
for i in range(1,11):
    cube[i]=i**2
    
print(cube)



#Exercise

name="JOY DIP DAS"
dictt={}
for i in name:
    dictt[i]=name.count(i)

print(dictt)
