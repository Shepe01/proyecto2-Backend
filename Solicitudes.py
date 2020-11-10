class Solicitud:
    def __init__(self,id1,cancion1,artista1,album1,fecha1,imagen1,spotify1,youtube1):
        self.id1 = id1
        self.cancion1 = cancion1
        self.artista1 = artista1
        self.album1 = album1
        self.fecha1 = fecha1
        self.imagen1 = imagen1
        self.spotify1 = spotify1 
        self.youtube1 = youtube1

    def getId1(self):
        return self.id1

    def getCancion1(self):
        return self.cancion1

    def getArtista1(self):
        return self.artista1

    def getAlbum1(self):
        return self.album1

            
    def getFecha1(self):
        return self.fecha1

    def getImagen1(self):
        return self.imagen1
    
    def getSpotify1(self):
        return self.spotify1
    
    def getYoutube1(self):
        return self.youtube1

    def setId1(self, id1):
        self.id1 = id1

    def setCancion1(self, cancion1):
        self.cancion1 = cancion1

    def setArtista1(self, artista1):
        self.artista1 = artista1

    def setAlbum1(self, album1):
        self.album1 = album1

    def setFecha1(self, fecha1):
        self.fecha1 = fecha1
        
    def setImagen1(self, imagen1):
        self.imagen1 = imagen1
            
    def setSpotify1(self, spotify1):
        self.spotify1 = spotify1
    
    def setYoutube1(self, youtube1):
        self.youtube1 = youtube1