import sys
import re

class Scanner:
    def __init__(self, palabra):
        self.palabra = palabra
        self.lineaAtributo = 1
        self.listaTokens = []

    def formarToken(self, nombreToken, palabra, lineaAtributo):
        self.listaTokens.append([nombreToken, palabra, lineaAtributo])
        # Aqui va el print de cada token.

    def leerArchivo(self):
        # leer archivo, lo divide (.split(" ")) cada division la manda a procesar(linea)
        return

    def esPalabraReservada(self):
        # Retorna verdadero o falso
        # 7 o mas if
        return True

    def esNombre(self):

        patron = re.search("[a-z][a-zA-Z0-9]+", self.palabra)
        resultado = False

        if palabra == patron.group():
            resultado = True
    
        return resultado

        #p = re.search("[a-z][a-zA-Z0-9]+")
        #return p

    def esComentario(self):

        patron = re.search("^\$[a-zA-Z \-_\(\)/]+$", self.palabra)
        resultado = False

        try:
            if self.palabra == patron.group():
                resultado = True
        except AttributeError:
            print("Error en la linea " + self.lineaAtributo + ". Comentario contiene caracteres invalidos.")
        finally:
            return resultado

        return resultado

    def esPunto(self):

        if self.palabra == ".":
            return True
        else:
            return False

    def esOperador(self):
        return

    def esFinal(self):
        return

    def esValor(self):
        return

    def esAritmetica(self):
        return

    def procesarInstruccion(self):

        if esPalabraReservada():
            formarToken("Palabra Reservada", self.palabra, self.lineaAtributo)
        elif esNombre():
            formarToken("Nombre", self.palabra, self.lineaAtributo)
        elif esComentario():
            formarToken("Comentario", self.palabra, self.lineaAtributo)
        elif esPunto():
            formarToken("Punto", self.palabra, self.lineaAtributo)
        elif esValor():
            formarToken("Valor", self.palabra, self.lineaAtributo)
        elif esOperador():
            formarToken("Operador", self.palabra, self.lineaAtributo)
        elif esFinal():
            formarToken("Final", self.palabra, self.lineaAtributo)
        elif esAritmetica():
            formarToken("Aritmetica", self.palabra, self.lineaAtributo)
        else:
            print("Error en linea " + self.lineaAtributo)
            exit
            # tirar error diciendo que no es ninguna de estas.

        # llama esPalabraReservada()
        # esPalabraReservada() is false { #Todos los if, para ver si es asignacion, etc }
        # esPalabraReservada() is true { mostrar mensaje error y seguir con la siguiente instruccion }

        # Se anade a una lista de listas el tipo de complemento lexico, el texto y el numero de linea
        # Ejm: [[PalabraReservada, lizano, 1], [Nombre, i, 1]....]
        # Llamar a imprimir Tipo de componente lexico, Texto del componente lexico, Atributos adicionales del componente
        return


def main():
    # print(sys.argv[1])

    scanner = Scanner(True)
    # scanner.palabra = False
    # print(scanner.palabra)
    # scanner.procesarInstruccion()

    # Se saca del args
    # leer archivo()


main()

