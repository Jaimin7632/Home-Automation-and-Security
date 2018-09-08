"""
    RefrigeratorSecurity.py
    Created by Dmitry Chulkov
    Security system for refrigerator. When a person opens refrigerator
    this program takes a picture of him/her, identify (with Microsoft Face API),
    checks permission for this person, send result to Node-Red
"""



import getImage, recognition, access, sendData



    

        


# this function starts all analyzing stuff 
def process():
    path = "D:/"
    host = "192.168.43.1:8080"

    # save a picture of a violator
    getImage.fromIpCam(path, host)
    # get name of person on the photo
    name = recognition.checkPerson(path + "image.jpg", "ffb-fff")
    # check this person for access permissions
    status = access.check(name)
    if status['access'] != True:
        if status['trustedPerson'] == False:
            print ("stranger")
        elif status['trustedPerson'] == True:
            print (name)
            
    









process()

