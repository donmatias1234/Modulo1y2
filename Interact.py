import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb=client['mydatebase']
col = mydb['cars']
print(mydb.list_collection_names())
line= '----------------------------------------------------------------'

'''
mycar = {'_id':1, 'marca':'Toyota', 'modelo':'Corolla', 'agno': '2011'}
col.insert_one(mycar)
morecars = [{'_id':2, 'marca':'Toyota', 'modelo':'Yaris', 'agno': '2014'},\
            {'_id':3, 'marca':'Mazda', 'modelo':'3', 'agno': '2019'},\
            {'_id':4, 'marca':'Suzuki', 'modelo':'Swift', 'agno': '2017'}
]
col.insert_many(morecars)
'''

'''
print(line)
print(col.find_one({'marca':'Mazda'}, {'_id':0,'modelo':0}))
print(line)
print(col.find_one({'marca':{'$gt':'P'}}, {'_id':0})) #hay mas de uno perod ocmo es un fin_one solo tura el primero con marca mayor a "P"
print(line)
print(col.find_one({'marca':{'$regex':'\w*z\w*'}}, {'_id':0}))
print(line)
'''
for x in col.find({}, {'_id':0, 'modelo':0}):
    print("El vehiculo es " + x['marca'] + " del año " + x['agno'])
print(line)
for x in col.find({}, {'_id':0, 'modelo':0}).limit(2): #miestro los primeros 2
    print("El vehiculo es " + x['marca'] + " del año " + x['agno'])
print(line)
for x in col.find({}, {'_id':0, 'modelo':0}).skip(2):  #muestro des ues de los 2 primeros
    print("El vehiculo es " + x['marca'] + " del año " + x['agno'])
print(line)
for x in col.find({'marca':{'regex':'\w*z\w*'}}, {'_id':0}):
    print("El vehiculo es " + x['marca'] + " del año " + x['agno'])
print(line)
