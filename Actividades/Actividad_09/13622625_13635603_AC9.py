from random import randint, choice

__author__ = 'figarrido'

NOMBRES = ['Karim', 'Christian', 'Belen', 'Patricio', 'Jaime',
           'Marco', 'Rodrigo', 'Felipe', 'Antonio', 'Ian']

TAREAS = ['Hacer el papeleo', 'Depositar los sueldos',
          'Descansar', 'Comer', 'Tomar cafe',
          'Organizar la reunion', 'Agregar datos al sistema',
          'Jugar con las sillas', 'Revisar CV\'s',
          'Marcar entrada']


class MetaPersona(type):
    def __new___(meta, nombre, base_clases, diccionario):
        if nombre in ["Persona", "Jefe", "Empleado"]:
            return super().__new__(meta, nombre, base_clases, diccionario)
        else:
            print("La clase que esta intentando crear no esta correctamente escrita")
        def hacer_tarea(self, tarea = None):
            print("Tarea: {0}, Nombre: {1}".format(self.tareas_realizadas[-1], self.nombre))

            


class MetaEmpresa(type):
    def __new__(meta, nombre, base_clases, diccionario):
        if nombre == "Jefe":
            return super().__new__(meta, nombre, base_clases, diccionario)
        else:
            print("La clase que esta intentando crear no esta correctamente escrita")
        def nuevo_empleado(self, persona):
            self.empleados[persona] = persona
        def subir_sueldo(self, empleado, value):
            self.empleados[empleado].sueldo += value


class Empresa(metaclass=MetaEmpresa):
    pass


    def __init__(self, boss):
        self.boss = boss
        self.empleados = {}


class Persona(metaclass=MetaPersona):
    def __init__(self, nombre, edad, **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return '{} is {} years old'.format(self.nombre, self.edad)


class Empleado(Persona):
    id_actual = 0

    def __init__(self, sueldo, **kwargs):
        super().__init__(**kwargs)
        self.sueldo = sueldo
        self.id_empleado = Empleado.id_actual
        Empleado.id_actual += 1
        self.tareas_realizadas = []

    def __str__(self):
        return super().__str__() + '\nID: {} - Sueldo: {}'.format(self.id_empleado, self.sueldo) + '\n'


class Jefe(Empleado):
    def __init__(self, **kwargs):
        self.password = 'Tu jefecito lindo'
        super().__init__(**kwargs)


if __name__ == '__main__':

    System = Empresa(Jefe(nombre='Pedro', edad=30, sueldo=1000000))

    """
    Agrega 10 empleados en la empresa
    """
    for _ in range(10):
        System.nuevo_empleado(Empleado(nombre=NOMBRES[_], edad=randint(20, 40),
                                       sueldo=randint(500000, 800000)))
    """
    Muestra a los empleados
    """
    for ID in System.empleados:
        print(System.empleados[ID])

    """
    Elige al azar al empleado del mes
    """
    empleado_del_mes = System.empleados[choice(list(System.empleados))]

    System.subir_sueldo(empleado_del_mes.id_empleado, 'Tu jefecito lindo')

    print('El empleado del mes es: {} y su sueldo quedo en ${}\n'.format(
        empleado_del_mes.nombre, empleado_del_mes.sueldo))

    """
    A cada empleado le asigna una tarea
    """
    for ID in System.empleados:
        System.empleados[ID](choice(TAREAS))

    print(Empresa(empresa=System))
