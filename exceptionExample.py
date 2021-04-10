try:
    a_list = [1,2,3,4]
    print(a_list[4])
except IndexError:
    print("Fetching wrong index value")
except:
    print("Other error")