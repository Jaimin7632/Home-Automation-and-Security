# 
#	Person.py
#	Created by Dmitry Chulkov
#	This file provides a set of functions that allow to work with a single person in Face API
#

import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

global KEY
KEY = 'fd4eac20ccfd4f979ffade6a7d134997'

def createPerson(personGroupID, name):
    global KEY

    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': KEY,
    }

    params = urllib.parse.urlencode({
    })

    body = {'name': name}

    try:
        conn = http.client.HTTPSConnection('southeastasia.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/persongroups/" + personGroupID + "/persons?%s" % params, json.dumps(body), headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        data = data.decode('ascii')
        data = json.loads(data)
        return data
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return

    
def getPerson(personGroupID, personID):
    global KEY
    
    headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': KEY,
    }

    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('southeastasia.api.cognitive.microsoft.com')
        conn.request("GET", "/face/v1.0/persongroups/" + personGroupID + "/persons/" + personID + "?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        data = data.decode('ascii')
        data = json.loads(data)
        return data
    except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return

    
def listPersonsInPersonGroup(personGroupID):
    global KEY
	
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': KEY,
    }

    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('southeastasia.api.cognitive.microsoft.com')
        conn.request("GET", "/face/v1.0/persongroups/" + personGroupID + "/persons?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        data = data.decode('ascii')
        data = json.loads(data)
        return data
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror)) 
    return
	
    
def addPersonFace(personGroupID, personID, image, targetFace='{string}'):
    global KEY
    
    headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': KEY,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        #'targetFace': targetFace,
    })
    
    body = open(image, 'rb')

    try:
        conn = http.client.HTTPSConnection('southeastasia.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/persongroups/" + personGroupID + "/persons/" + personID + "/persistedFaces?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        data = data.decode('ascii')
        data = json.loads(data)
        return data
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    
    return




def deletePerson(personGid,personId):
    global KEY
    headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': KEY,
    }

    params = urllib.parse.urlencode({
        
    })
    body = {    }

    try:
        personGroupId= personGid
        personId= personId
        
        conn = http.client.HTTPSConnection('southeastasia.api.cognitive.microsoft.com')
        conn.request("DELETE", "/face/v1.0/persongroups/"+personGroupId+"/persons/"+personId+"?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))





