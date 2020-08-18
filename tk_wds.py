#!/usr/bin/env python
import sys
count = 0

thisdict = {
}

if len(sys.argv) <= 1 :
    print("!!The program can't be executed whithout an archive!!")
else:
    file_name = sys.argv[1]

    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            count += 1

            for word in line.split(): 
                if word in thisdict:
                    thisdict[word] += 1                    
                else:
                    thisdict[word] = 1

dict_sort={key: value for key, value in sorted(thisdict.items(), key=lambda item: item[1])}
for key, value in dict_sort.items(): 
    print("{}: {}".format(key, value))         