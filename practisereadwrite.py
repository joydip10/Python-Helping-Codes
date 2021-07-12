with open('part1.txt','r',encoding='UTF-8') as rf:
    with open('part2.txt','w+',encoding='UTF-8') as wf:
        wf.write('NAME, AGE\n')
        data=rf.readlines()
        for i in data:
            wf.write(i)
#            wf.write('\n')