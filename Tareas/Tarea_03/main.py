__author__ = 'Ignacio'



if __name__ == '__main__':
    parte = input("Desea ejecutar la Parte_I o la Parte_II (ingrese Parte_I/Parte_II)")
    tiempo = int(input("Ingrese el tiempo de simulacion"))
    if parte == "Parte_I":
        import Parte_I
        s = Parte_I.Supermercado(tiempo)
        s.run()
    if parte == "Parte_II":
        import Parte_II
        Parte_II.env.run(until=tiempo)
        Parte_II.archivo_clientes()
        Parte_II.archivo_informe()
