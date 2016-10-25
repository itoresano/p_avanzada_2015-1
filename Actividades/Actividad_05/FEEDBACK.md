# [Actividad 5](https://github.com/IIC2233-2015-1/syllabus/tree/master/Actividades%20en%20Clases/Actividad%2005)
### Distribución de puntajes

* **(1.0 pts)** Requerimiento 1: Acceso correcto a las estaciones del mapa.
* **(3.0 pts)** Requerimiento 2: Decir si existe o no un camino.
* **(2.0 pts)** Requerimiento 3: Impresión del camino.

| Requerimiento 1 | Requerimiento 2 | Requerimiento 3 | Descuento |
|:--------|:--------|:--------|:--------|
| 1.0 | 0.8 | 0.5 | 0.5 |

| Nota |
|:-----|
| **2.8** |

### Comentarios
* Al parecer no lograste terminar el método, traté de arreglarlo de varias formas. Primero porque tus `if`s en `direcciones[contador]` se salían del rango. Debiste hacer que tu función recursiva vaya guardando el camino que lleva ingresándoselo como parámetro. Creo que intestaste hacer eso en el `else` del `reset`, pero al crear `reset +=1` sin haber creado la variable `reset` antes, el programa se cae.
* El contador nunca regresa a 0, vuelve a 2.
* Luego de varios arreglos logré que printeara `(True, [Estacion 1, Estacion 2, Estacion 7, Estacion 12, Estacion 11, Estacion 10, Estacion 10])`, it's something.
