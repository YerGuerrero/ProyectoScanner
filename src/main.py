import sys

class Scanner:
    def __init__(self, palabra):
        self.palabra = palabra

    def esPalabraReservada(self):
        if (self.palabra=="platillo"):
            return True
        elif(self.palabra=="sal"):
            return True
        elif (self.palabra == "lizano"):
            return True
        elif (self.palabra == "("):
            return True
        elif (self.palabra == "=>"):
            return True
        elif (self.palabra == ")"):
            return True
        elif (self.palabra == ","):
            return True
        elif (self.palabra == "["):
            return True
        elif (self.palabra == "]"):
            return True
        elif (self.palabra == "-"):
            return True
        elif (self.palabra == "mezclar"):
            return True
        elif (self.palabra == "devolver"):
            return True
        elif (self.palabra == "fresco"):
            return True
        elif (self.palabra == "agua_dulce"):
            return True
        elif (self.palabra == "cafe"):
            return True
        elif (self.palabra == "listo"):
            return True
        elif (self.palabra == "AND"):
            return True
        elif (self.palabra == "OR"):
            return True
        elif (self.palabra == "$"):
            return True
        elif (self.palabra == "menu"):
            return True
        elif (self.palabra == "nl"):
            return True
        elif (self.palabra == "tab"):
            return True
        elif (self.palabra == "acompanar"):
            return True
        elif (self.palabra == "melcochon"):
            return True
        elif (self.palabra == "servir"):
            return True
        elif (self.palabra == "tomarOrden"):
            return True
        elif (self.palabra == "cocinar"):
            return True
        else:
            return False

    def leerArchivo(self):
        # leer archivo, lo divide (.split(" ")) cada division la manda a procesar(linea)
        return

    def procesarInstruccion(self):
        # llama esPalabraReservada()
        # esPalabraReservada() is true { #Todos los if }
        # esPalabraReservada() is false { mostrar mensaje error y seguir con la siguiente instruccion }

        # Se anade a una lista de listas el tipo de complemento lexico, el texto y el numero de linea
        # Ejm: [[PalabraReservada, lizano, 1], [Nombre, i, 1]....]
        # Llamar a imprimir Tipo de componente lexico, Texto del componente lexico, Atributos adicionales del componente
        return


def main():
    print(sys.argv[1])
    # Se saca del args
    # leer archivo()

main()

