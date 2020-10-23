import sys

def esPalabraReservada(palabra):
    if (palabra=="platillo"):
        return True
    elif(palabra=="sal"):
        return True
    elif (palabra == "lizano"):
        return True
    elif (palabra == "("):
        return True
    elif (palabra == "=>"):
        return True
    elif (palabra == ")"):
        return True
    elif (palabra == ","):
        return True
    elif (palabra == "["):
        return True
    elif (palabra == "]"):
        return True
    elif (palabra == "-"):
        return True
    elif (palabra == "mezclar"):
        return True
    elif (palabra == "devolver"):
        return True
    elif (palabra == "fresco"):
        return True
    elif (palabra == "agua_dulce"):
        return True
    elif (palabra == "cafe"):
        return True
    elif (palabra == "listo"):
        return True
    elif (palabra == "AND"):
        return True
    elif (palabra == "OR"):
        return True
    elif (palabra == "$"):
        return True
    elif (palabra == "menu"):
        return True
    elif (palabra == "nl"):
        return True
    elif (palabra == "tab"):
        return True
    elif (palabra == "acompanar"):
        return True
    elif (palabra == "melcochon"):
        return True
    elif (palabra == "servir"):
        return True
    elif (palabra == "tomarOrden"):
        return True
    elif (palabra == "cocinar"):
        return True
    else:
        return False

def leerArchivo():
    # leer archivo, lo divide (.split(" ")) cada division la manda a procesar(linea)
    return

def procesarInstruccion():
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

