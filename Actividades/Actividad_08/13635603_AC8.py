# Crea aquí tus decoradores
def guardar_instancias(clase):
    instancias = []
    prev_init = getattr(clase, "__init__")
    def new_init(self, *args):
        instancias.append(clase)
        self.instancias = instancias
        prev_init(self, *args)
    setattr(clase, "__init__", new_init)
    return clase

def comparar_por(tipo):
    diametro = getattr(Hamburguesa, "diametro")
    def comparar(self, h1, h2):
        if h1.diametro > h2.diametro:
            return h1 > h2 is True
        if h1.diametro < h2.diametro:
            return  h1 < h2 is True
        if h1.diametro == h2.diametro:
            return h2 == h1 is True


def cambiar_precio(precio_bruto_a_neto):
    iva = 1.23
    def cambiar(precio_bruto):
        precio_nuevo = precio_bruto_a_neto(precio_bruto)*iva/1.19
        return precio_nuevo
    return cambiar



# Debes descomentar las tres líneas comentadas para probar tus decoradores

@guardar_instancias
@comparar_por('diametro')
class Hamburguesa:

    def __init__(self, altura, diametro, cantidad_carnes):
        self.altura = altura
        self.diametro = diametro
        self.cantidad_carnes = cantidad_carnes


    def __repr__(self):
        return ('Hamburguesa de {0} cm de altura, '
                '{1} cm de diametro y '
                '{2} carnes').format(self.altura, self.diametro,
                                     self.cantidad_carnes)


@cambiar_precio
def precio_bruto_a_neto(precio_bruto):
    return (precio_bruto * 1.19 + 100)

if __name__ == "__main__":
    hamburguesa1 = Hamburguesa(10, 15, 2)
    hamburguesa2 = Hamburguesa(7, 10, 1)
    hamburguesa3 = Hamburguesa(10, 10, 2)

    print(hamburguesa2 > hamburguesa1)
    print(hamburguesa2 == hamburguesa3)
    print(hamburguesa1 < hamburguesa3)

    print(Hamburguesa.instancias)
    hamburguesa4 = Hamburguesa(12, 20, 4)
    print(Hamburguesa.instancias)

    print(precio_bruto_a_neto(2000))

#