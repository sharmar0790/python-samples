import os
import re
from base64 import b64decode,b64encode
import uuid

rid = input("Enter the Reference ID : ")
print("Entered Reference ID is : ", rid)

ridBytes = rid.encode("UTF-8")
encryptedRIDBytes = b64encode(ridBytes)

newFile = open("Reference_data.txt","rb")
contents = ""
if newFile.mode == 'rb':
    contents = newFile.read()
else:
    exit(-1)

decryptedBytes = b64decode(contents)
decryptedString = str(decryptedBytes)

if ridBytes in decryptedBytes:
    list = decryptedString.split(",")
    print("Reference Id %s is present with Finger Print %s " %(rid ,list[1]))
else:
    print("Invalid Reference ID")

newFile.close()
