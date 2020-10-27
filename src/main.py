import sys
import re



# Clase encargada de leer una entrada y devolver una secuencia de componentes lexicos (Tokens) para que estos puedan ser
# utilizados durante la siguiente etapa de analisis
class Explorador:

    # Aqui se definen los atributos que tendra la clase scanner
    def __init__(self, nombre_archivo):
        self.lineaAtributo = 1
        self.listaTokens = []
        self.archivo=nombre_archivo

    # Esta funcion sera la encargada de recibir como parametro el tipo de componente lexico, el texto del
    # componente lexico y la linea correspondiente para insertarlo en la lista de tokens e imprimirlos
    def formarToken(self, nombreToken, palabra, lineaAtributo):
        self.listaTokens.append([nombreToken, palabra, lineaAtributo])
        print("<"+nombreToken+","+palabra+","+str(lineaAtributo)+">")

    # Esta funcion es la encargada de verificar si la entrada es una palabra reseervada
    # Si es una palabra reservada retorna True y si no retorna False
    def esPalabraReservada(self, palabra):
        palabraReservada=["platillo","sal","lizano","(","=>",")",",","[","]","-","mezclar","fresco","agua_dulce",
                          "cafe","AND","OR","menu","nl","tab","acompanar","melcochon","servir","tomarOrden",
                          "cocinar","\¿","\?"]
        resultado = False
        try:
            palabraReservada.index(palabra)
            resultado = True
        except ValueError:
            resultado = False
        finally:
            return resultado

    # Esta funcion es la encargada leer linea por linea la gramatica entrante por medio de un archivo .txt
    # Cada una de estas lineas son separadas por un espacio vacio y los textos obtenidos se guardan en una lista
    # Por ultimo llama la funcion procesarInstruccion con cada uno de los textos almacenados en los campos de la lista
    def leerArchivo(self):
        archivo= open(self.archivo, 'r')
        for linea in archivo.readlines():
            linea_leida = linea.split()
            if linea_leida[0] == "$":
                self.esComentario(linea)
                self.formarToken("Comentario", linea, self.lineaAtributo)
            else:
                for i in linea_leida:
                    self.procesarInstruccion(i)
            self.lineaAtributo += 1 # Por cada linea procesada se aumenta el contador
        archivo.close()

    # Esta funcion verifica si la entrada corresponde a un nombre que contenga letras y numeros o solo letras
    def esNombre(self,palabra):
        resultado = bool(re.search("^[_A-z0-9]*((-|\s)*[_A-z0-9])*$", palabra))
        return resultado

    # Esta funcion es la encargada de verificar si la entrada es un comentario
    def esComentario(self,palabra):
        patron = re.search("^\$[a-zA-Z0-9 \-_\(\)/]+", palabra)
        try:
            if palabra == patron.group():
                return True
        except AttributeError:
            print("Error en la linea " + str(self.lineaAtributo) + ". Comentario contiene caracteres invalidos.")
        finally:
            return False

    # Esta funcion es la encargada de verificar que la entrada sea un punto
    def esPunto(self,palabra):
        if palabra == ".":
            return True
        else:
            return False

    # Esta funcion es la encargada de verificar que la entrada sea alguno de los siguientes operadores: <,>,>=,<=,==
    # !=,!
    def esOperador(self,palabra):
        operadores= ["<",">", "<=", ">=" , "==" , "!=" , "!"]
        resultado = False
        try:
            operadores.index(palabra)
            resultado = True
        except ValueError:
            resultado = False
        finally:
            return resultado


    # Esta funcion es la encargada de verificar que la entrada sea el final de la funcion ya sea que contenga la
    # palabra final o devolver
    def esFinal(self,palabra):
        if(palabra== "Listo" or palabra== "Devolver"):
            return True
        else:
            return False

    # Esta funcion es la encargada de verificar que la entrada sea un numero entero, negativo o flotante
    def esValor(self,palabra):
        resultado = bool(re.search("-?[0-9]+.[0-9]+", palabra) or re.search("-?[0-9]+", palabra))
        return resultado

    # Esta funcion es la encargada de verificar que la entrada sea un operador aritmetico como: +,-,/,*,(,),%
    def esAritmetica(self,palabra):
        listaAritmetica = ["+", "-", "/", "*", "(", ")", "%"]
        resultado = False
        try:
            listaAritmetica.index(palabra)
            resultado = True
        except ValueError:
            resultado = False
        finally:
            return resultado

    #Esta es la funcion encargada de verificar que la entrada sea un texto
    def esTexto(self, palabra):
        patron = re.search("^\"[a-zA-Z0-9 \-_\(\)/]+\"$", palabra)
        try:
            if palabra == patron.group():
                return True
        except AttributeError:
            print("Error en la linea " + str(self.lineaAtributo) + ". Texto contiene caracteres invalidos.")
        finally:
            return False

    # Esta funcion es la encargada de categorizar la palabra segun el tipo de componente lexico y llama la funcion
    # formarToken con los datos correspondientes
    def procesarInstruccion(self,palabra):
        if self.esPalabraReservada(palabra):
            self.formarToken("Palabra Reservada", palabra, self.lineaAtributo)
        elif self.esValor(palabra):
            self.formarToken("Valor", palabra, self.lineaAtributo)
        elif self.esNombre(palabra):
            self.formarToken("Nombre", palabra, self.lineaAtributo)
        elif self.esPunto(palabra):
            self.formarToken("Punto", palabra, self.lineaAtributo)
        elif self.esOperador(palabra):
            self.formarToken("Operador", palabra, self.lineaAtributo)
        elif self.esFinal(palabra):
            self.formarToken("Final", palabra, self.lineaAtributo)
        elif self.esAritmetica(palabra):
            self.formarToken("Aritmetica", palabra, self.lineaAtributo)
        elif self.esTexto(palabra):
            self.formarToken("Texto", palabra, self.lineaAtributo)
        else:
            print("Error en linea " + str(self.lineaAtributo))
            exit
        return

# Esta funcion es la encargada de ejecutar el scanner
def main():
    Explorador( sys.argv[1]).leerArchivo()


main()

