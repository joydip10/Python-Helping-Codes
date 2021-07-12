import codecs

f_name="JOY DIP"
l_name="DAS"
full_name=f_name+" "+l_name
print(full_name)


#print(full_name+3) #produces error

print(full_name+"3") # no error
print(full_name+str(10)) # no error

print(full_name*3) #prints the full_name string three times


for i in full_name:
    print(i,end='  ')

 
      print('\n')



var=""

if i in var:
    print('Not empty')
else:
    print('Empty')