
#  open file for reading
thatfile = open('/Users/tom.stear/Desktop/python_projects/pride_and_prejudice_ch_1.txt', 'r')

#  get the lines in the file
lines = thatfile.readlines()


print('Found %d lines' % len(lines))

#  on each line, count how many words there are (.split(' '))
for i in range(0, len(lines)):
    words = lines[i].split(' ')
    print('Line %d is %d words long.' % (i, len(words)))

    
thatfile.close()