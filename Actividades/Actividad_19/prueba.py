__author__ = 'Ignacio'

dia1 = 13
mes1 = 1
hora1 = 11
min1 = 8
def tiempo(minuto, hora, dia, mes, a):
    dif_min = minuto - a[0]
    print(dif_min)
    dif_hora = hora - a[1]
    print(dif_hora)
    dif_dia = dia - a[2]
    print(dif_dia)
    dif_mes = mes - a[3]
    print(dif_mes)
    if dif_min < 0:
        print(dif_min)
        dif_min += 60
        dif_hora -= 1
    if dif_hora < 0:
        print(dif_hora)
        dif_hora += 24
        dif_dia -= 1
    if dif_dia < 0:
        print(dif_dia)
        dif_dia += 30
        dif_mes -= 1
    tiempo = dif_min + dif_hora*60 + dif_dia*24*60 + dif_mes*24*60*30
    return tiempo
b = "27-01-2015 3:56"
lista = [16,16,13,3]
print(tiempo(39,2,16,3,lista))




