import requests 

direccion = "http://www.omdbapi.com/?apikey=2133bec5&i=tt3896198" #URL a la que quiero llamar

#Hacer petición http
respuesta = requests.get(direccion)

if respuesta.status_code == 200:
    # Esto era una comprobación previa para ver que todo salía bien. 'print(respuesta.text)'
    datos = respuesta.json()
    # Para ver que ha creado el fichero, podríamos hacer un print(datos)
else:
    print("Se ha producido un error", respuesta.status_code)