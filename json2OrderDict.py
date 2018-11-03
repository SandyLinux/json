import json
from collections import OrderedDict

mydict='{"name":"ceme", "shares":45, "price":12.01}'
datadict = json.loads(mydict, object_pairs_hook=OrderedDict)
print(mydict, ' type is :', type(mydict))
print(datadict, 'type is :', type(datadict))



class MyObject:
        
    def __init__(self,dct):
        self.__dict__ = dct


data = json.loads(mydict, object_hook = MyObject)

print(data.name)
print(data.price)
print(data.shares)

dictstring = json.dumps(datadict, indent=4)
print(dictstring)


# serialize an object to ordered dictionary
class Rectangle:
    def __init__(self,h,w):
        self.h = h
        self.w = w


#add classname into the object dictionary
def serialize_instance(obj):
    #d = {'__classname__':type(obj).__name__}
    d={}
    d.update(vars(obj))
    return d


rec = Rectangle(3,5)

obj2str = json.dumps(rec, default=serialize_instance)
print(obj2str)

print('@@@@@',vars(rec))


