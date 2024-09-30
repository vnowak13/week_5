#dictionary = a collention of {key:value} parts order and changeable. No duplicates 
capitals = {"USA": "Washington DC",
             "India": "New Dehli",
             "China": "Beijin",
             "Russia": "Moscow"}
             
#print(dir(captials))
#print(help(captials))
# print(captipals.get("USA"))

# if captipals.get("Russia"):
#     print("That captipal exists")
# else:
#     print("That captial doesn't exists")

# updates 
# capitals.update({"Germany": "Berlin",
#                  "Poland": "Warsaw",
#                  "France": "Paris"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China") #removes item from the dictionary
# capitals.popitem() #rid of last item of the dictionary
# capitals.clear() #clears the dictionary

# keys = capitals.keys() # it returns all the keys not the variables
# for key in capitals.keys(): 
#     print(keys)

# capitals.values() #returns all the values of the dictionary
# values = capitals.values()
# for values in capitals.values():
#     print(values)

# items =capitals.items()
# for key, value in capitals.items():
#     print(f "{key}: {values}")