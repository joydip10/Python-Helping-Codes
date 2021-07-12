with open("exercisefile2_1.txt","r") as rf:
    with open("exercisefile2_test.txt","a") as wf:
        data=rf.readlines()
        for info in data:
            part_1,part_2=info.split(",")
            new_data=f"{part_1}'s salary is {part_2}"
            wf.write(new_data)
            
            
with open("exercisefile2_test.txt","r") as rf:
    print(rf.read())