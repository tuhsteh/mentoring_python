
import re
import operator

#  open file for reading
thatfile = open('/Users/tom.stear/Desktop/python_projects/pride_and_prejudice_ch_1.txt', 'r')

#  get the lines in the file
lines = thatfile.readlines()

print('Found %d lines' % len(lines))

wordsMap = {}

#  on each line, count how many words there are (.split(' '))
for i in range(0, len(lines)):
    for w in (lines[i].split(' ')):
        word = (re.sub(r"[\n\t\s\W]", "", w)).lower()
        if (word == '' or len(word) < 3):
            continue
        try:
            value = wordsMap[word]
            value += 1
            wordsMap[word] = value
        except KeyError:
            wordsMap[word] = 1
    
thatfile.close()

sorted_x = sorted(wordsMap.items(), key=operator.itemgetter(1))
sorted_x.reverse()

i = 10
for (k,v) in sorted_x:
    print('%25s:\t%3d' % (k,v))
    i -= 1
    if (i < 0):
        break



#for w in wordsMap.keys():
#    print('%25s:\t%3d' % (w, wordsMap[w]))

