import requests

API_KEY = "2133bec5"
url_template = "http://www.omdbapi.com/?apikey={}&{}={}"

def peticion(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos["Response"] == "False":
            return datos["Error"]
        else: 
            return datos
    else:
        return "Error en consulta por id: ", respuesta.status_code

pregunta = input("Título de la película: ")

respuesta = peticion(url_template.format(API_KEY, 's', pregunta))
if isinstance(respuesta, str):
    print(respuesta)
else:
    primera_peli = respuesta["Search"][0]
    clave = primera_peli["imdbID"]

    respuesta = peticion(url_template.format(API_KEY, 'i', clave))
    if isinstance(respuesta, str):
        print(respuesta)
    else:
        titulo = respuesta["Title"]
        agno = respuesta["Year"]
        director = respuesta["Director"]
        print(f"La peli {titulo}, estrenada en el año {agno}, fue dirigida por {director}")


'''
Version 0.1

API_KEY = "2133bec5"
pregunta = input("Título de la película: ")
direccion = f"http://www.omdbapi.com/?apikey={API_KEY}&s={pregunta}"
respuesta = requests.get(direccion)

if respuesta.status_code == 200:
    datos = respuesta.json()
    if datos["Response"] == "False":
        print(datos["Error"])
    else: 
        primera_peli = datos["Search"][0]
        clave = primera_peli["imdbID"]

        otra_direccion = f"http://www.omdbapi.com/?apikey={API_KEY}&i={clave}"
        otra_respuesta = requests.get(otra_direccion)
        
        if otra_respuesta.status_code == 200:
            datos = otra_respuesta.json()
            if datos["Response"] == "False":
                print(datos["Error"])
            else: 
                titulo = datos["Title"]
                agno = datos["Year"]
                director = datos["Director"]
                
                print(f"La peli {titulo}, estrenada en el año {agno}, fue dirigida por {director}")
        else:
            print("Error en consulta: ", otra_respuesta.status_code)

else:
    print("Error en consulta: ", respuesta.status_code)
'''

