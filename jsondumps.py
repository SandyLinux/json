#json is a light wight tool to handle json file, similar with pickel and ??
#
#2 functions used : dumps and loads

#1.1 dumps , object ->json string

import json

newdict ={'name':'wang','id':'001','address':'1 main street'}
jsonstring = json.dumps(newdict)
#print('type of newdict is ', type(newdict))
#print(jsonstring, ' type is ', type(jsonstring))

with open('input.json','r') as f:
    #data's type is string
    data = f.read()


str2dict = json.loads(data)

print(str2dict)
print(type(str2dict))

for i in (str2dict['quiz']['sport']['q1'].values()):
    if type(i) == list:
        print('list....')
        for j in i:
            print(j)
    else:
        print(i)

#dump is used to write json data into a file

with open('output.json','w') as f:
    json.dump(data,f)

#using load and dump to process a file containing json data
with open('output.json','r') as f:
    data = json.load(f)
print('after load.....', data)

with open('genr.json','w') as f:
    f.write(data)



#json encode and decode support None, bool, int, float, str, lists, tuples, dictionary. json _
#small changes when json<--> object
#True  ===> true, Noone====>null

print(json.dumps(False))
print(json.dumps(True))


a1=None

print(a1)
print(json.dumps(a1))


#dump into --> string
print(type(json.dumps(1)))



#dump list ->>string
mylist=[1,2,'33']
print(json.dumps(mylist), type(json.dumps(mylist)))



#dump tuple ====> string
mytuple=(1,2,3,4)
print(json.dumps(mytuple), type(json.dumps(mytuple)))



#dump dictionary ====> string
mydict={'a':1,'b':2,'c':3}
print(json.dumps(mydict), type(json.dumps(mydict)))


with open('allobjects.conf','w') as f:

    #json.dump(json.dumps(mydict),f)
    json.dump('werw',f)

with open('allobjects.conf','r') as f:
    daa = json.load(f)

print(daa)
