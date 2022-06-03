#automata que acepte cadenas binarias 0|1 que sean pares

class Automata:
    def __init__(self, cadena, automata):
        self.cadena = cadena
        self.automata = automata

    def NumerosBinarios(self):
        self.estado = 1
        
        for i in range(0, len(self.cadena)):
            self.transicion = self.cadena[i]
            if self.estado == 1:
                if str.isdigit(self.transicion):
                    if self.transicion == '1' or self.transicion == '0':
                        self.estado = 2
                    else:
                        return False
                else:
                        return False
            
            elif self.estado == 2:
                if str.isdigit(self.transicion):
                    if self.transicion == '1':
                        self.estado = 2
                    elif self.transicion == '0':
                        self.estado = 3
                    else:
                        return False
                else:
                    return False
            
            elif self.estado == 3:
                if str.isdigit(self.transicion):
                    if self.transicion == '0':
                        self.estado = 3
                elif self.transicion == '1':
                    self.estado = 2
                else:
                    return False
            else:
                return False

        if self.estado == 3:
            return True
        else:
            return False

    def main():
        cadena = input("Introduce Numero Binarios Pares: ")
        AFD = Automata(cadena)
        if AFD.NumerosBinarios() == True:
            print("El numero binario es par: ", cadena,"\n")
        else:
            print("El numero binario no es par \n")
    if __name__ == "__main__":
        main()