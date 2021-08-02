import pymongo
import requests #permite conectanor con un sitio web (en este caos API web) y tmb lanzar un metodo web para obtener ingfo desde la API
import json
client = pymongo.MongoClient("mongodb://localhost:27017/") #obtenemos el cliente
mydb=client['MiniProyecto3'] #referencia a la base de datos mydatabase

#paso la direccion de URL como string entre ""
url = 'https://apis.digital.gob.cl/fl/feriados/2020'
# desde la API, boton derecho->inspeccionar->Network->header-->Remote address: corresponde al valor del user-agent
# en este caso 52.10.168.224:443
headers = {'User-Agent': 'AppleWebKit/537.36'}
response = requests.get(url, headers=headers)
responseJSON = json.loads(response.text) #convierte la parte texto de la respuesta en un objecto JSON, es importatne especificar que solom la parte de text porque hay otras cosas como los headers de  la respuesta qu eno nos interesa manipular
#print(response.text)
print(responseJSON)

col = mydb['feriados2020']  #referencio la var laColeccion a la coleccion 'todos' dentro de la BD mydatabase
#col.insert_many(responseJSON)  #se insertaron 19 documentos

line= '----------------------------------------------------------------'
print('===== Todos los Feriados de 2020 =====')
for x in col.find({}, {'nombre':1, 'tipo':1, 'fecha':1}):
    print('El día de '+x['nombre']+' es un feriado de tipo '+x['tipo']+' y se celebra el '+x['fecha'])
print(line)
print('===== Solo los Feriados Civiles de 2020 =====')
for x in col.find({'tipo':'Civil'}, {'nombre':1, 'tipo':1, 'fecha':1}):
    print('El día de '+x['nombre']+' es un feriado de tipo '+x['tipo']+' y se celebra el '+x['fecha'])
print(line)
print('===== Solo los Feriados Irrenunciables de 2020 =====')
for x in col.find({'irrenunciable':'1'}, {'nombre':1, 'tipo':1, 'fecha':1}):
    #irrencunciable es una var booleanda con valor True con 1
    print('El día de '+x['nombre']+' es un feriado de tipo '+x['tipo']+' y se celebra el '+x['fecha'])
print(line)
print('===== Solo los Feriados que incluyen "Santo" o "Santos" =====')
for x in col.find({'nombre':{'$regex':'\w*Santo\w*'}}, {'nombre':1, 'tipo':1, 'fecha':1}):
    print('El día de '+x['nombre']+' es un feriado de tipo '+x['tipo']+' y se celebra el '+x['fecha'])
print(line)
print('===== Leyes relacionadas con el Plebiscito de Abril =====')
print('Las leyes involucradas en el día del Plebiscito Constitucional son las siguientes:')
for x in col.find({'nombre':{'$regex':'\w*Plebiscito\w*'}}, {'nombre':1, 'tipo':1, 'leyes':1}):
    for y in x['leyes']: #epecificar BIEN LO QUE QUIERO RECORRER, en este caso viene  a ser la lista de leyes
        print(y['nombre']+' Revisar en: '+y['url'])
print(line)
