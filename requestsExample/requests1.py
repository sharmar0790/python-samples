import requests as rq

data  = rq.get("https://www.google.com")

print("data {}".format(data))
print("data.headers {} : ".format(data.headers))