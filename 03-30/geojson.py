import urllib
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
    pass


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
    pass


def readResponseDocument(req):
    """
    Make the web request using the supplied request document, 
    and give back the data document in the response
    @return (str) The JSON data in the response
    @raises (ValueError) If the request fails
    """
    pass


def printResponseDocument(resp):
    """
    Using the JSON parser (import json), read the fields from 
    the data document in the response.  Print only the data docment, 
    not the entire response.
    """
    pass


def printCoords(resp):
    """
    Using the JSON parser, find the Latitude and Longitude 
    values in the response, and print them nicely.
    """
    pass


def printLocation(resp):
    """
    Using the JSON parser, find the "formatted_address" field.
    """
    pass



if __name__ == "__main__":
    address = getAddressToSearch()
    req = buildRequest(address)
    
    print('Retrieving...', url)
    
    resp = readResponseDocument(req)
    
    printResponseDocument(resp)
    
    printCoords(resp)
    
    printLocation(resp)
    
    