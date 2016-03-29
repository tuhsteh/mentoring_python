

textFile = open('/Users/tom.stear/Desktop/python_projects/pride_and_prejudice_ch_1.txt','r')

lines = textFile.readlines()

print('Found %d lines' % len(lines))

for i in range(0,len(lines)):
    print('Line %d is %d characters long.' % (i, len(lines[i])))
