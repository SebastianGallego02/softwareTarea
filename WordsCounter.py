import json
import csv
import os
import xml.etree.ElementTree as ET

class WordsCounter:

    def __init__(self):
        self._texts = {}
        self._rutas = []


    """ Funcion que sirve para encontrar todos los archivos con las extensiones deseadas dentro 
        de la carpeta que el usuario indique 
        @:param la ruta de la carpeta
    """
    def buscarArchivos(self, rutaCarpeta):
        try:
            extensiones = ['txt', 'xml', 'json', 'csv']
            # Obtener la lista de archivos en el directorio
            archivos_en_directorio = os.listdir(rutaCarpeta)
            # Filtrar los archivos por extensión
            archivos_filtrados = [archivo for archivo in archivos_en_directorio if
                                  any(archivo.endswith(ext) for ext in extensiones)]
            for archivo in archivos_filtrados:
                ruta_completa = os.path.join(rutaCarpeta, archivo)
                print(f'Archivo encontrado: {ruta_completa}')
                self._rutas.append(ruta_completa)
        except FileNotFoundError:
            return "la carpeta indicada no existe"
        except OSError:
            return "No se encontraron archivos de texto en la carpeta"



    def leerArchivo(self, archivoRuta):
        extension = archivoRuta.split('.')[-1].lower()
        archivoNombre = archivoRuta.split('\\')[-1].lower()  # Obtener la extensión del archivo
        texto = []
        match extension:
            case 'json':
                with open(archivoRuta, 'r') as file:
                    contenido = json.load(file)
                    for palabra in contenido:
                        print(palabra)
            case 'csv':
                with open(archivoRuta, 'r') as file:
                    contenido = csv.reader(file)
                    for fila in contenido:
                        for palabra in fila:
                            texto.append(palabra)
            case 'xml':
                tree = ET.parse(archivoRuta)
                root = tree.getroot()
                for elem in root.iter():
                    if elem.text:
                        palabras = elem.text.split()
                        for palabra in palabras:
                            texto.append(palabra)
            case 'txt':
                with open(archivoRuta, 'r') as file:
                    contenido = file.read()
                palabras = contenido.split()
                for palabra in palabras:
                    texto.append(palabra)
            case _:
                return "No se encontraron archivos"

        self._texts[archivoNombre] = texto
        return True

