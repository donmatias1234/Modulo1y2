import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client.list_database_names())

mydb=client['nuevabase']
print(mydb.list_collection_names())

mydb = client['test'] #referenciando la bbdd test a mydb
colec= mydb['miColeccion'] #referencio la coleccion 'micoleccion' desde la var que tiene la bbdd 'test'
#colec.insert_one({'x': 10, 'y': 20})
#colec.insert_one({'x': 35, 'y': 80})
print(colec)
