import requests

API_KEY = "2133bec5"
url_template = "http://www.omdbapi.com/?apikey={}&{}={}"

class PeticionError(Exception):
    pass

def peticion(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos["Response"] == "False":
            raise PeticionError(datos["Error"])
        else: 
            return datos
    else:
        raise  PeticionError("Error en consulta: {}".format(respuesta.status_code))

repetir = 'S'

while repetir == 'S':
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

    repetir = input("¿Quieres hacer otra búsqueda? (S/N) ").upper()