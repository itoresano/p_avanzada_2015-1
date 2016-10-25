# debes definir la metaclase 'Meta' a continuacion
def crear_property(tipo, valor):
    def setter(self, valor):
        pass
    def getter(self):
        return self.value

    return property(getter, setter)



class Meta(type):
    def __new__(meta, clase, base, dic):
        return super().__new__(meta, clase, base, dic)


# debes definir las clases 'Person' y 'Company' a continuacion

class Person(metaclass = Meta):
    name = str
    age = int


class Company(metaclass = Meta):
    name = str
    stock_value = float
    employees = list

# El resto es para probar tu programa
if __name__ == '__main__':

    c = Company()
    c.name = 'Apple'
    c.stock_value = 125.78
    c.employees = ['Tim Cook', 'Kevin Lynch']

    print(c.name, c.stock_value, c.employees, sep=', ')

    p = Person()
    p.name = 'Karim'
    p.age = 'hola'
    # Esto debiese imprimir 'ERROR'

    print(p.name, p.age, sep=', ')
