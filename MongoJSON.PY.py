import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb=client['mydatebase']
col = mydb['cars']
print(mydb.list_collection_names())
line= '----------------------------------------------------------------'

#la notacion de en JSON para denotar un strin es entre ""
elTexto = '{ "name": {"first":"Jaime", "last":"Lopez"}, "age":"30", "city":["New York", "Chicago"]}'
elString = json.dumps(elTexto)
elJason = json.loads(elTexto)
print(elString) # imprime toda la cadena de carcteres anteponiendo \ a las " para indicar que son parte del texto
print(elJason)
#en python lo denotamos como siempre entre ''
print(elJason['name']['first'])
print(elJason['age'])
print(line)
# la response de una api entrega un string grande con el status (si fue existoso o no la cosnulta
#ApiResponse simula lo que entregaria una api verdadera (:
ApiResponse = '{"status":"success","data": [ \
                {"id":"1", "employee_name":"Tiger Nixon", "employee_salary":"320800", "employee_age":"61"},\
              {"id":"2", "employee_name":"Garret Winters", "employee_salary":"170750", "employee_age":"50"},\
              {"id":"3", "employee_name":"Ashton Cox", "employee_salary":"86000", "employee_age":"45"}]}'
elJason = json.loads(ApiResponse)
#hay que examinar bien el formato de la api para saber bien que es lo que nos esta devolviendo y ocmo pedirselo

print(elJason) #muestra toda la respuesta de la api
print(elJason['data']) #solo muestra la data (la lista)

col =mydb['empleados']
#solo inserto la lista de datos en formato json---> elJason  (que ya lo inteprete con loads
ret = col.insert_many(elJason['data']) # tengo que pasar solo la parte de 'data' del JSON
#MongoDB genera un _id por defecto
for x in col.find({}, {'_id':0, 'id':0}):
    print(x)