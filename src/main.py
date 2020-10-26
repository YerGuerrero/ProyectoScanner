import sys
import re

class Scanner:
    def __init__(self, nombre_archivo):
        self.lineaAtributo = 1
        self.listaTokens = []
        self.archivo=nombre_archivo

    def formarToken(self, nombreToken, palabra, lineaAtributo):
        self.listaTokens.append([nombreToken, palabra, lineaAtributo])
        # Aqui va el print de cada token.

    def esPalabraReservada(self, palabra):
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
        elif (palabra == "fresco"):
            return True
        elif (palabra == "agua_dulce"):
            return True
        elif (palabra == "cafe"):
            return True
        elif (palabra == "AND"):
            return True
        elif (palabra == "OR"):
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

    def leerArchivo(self):
        archivo= open(self.archivo, 'r')
        print("archivo", archivo)
        for linea in archivo.readlines():
            print(linea)
            linea_leida = linea.split()
            for i in linea_leida:
                # self.procesarInstruccion(i)
                print(i)
        archivo.close()
        return

    def esNombre(self,palabra):
        resultado = bool(re.search("^[_A-z0-9]*((-|\s)*[_A-z0-9])*$", palabra))
        return resultado


    def esComentario(self,palabra):
        patron = re.search("^\$[a-zA-Z \-_\(\)/]+$", palabra)
        try:
            if palabra == patron.group():
                return True
        except AttributeError:
            print("Error en la linea " + str(self.lineaAtributo) + ". Comentario contiene caracteres invalidos.")
        finally:
            return False


    def esPunto(self,palabra):
        if palabra == ".":
            return True
        else:
            return False

    def esOperador(self,palabra):
        resultado = bool(re.search("(< | > | <=| >= | == | != | ! )", palabra))
        return resultado

    def esFinal(self,palabra):
        if(palabra== "Listo" | palabra== "Devolver"):
            return True
        else:
            return False

    def esValor(self,palabra):
        return

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

    def procesarInstruccion(self,palabra):
        if self.esPalabraReservada(palabra):
            self.formarToken("Palabra Reservada", palabra, self.lineaAtributo)
        elif self.esNombre(palabra):
            self.formarToken("Nombre", palabra, self.lineaAtributo)
        elif self.esComentario(palabra):
            self.formarToken("Comentario", palabra, self.lineaAtributo)
        elif self.esPunto(palabra):
            self.formarToken("Punto", palabra, self.lineaAtributo)
        elif self.esValor(palabra):
            self.formarToken("Valor", palabra, self.lineaAtributo)
        elif self.esOperador(palabra):
            self.formarToken("Operador", palabra, self.lineaAtributo)
        elif self.esFinal(palabra):
            self.formarToken("Final", palabra, self.lineaAtributo)
        elif self.esAritmetica(palabra):
            self.formarToken("Aritmetica", palabra, self.lineaAtributo)
        else:
            print("Error en linea " + str(self.lineaAtributo))
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
    print(sys.argv[1])
    Scanner( sys.argv[1]).leerArchivo()


main()

