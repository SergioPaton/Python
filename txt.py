class SalidaTxt:
    def __init__(self, path) -> None:
        self.__path = path

    def escribir(self, texto):
        f = open(self.__path, 'wt')
        f.write(texto)
        f.close()

    def leer(selft):
        f = open(selft.__path, 'rt')
        texto = f.read()
        f.close()
        return texto


class Escritor:

    def main():
        libro = SalidaTxt('libro.txt')
        oracion = "Y luego está el que espera un golpe de suerte. bHasta que llega y se queda sin dientes"
        print(f'Texto a escribir "{oracion}"\n')
        libro.escribir(oracion)
        print(f'Texto leido: "{libro.leer()}"\n')
        print(
            f'Ambos textos son: {"IGUALES" if oracion==libro.leer() else "DIFERENTES"}')


if __name__ == '__main__':
    Escritor.main()