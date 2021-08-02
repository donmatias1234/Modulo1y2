import pymongo
import requests #permite conectanor con un sitio web (en este caos API web) y tmb lanzar un metodo web para obtener ingfo desde la API
import json

client = pymongo.MongoClient("mongodb://localhost:27017/") #obtenemos el cliente
mydb=client['mydatebase'] #referencia a la base de datos mydatabase
'''
#paso la direccion de URL como string entre ""
response = requests.get("https://jsonplaceholder.typicode.com/todos")
responseJSON = json.loads(response.text) #convierte la parte texto de la respuesta en un objecto JSON, es importatne especificar que solom la parte de text porque hay otras cosas como los headers de  la respuesta qu eno nos interesa manipular
print(response.text)
print(responseJSON)

for t in responseJSON:
    print(t['title'])

laColeccion = mydb['todos']  #referencio la var laColeccion a la coleccion 'todos' dentro de la BD mydatabase
laColeccion.insert_many(responseJSON)  #inserto lo que ya esta en formato json a la coleccion
'''

#recmendable testear el URL y ver como entrega los datos: como lista, una sola cadena de caracteres, etc
#el uso de "" o '' para el URL es indiferente
response = requests.get("https://raw.githubusercontent.com/bahamas10/css-color-names/master/css-color-names.json")
responseJSON = json.loads(response.text) #convierte la parte texto de la respuesta en un objecto JSON, es importatne especificar que solom la parte de text porque hay otras cosas como los headers de  la respuesta qu eno nos interesa manipular
print(response.text)
print(responseJSON)
laColeccion = mydb['colores']
#como es un solo objeto (una sola cadena de caracteres) se usa un insert_one
laColeccion.insert_one(responseJSON)