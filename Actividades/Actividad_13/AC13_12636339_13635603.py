__author__ = 'Victor Vidaurre'
import random
import simpy

class Cliente:
    def __init__(self, env, id_cliente, tiempo_atencion):
        self.env = env
        self.id = id_cliente
        self.tiempo_aburrimiento = random.uniform(50, 90)
        self.tiempo_en_fila = tiempo_atencion


def llega_cliente(env, cliente, caja):
    print('{0} llega al banco en {1:.2f}.'.format(cliente.id, env.now))
    with caja.cajas.request() as solicitud:
        yield solicitud
        print('{0} entra a la caja {2} en {1:.2f}.'.format(cliente.id, env.now, caja.id))
        yield env.process(caja.atender(cliente.id))
        print('{0} deja la caja {2} en {1:.2f}.'.format(cliente.id, env.now, caja.id))
        caja.cola -= 1

class Caja:
    def __init__(self, env, tiempo_atencion, iden):
        self.id = iden
        self.env = env
        self.cajas = simpy.Resource(env, capacity=1)
        self.tiempo_atencion = tiempo_atencion
        self.cola = 0

    def atender(self, llega_cliente):
        yield self.env.timeout(round(random.expovariate(1/self.tiempo_atencion) + 0.5))

def configuracion_sim(env, num_cajas, tiempo_atencion, tiempo_llegada):
    caja = []
    for i in range(1, num_cajas+1):
        caja.append(Caja(env, tiempo_atencion, i))
    lista_largos = []
    for i in caja:
        lista_largos.append(i.cola)
    j = 0

    while True:
        yield env.timeout(round(random.expovariate(1/tiempo_llegada) + 0.5))
        j += 1
        cliente = Cliente(env, j, tiempo_atencion)
        caja_elegida = min(lista_largos)
        for i in caja:
            if i.cola == caja_elegida:
                i.cola += 1
                env.process(llega_cliente(env, cliente, i))
                break

if __name__ == "__main__":
    numero_cajas = int(input("Ingrese el número de cajas: "))
    numero_tiempo = int(input("Ingrese el tiempo maximo"))
    env = simpy.Environment()
    tiempo_atencion = 15
    tiempo_llegada = 10
    env.process(configuracion_sim(env, numero_cajas, tiempo_atencion, tiempo_llegada))
    env.run(until=1000)



