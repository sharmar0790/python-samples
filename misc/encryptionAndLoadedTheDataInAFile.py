import os
import re
from base64 import b64encode
import uuid

rid = input("Enter the Reference ID : ")
print("Entered Reference ID is : ", rid)

flag=0
while True:
    if not re.search("[0-9]",rid):
        flag=-1
        break
    elif not re.search("[a-zA-Z]",rid):
        flag=-1
        break
    elif len(rid) >= 13:
        flag =-1
        break
    else:
        break

if flag == -1:
    print("Invalid Reference ID")
    exit(1)

newFile = open("Reference_data.txt","wb+")
fingerPrint = uuid.uuid4()
dataToBeWritten = rid + "," + str(fingerPrint)
dataToBeWrittenBytes = dataToBeWritten.encode("UTF-8")
encryptedStr = b64encode(dataToBeWrittenBytes)

newFile.write(encryptedStr)
newFile.close()
