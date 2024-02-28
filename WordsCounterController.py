from WordsCounter import WordsCounter
import json
class WordsCounterController:

    def __init__(self, ruta, palabra):
        self.WCounter = WordsCounter()
        self.ruta = ruta
        self.palabra = palabra
        self.totalApariciones = {}

    def buscarArchivos(self, rutaCarpeta):
        return self.WCounter.buscarArchivos(rutaCarpeta)
    def leerArchivos(self):
        if len(self.WCounter._rutas) == 0:
            return "no se encontraron archivos de texto en la carpeta"
        for archivo in self.WCounter._rutas:
            self.WCounter.leerArchivo(archivo) #'C:\\Users\\sebas\\Documents\\software\\farsante.txt'
        return "archivos leidos"

    """
    iterar sobre los textos, y contar las palabras
    """
    def contarPalabras(self, palabraBuscada):

        for archivo in self.WCounter._texts:
            self.totalApariciones[archivo] = 0
            for palabra in self.WCounter._texts[archivo]:
                if palabra == palabraBuscada:
                    self.totalApariciones[archivo] += 1
        return self.totalApariciones

    def totalAparicionesPorCarpeta(self):
        total = 0
        for archivo in self.totalApariciones:
            total += self.totalApariciones[archivo]
        return total

