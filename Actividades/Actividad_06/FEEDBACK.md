# [Actividad 6](https://github.com/IIC2233-2015-1/syllabus/tree/master/Actividades%20en%20Clases/Actividad%2006)

### Distribución de puntajes

Requerimientos (**R**):

* **(1.0 pts)** R1: Implementación de la función generadora de la integral
* **(1.0 pts)** R2: Correcto llamado de la función que calcula energía dependiendo del tipo
* **(1.0 pts)** R3: Implementación de la función generadora de los tiempos
* **(1.0 pts)** R4: Implementación de ciclo que va generando cada paso
* **(1.0 pts)** R5: Plotear los datos
* **(1.0 pts)** R6: Calidad del código
   * Parten con 1.0 punto que va disminuyendo cada vez que se incurra en malas prácticas como:
        * Código poco legible
        * Lineas innecesarias
        * Etc

**Además, se descontará (0.5) puntos si no sigue formato de entrega.**

### Obtenido por el alumno
| R1 | R2 | R3 | R4 | R5 | R6 | Descuento |
|:--------|:--------|:--------|:--------|:--------|:--------|:--------|
| 0 | 1.0 | 0.5 | 0.5 | 0 | 0.6 | 0.2 |

| Nota |
|:-----|
| **3.4** |

### Comentarios
* No implementaste bien la función de la energía solar.
* La keyword `yield` para que se use optimamente, debes utilizarla dentro de un ciclo. Por ejemplo en tu código de la función `energia_acumulada haces esto`
```python
	def energia_acumulada(tipo):
    n = 5
    k = 0
    yield calcular_energia(tipo)(k/n)
    if k <= 1440:
        k += 1
```
Para que funcione correctamente y agrege valores al `generator` debiste hacer esto
```python
	def energia_acumulada(tipo):
    n = 5
    k = 0
    if k <= 1440:
    	yield calcular_energia(tipo)(k/n)
        k += 1
```
* No implementaste ninguna función integradora.