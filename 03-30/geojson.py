import urllib
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
#  Takes a JSON document as a query.
#  required parameters:  
#       'sensor'  : boolean,
#       'address' : str (the address to search, ex. "Boise, ID")
#       

def getAddressToSearch():
    """
    Ask user for input, like "Boise,ID"
    @return (str) The user's input
    """
    print('Please enter a location to search for (e.g. "Boise, ID"):  ')
    address = input()
#    print(address)
    return address


def buildRequest(addr):
    """
    Assemble the JSON Document that makes the web request
    ex:  
      {
        'sensor':'false',
        'address': addr
      }
    MUST BE URLENCODED (urllib.urlencode())
    @return (str) the request document
    """
    document = {'sensor':'false','address':'%s'%(addr)}
#    print(document)
#    print(json.dumps(document))
    return serviceurl + urllib.parse.urlencode(document)


def readResponseDocument(req):
    """
    Make the web request using the supplied request document, 
    and give back the data document in the response
    @return (str) The JSON data in the response
    @raises (ValueError) If the request fails
    """
    resp = urllib.request.urlopen(req)
#    print(resp)
    print('HTTP %d:  %s' % (resp.getcode(), resp.reason))
    respData = resp.read()
#    print(respData)
    return respData


def printResponseDocument(resp):
    """
    Using the JSON parser (import json), read the fields from 
    the data document in the response.  Print only the data document, 
    not the entire response.
    """
    respObject = json.loads(resp.decode("utf-8"))
    print('printResponseDocument',respObject)


def printCoords(resp):
    """
    Using the JSON parser, find the Latitude and Longitude 
    values in the response, and print them nicely.
    """
    respObject = json.loads(resp.decode("utf-8"))
    lat = respObject['results'][0]['geometry']['location']['lat']
    lng = respObject['results'][0]['geometry']['location']['lng']
    print('Latitude: %f, Longitude: %f' % (lat,lng))


def printLocation(resp):
    """
    Using the JSON parser, find the "formatted_address" field.
    """
    respObject = json.loads(resp.decode("utf-8"))
    formatted_address = respObject['results'][0]['formatted_address']
    print('Formatted Address:  %s' % formatted_address)


if __name__ == "__main__":
    address = getAddressToSearch()
    req = buildRequest(address)
    print('Retrieving...', req)
    resp = readResponseDocument(req)
    printResponseDocument(resp)
    printCoords(resp)
    printLocation(resp)
    
    