def search(item,list):
    if item in list:
        print("Found the number %d at index %d " %(item, list.index(item)))
    else:
        print("Not Found the number : ", item)

list = [1,2,3,4,5,6]
search(3,list)
search(10,list)
