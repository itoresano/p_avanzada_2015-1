# [Actividad 7](https://github.com/IIC2233-2015-1/syllabus/tree/master/Actividades%20en%20Clases/Actividad%2007)

### Distribución de puntajes

Requerimientos (**R**):

* **(1.2 pts)** R1: Leer el archivo correctamente
* **(0.4 pts)** R2: Consulta a
* **(0.4 pts)** R3: Consulta b
* **(0.9 pts)** R4: Consulta c
* **(0.4 pts)** R5: Consulta d
* **(0.9 pts)** R6: Consulta e
* **(0.9 pts)** R7: Consulta f
* **(0.9 pts)** R8: Impresión de consultas

   * Se otorgará 0 pts si se utilizó un enfoque iterativo

**Además, se descontará (0.5) puntos si no sigue formato de entrega.**

### Obtenido por el alumno
| R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | Descuento |
|:--------|:--------|:--------|:--------|:--------|:--------|:--------|:--------|
| 1.2 | 0.4 | 0.3 | 0.9 | 0.4 | 0.2 | 0 | 0.45 |

| Nota |
|:-----|
| **4.85** |

### Comentarios
* La lista `leer` ya es iterable por lo que  no necesitas usar `line for line in leer` en tus métodos; simplemente `leer`.
* Para buscar zurdos, podrías ser más preciso si hicieras un código así:
```python
def chilenos_zurdos():
    chileno_zurdo = list(tuple(filter(lambda x: x[3]=="Chile" and x[4]=="izquierdo",
                                      [line for line in leer])))
    return chileno_zurdo
```
que asi:
```python
def chilenos_zurdos():
    chileno_zurdo = list(tuple(filter(lambda x: "Chileno" in x and "Izuquierda" in x,
                                      [line for line in leer])))
    return chileno_zurdo
```
porque así buscas donde corresponde a la nacionalidad en lugar de arriesgarte a tener coincidencias que no corresponden. Lo otro: pusiste "Chileno" e "Izuquierda" y por eso no funcionaba la consulta xd.

* `goleador()` no te funciona porque:
1. Tus tuplas tienen contenido del tipo `string` y no del tipo `int`, por lo que min no funciona como tú quieres y retorna un string.
2. No estás retornando un objeto del tipo tupla, sino que un `string`, por lo que cuando haces min (x[8], y [9]), x es un string y no la tupla completa.

```python 
def goleador():
    goleador = list(tuple(reduce(lambda x, y: min(x[8],y[9] ), [line for line in leer])))
    return goleador
```
para arreglarlo siguiendo tu forma de escribirlo, debería ser así:
```python
def goleador():
    goleador = list(tuple(reduce(lambda x, y: x if max(int(x[8]),int(y[8]))==int(x[8]) else y, [line for line in leer])))
    return goleador
```
y ahí corre :).

* No se imprimen los chilenos-zurdos como debería u.u. (llegaste a un resultado incorrecto).