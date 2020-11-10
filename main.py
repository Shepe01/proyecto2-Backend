from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from Personas import persona
from Canciones import Cancion
from Solicitudes import Solicitud

app = Flask(__name__)
CORS(app)


Usuarios = [] 
Canciones = []
cont_canciones = 0
Solicitudes = []
Cont_soli =0

Usuarios.append(persona('Usuario','Maestro','admin','admin','administrador'))

Solicitudes.append(Solicitud('','Sofia','Alvaro Soler','El Mismo Sol','2016','https://www.buscaletras.com/photos/albums/alvaro-soler/max/eterno-agosto.jpg','https://open.spotify.com/embed/track/5vj59ONIVbyhcrI8ZSwoRo','https://www.youtube.com/embed/qaZ0oAh4evU'))
Solicitudes.append(Solicitud('','Trouble','Avicii','STORIES','2015','https://c-sf.smule.com/rs-s34/arr/af/f5/8ea3aa7b-1525-40d3-91be-705298cfd9ea_1024.jpg','https://open.spotify.com/embed/track/0JZ9TvOLtZJaGqIyC4hYZX','https://www.youtube.com/embed/GiuabrUp8zM'))
Solicitudes.append(Solicitud('','High Hopes','Panic! At The Disco ','Pray For The Wicked','2018','https://lastfm.freetls.fastly.net/i/u/ar0/7b944039297639ed837617053a3cd1ca.jpg','https://open.spotify.com/embed/track/1rqqCSm0Qe4I9rUvWncaom','https://www.youtube.com/embed/IPXIgEAGe4U'))
Solicitudes.append(Solicitud('','sunflower','Post Malone ','beerbongs & bentleys','2018','https://i1.sndcdn.com/artworks-000453095229-y5m0e2-t500x500.jpg','https://open.spotify.com/embed/track/3KkXRkHbMCARz0aVfEt68P','https://www.youtube.com/embed/ApXoWvfEYVU'))
Solicitudes.append(Solicitud('','Memories','Maroon 5 ','Marron 5 Radio','2019','https://www.letrarius.com/images/albums/maroon%205.jpg','https://open.spotify.com/embed/track/2b8fOow8UzyDFAE27YhOZM','https://www.youtube.com/embed/SlPhMPnQ58k'))



@app.route('/', methods=['GET'])
def rutaInicial():
    print("Ruta Inicial")
    return("Ruta Incial")

@app.route('/Login',methods = ['POST'])

def Login():
    global Usuarios
    username = request.json['usuario']
    password = request.json['password']
    for usuario in Usuarios:
        if usuario.getUsuario()== username and usuario.getPassword()==password:
            Dato = {
                'message': 'Success',
                'usuario': usuario.getUsuario(),
                'tipo' : usuario.getTipo()
            }
            break
        else:
            Dato = {
                'message' : 'Falied',
                'usuario': ''

        }
    respuesta = jsonify(Dato)
    return respuesta

@app.route('/Contraseña',methods = ['POST'])

def Contraseña():
    global Usuarios
    username = request.json['usuario']
    for usuario in Usuarios:
        if usuario.getUsuario()== username:
            Dato = {
                'message': 'Success',
                'password': usuario.getPassword()

            }
            break
        else:
            Dato = {
                'message' : 'Falied',
                'password': ''

        }
    respuesta = jsonify(Dato)
    return respuesta


@app.route('/Personas/<string:nombre>',methods = ['GET'])

def ObtenerPersonas(nombre):
    global Usuarios
    for usuario in Usuarios:
        if usuario.getUsuario() == nombre:
            Dato ={
                'nombre':usuario.getNombre(),
                'apellido':usuario.getApellido(),
                'usuario': usuario.getUsuario(),
                'password':usuario.getPassword()
                }
            break
    respuesta = jsonify(Dato)
    return(respuesta)

@app.route('/Personas/<string:nombre>', methods=['PUT'])
def ActualizarPersona(nombre):
    global Usuarios
    for i in range(len(Usuarios)):
        if nombre == Usuarios[i].getUsuario():
            Usuarios[i].setNombre(request.json['nombre'])
            Usuarios[i].setApellido(request.json['apellido'])
            Usuarios[i].setUsuario(request.json['usuario'])
            Usuarios[i].setPassword(request.json['password'])
            break
    return jsonify({'message':'Se actualizo el dato exitosamente'})

@app.route('/Personas/<string:nombre>', methods=['DELETE'])
def EliminarPersona(nombre):
    global Usuarios
    for i in range(len(Usuarios)):
        if nombre == Usuarios[i].getNombre():
            del Usuarios[i]
            break
    return jsonify({'message':'Se elimino el dato exitosamente'})

@app.route('/Personas', methods=['POST'])
def AgregarUsuario():
    global Usuarios
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    username = request.json['usuario']
    password = request.json['password']
    tipo = request.json['tipo']
 
    encontrado = False
    for usuario in Usuarios:
        if usuario.getUsuario()==username:
            encontrado = True
            break
    if encontrado:
        return jsonify({
            'message':'Failed',
            'reason':'El usuario ya esta registrado'
        })
    else:
        nuevo = persona(nombre,apellido,username,password,tipo)
        Usuarios.append(nuevo)
        return jsonify({
            'message':'Success',
            'reason':'Se agrego el usuario'
        })


@app.route('/Personas', methods = ['GET'])
def VerPersonas():
    global Usuarios
    Datos = []
    for usuario in Usuarios:
        Dato = {
            'nombre' : usuario.getNombre(),
            'apellido' : usuario.getApellido(),
            'usuario' : usuario.getUsuario(),
            'password' : usuario.getPassword()
        }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return (respuesta)

@app.route('/Solicitud', methods = ['POST'])
def guardarCancion1():
    global Solicitudes, Cont_soli  
    id1 = Cont_soli
    nombre1 = request.json['nombre1']
    artista1 = request.json['artista1']
    album1 = request.json['album1']
    fecha1 = request.json['fecha1']
    imagen1 = request.json['imagen1']
    spotify1 = request.json['spotify1']
    youtube1 = request.json['youtube1']
    nuevo = Solicitud(id1, nombre1, artista1, album1, fecha1, imagen1, spotify1, youtube1)
    Solicitudes.append(nuevo)
    Cont_soli +=1
    return jsonify({
            'message' : 'Success',
            'reason' : 'Se Agrego la Cancion'
        })

@app.route('/Solicitud', methods = ['GET'])
def obtenerCanciones1():
    global Solicitudes, Cont_soli
    Datos = []
    for Solicitud in Solicitudes:
        Dato = {
            'id1' : Solicitud.getId1(),
            'nombre1' : Solicitud.getCancion1(),
            'artista1' : Solicitud.getArtista1(),
            'album1' : Solicitud.getAlbum1(),
            'fecha1' : Solicitud.getFecha1(),
            'imagen1' : Solicitud.getImagen1(),
            'spotify1' : Solicitud.getSpotify1(),
            'youtube1' : Solicitud.getYoutube1()
        }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return (respuesta)

@app.route('/Cancion', methods = ['POST'])
def guardarCancion():
    global Canciones, cont_canciones  
    id = cont_canciones
    nombre = request.json['nombre']
    artista = request.json['artista']
    album = request.json['album']
    fecha = request.json['fecha']
    imagen = request.json['imagen']
    spotify = request.json['spotify']
    youtube = request.json['youtube']
    nuevo = Cancion(id, nombre, artista, album, fecha, imagen, spotify, youtube)
    Canciones.append(nuevo)
    cont_canciones +=1
    return jsonify({
            'message' : 'Success',
            'reason' : 'Se Agrego la Cancion'
        })

@app.route('/Cancion', methods = ['GET'])
def obtenerCanciones():
    global Canciones, cont_canciones
    Datos = []
    for Cancion in Canciones:
        Dato = {
            'id' : Cancion.getId(),
            'nombre' : Cancion.getCancion(),
            'artista' : Cancion.getArtista(),
            'album' : Cancion.getAlbum(),
            'fecha' : Cancion.getFecha(),
            'imagen' : Cancion.getImagen(),
            'spotify' : Cancion.getSpotify(),
            'youtube' : Cancion.getYoutube()
        }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return (respuesta)
if __name__ == "__main__":
    app.run(port=3000, debug=True)
    