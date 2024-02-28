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



    def leerArchivo(self, archivo_ruta):
        extension = archivo_ruta.split('.')[-1].lower()
        archivoNombre = archivo_ruta.split('\\')[-1].lower()  # Obtener la extensión del archivo
        texto = []
        match extension:
            case 'json':
                with open(archivo_ruta, 'r') as file:
                    contenido = json.load(file)
                    for palabra in contenido:
                        print(palabra)
            case 'csv':
                with open(archivo_ruta, 'r') as file:
                    contenido = csv.reader(file)
                    for fila in contenido:
                        for palabra in fila:
                            texto.append(palabra)
            case 'xml':
                tree = ET.parse(archivo_ruta)
                root = tree.getroot()
                for elem in root.iter():
                    if elem.text:
                        palabras = elem.text.split()
                        for palabra in palabras:
                            texto.append(palabra)
            case 'txt':
                with open(archivo_ruta, 'r') as file:
                    contenido = file.read()
                palabras = contenido.split()
                for palabra in palabras:
                    texto.append(palabra)
            case _:
                return "No se encontraron archivos"

        self._texts[archivoNombre] = texto
        return True


    def contarPalabra(self, palabraBuscada, texto):
        totalAparicioines = 0
        for palabra in texto:
            if palabra == palabraBuscada:
                totalAparicioines += 1
        return totalAparicioines
