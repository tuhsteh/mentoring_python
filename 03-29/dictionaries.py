

def readDictionary(file):
    dictionary = {}
    lines = file.readlines()
    for l in lines:
#        print(l)
        tokens = l.split(",")
#        print(len(tokens))
        dictionary[tokens[1]] = tokens[2].strip()
    return dictionary
        


def readFile(name = '/Users/tom.stear/Desktop/python_projects/03-29/sample.txt'):
    f = None
    try:
        f = open(name, 'r')
    except Error as e:
        print('Error opening file.  ', e)
    return f


def printCapitals(dictionary):
    for k in dictionary:
        print('The capital of %s is %s' % (k, dictionary[k]))

        
def printStates(dictionary):
    for k in dictionary:
        print(k)
    



if __name__ == "__main__":
    file = readFile()
    stateDictionary = readDictionary(file)
    printStates(stateDictionary)
    printCapitals(stateDictionary)
    
    