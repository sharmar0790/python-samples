import postcodes_io_api
import json,os
from math import *

api  = postcodes_io_api.Api(debug_http=False)
lat_long_list = []
resulted_list = []
filename='stores_output.json'

# remove outfile if already exist before executing the program again
# so not to append the old data
def remove_outputfile_ifexist():
    if os.path.exists(filename):
        os.remove(filename)
        print("file exist deleted")  
    else:
        print("file not exist")    


# write the latitude and longitude data in the new file
def write_json(data, filename='stores_output.json'):
    with open(filename,'a+') as f:
        json.dump(data, f,sort_keys=True, indent=4)

# read the input json file
def read_json():
    file = open('stores.json')
    stores_data = json.load(file)
    
    
    for i in stores_data:
        postcode = i['postcode']
        name = i['name']
        is_valid = api.is_postcode_valid(postcode)
        if is_valid:
            postcode_data = api.get_postcode(postcode)
            result = postcode_data['result']
            i['longitude']=result['longitude']
            i['latitude']=result['latitude']
            lat_long_list.append(i)
        else:
            print('postcode {0} is not valid'.format(postcode)) 
    file.close()        
    write_json(lat_long_list)   


# calculate the radius between the two latitude and longitude
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

# fine the nearest restaurants based on given input radius
def find_nearest_restaurants():
    asked_postcode = input('Enter the postcode:  ')
    asked_radius = float(input('Enter the radius(in kms):  '))
    is_valid = api.is_postcode_valid(asked_postcode)
    if is_valid:
        postcode_data = api.get_postcode(asked_postcode)
        result = postcode_data['result']
        asked_longitude=result['longitude']
        asked_latitude=result['latitude']

        for l in lat_long_list:
            lat = l['latitude']
            longi = l['longitude']

            desired_radius = haversine(asked_longitude,asked_latitude,longi,lat)   
            if desired_radius <= asked_radius:
                resulted_list.append(l)

        sort_and_print_result()        
    else:
        print('postcode {0} is not valid. Please try with different one.'.format(asked_postcode)) 

       

def sort_and_print_result():
    resulted_list.sort(key=lambda x: x['longitude'])                              
    resulted_list.sort(key=lambda x: x['latitude'], reverse=True)
    print(resulted_list) 

remove_outputfile_ifexist()
read_json()
find_nearest_restaurants()
