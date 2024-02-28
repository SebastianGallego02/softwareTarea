

from WordsCounterController import WordsCounterController
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':

    carpeta = input("ingrese la ruta de la carpeta en donde se encuentran los archivos -> : "
                    "  (ejemplo: C:\\Users\\sebas\\Documents\\software\\pruebas1)")
    palabra = input("ingrese ahora la palabra que se desea buscar -> :")

    controller = WordsCounterController(carpeta, palabra)
    #primero se buscan los archivos
    print(controller.buscarArchivos(carpeta))
    #se lee el contenido de todos los archivos encontrados

    print(controller.leerArchivos())
    print(controller.contarPalabras(palabra))
    print("total de apariciones por carpeta: " + str(controller.totalAparicionesPorCarpeta()))
