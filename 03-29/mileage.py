#mileage.py
from math import sqrt

def openFile(name = '/Users/tom.stear/Desktop/python_projects/03-29/fillups.txt'):
    f = open(name, "r")
    return f


def readDictionary(file):
    dictionary = {}
    lines = file.readlines()
    i = 0
    prev_mileage = 0
    for l in lines:
#        print(l)
        tokens = l.strip().split(" \t ")
#        print(len(tokens))
        tokens.insert(3, prev_mileage)
        print(tokens)
        dictionary[i] = tokens
#        limit to 10!
#        if i > 10:
#            break
        i += 1
        prev_mileage = tokens[-1]
    return dictionary


def printDictionary(d):
    for k in d:
        print(k, " ", d[k])


def printFuelEconomy(d):
    econList = []
    for k in d:
        if k == 0:
            continue
        v = d[k]
        date = v[0]
        price = float(v[1])
        gallons = float(v[2])
        prev = float(v[3])
        curr = float(v[4])
        econ = (curr - prev) / (1.0 * gallons)
        econList.append(econ)
        print(date, econ)
    return econList
        

def printCheapFillup(d):
    cheapest = ('',9999999999999)
    for k in d:
        v = d[k]
        date = v[0]
        price = float(v[1])
        gallons = float(v[2])
        prev = float(v[3])
        curr = float(v[4])
        if price < cheapest[1]:
            cheapest = (date, price)
    print ("%s, %.2f" % cheapest)

def printExpenseFillup(d):
    mostExpensive = ('',0)
    for k in d:
        v = d[k]
        date = v[0]
        price = float(v[1])
        gallons = float(v[2])
        prev = float(v[3])
        curr = float(v[4])
        if price > mostExpensive[1]:
            mostExpensive = (date, price)
    print ("%s, %.2f" % mostExpensive)

def printMostPerGal(d):
    mostPerGal = ('',0)
    for k in d:
        v = d[k]
        date = v[0]
        price = float(v[1])
        gallons = float(v[2])
        prev = float(v[3])
        curr = float(v[4])
        pricePerGal = price / gallons
        if pricePerGal > mostPerGal[1]:
            mostPerGal = (date, pricePerGal)
    print ("%24s:\t%8s, %.2f" % ("Highest Price per Gallon", mostPerGal[0], mostPerGal[1]))

def printLeastPerGal(d):
    leastPerGal = ('',99999999999)
    for k in d:
        v = d[k]
        date = v[0]
        price = float(v[1])
        gallons = float(v[2])
        prev = float(v[3])
        curr = float(v[4])
        pricePerGal = price / gallons
        if pricePerGal < leastPerGal[1]:
            leastPerGal = (date, pricePerGal)
    print ("%24s:\t%8s, %.2f" % ("Lowest Price per Gallon", leastPerGal[0],leastPerGal[1]))

def printOverallAverage(l):
    sum = 0
    for i in l:
        sum += i
    average = sum / len(l)
    print('Overall Fuel Economy Average:  %.2f Miles/Gal' % average)
    return average


def printStdDev(d, ave):
    #  sigma = sqrt( (1/len(d)) * summation(i)((econ - ave))**2 )
    #  sum = 0
    #  for k in d:
    #      econ = (prev - curr) / (1.0 * gallons)
    #      sum += (econ - ave)**2 
    #  return math.sqrt( (1/len(d)) * sum )  
    sum = 0
    for k in d:
        if k == 0:
            continue
        v = d[k]
        gallons = float(v[2])
        prev = float(v[3])
        curr = float(v[4])
        econ = (curr - prev) / (1.0 * gallons)
        sum += (econ - ave) ** 2
    sigma = sqrt((1/(len(d)-1)) * sum)
    print('Std Dev:  %.2f' % sigma)
    return sigma

dictionary = readDictionary(openFile())
printDictionary(dictionary)
econList = printFuelEconomy(dictionary)
printCheapFillup(dictionary)
printExpenseFillup(dictionary)
printLeastPerGal(dictionary)
printMostPerGal(dictionary)

average = printOverallAverage(econList)

printStdDev(dictionary, average)