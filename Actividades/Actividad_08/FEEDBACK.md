# [Actividad 8](https://github.com/IIC2233-2015-1/syllabus/tree/master/Actividades%20en%20Clases/Actividad%2008)

### Distribución de puntajes

Requerimientos (**R**):

* **(2.0 pts)** R1: Decorador `guardar_instancias`
* **(2.0 pts)** R2: Decorador `comparar_por`
* **(2.0 pts)** R3: Decorador `cambiar_precio`

**Además, se descontará (0.5) puntos si no sigue formato de entrega.**

### Obtenido por el alumno
| R1 | R2 | R3 | Descuento |
|:--------|:--------|:--------|:--------|
| 1.4 | 1.5 | 2 | 0 |

| Nota |
|:-----|
| **5.9** |

### Comentarios
* No compiló. Tienes que preocuparte de que funcione el programa antes de entregar
* Tenías que hacer el "comparar_por" genérico para cada atributo. Revisa como se hace en la pauta. Lo hiciste espeíficamente con el diámetro. Te falto agregar ```setattr``` después de la función comparar para cambiar la función con el decorador
* En la función 'guardar_instancias' pusiste ```self.instancias = instancias```, pero ahí no estabas llamando a la clase recién creada. De hecho por eso cuando pones ```Hamburguesa.instancias```lanza una excepción, ya que nunca creaste el atributo instancias.  También te faltó ```setattr(clase, 'instancias', list())```
