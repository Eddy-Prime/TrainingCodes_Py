#===============DICOCTIONARIES  is a data structure that stores data as key-value pairs
                    #they r ordered  & changeable . No duplicates allowed =================>


capitals = {"USA": "Washington, D.C.", "India": "New Delhi", "China": "Beijing", "Russia": "Moscow", "France": "Paris"}

# "dir" is for disctionary
#print(dir(capitals))

#print(capitals.get("USA"))

# this is for Update
capitals.update({"Germany" : "Berlin"})

#this says that if a key does or doesn't exist print this
#if capitals.get("USA"):
    #print("The capital does exist")
#else:
 #   print("The capital does not exist")

#capitals.pop("USA")

#clears the dictionary    
#capitals.clear()

#print(capitals)


#/////////////this is for both keys and values////////////////////


# for key in capitals:

#keys = capitals.keys()

#for loop to print all the keys
#for keys in capitals.keys():

 #   print (keys)

# ////this is for values (the cities)

#value = capitals.values()


#for value in capitals.values():
    #print(value)

#=======this is for both keys and values to print them together==================

items = capitals.items()

for key, value in capitals.items():
    print(f"{key} : {value}")
