# Actividad 11
### Distribución de puntajes

- **R1 (1.8 puntos):** Clase abstracta `Figura`, con todos los métodos pedidos.
- **R2 (1.4 puntos):** Clase `Circulo`, completamente implementada.
- **R3 (1.4 puntos):** Clase `Rectangulo`, completamente implementada.
- **R4 (1.4 puntos):** Clase `Triangulo`, completamente implementada.
- **B  (2.0 puntos):** Bonus de vértices con generador y `map`
- **La asignación de puntaje será menor si se implementaron métodos de forma innecesaria**

### Obtenido por el alumno

| R1 | R2 | R3 | R4 | B | Descuento |
|:--------|:--------|:--------|:--------|:--------|:--------|
| 2.0 | 1.8 | 1.8 | 0.2 | 0 | 0 |

| Nota |
|:-----|
| **6.8** |

### Comentarios
* Toda figura tiene un centro, es inherente a la clase, debia ser una property de figura no de sus subclases
* __repr__ tambien es inherente a figura, solo cambiaba el nombre de la clase , y hacia referencia a cosas que posee cada figura: area, perimetro, centro
* Todo bien, solo algunos detalles que se arreglan con modelacion, y 0.2 de bonus por hacer la traslacion pero no como se pedia con map