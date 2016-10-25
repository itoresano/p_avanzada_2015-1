# TAREA 3: README

## Archivos:

En la carpeta tarea_03 los archivos son:

 - main.py
 - Parte_I.py
 - Parte_II.py
 - cargar_archivos.py
 
## Funcionalidades del Sistema:

###General:

Para ejecutar el sistema se debe correr el archivo main.py y luego ingresar los parámetros pedidos por el programa
La parte I tanto como la parte II entregan los 3 archivos.csv pedidos en el enunciado sin embargo, en el archivo
reporte no se calculó el promedio del largo de las colas por cajas abiertas.

### Parte_I:

La parte I utiliza el método de simulación por eventos discretos, para esto use un método no muy elegante, por lo que
voy a explicar cómo funciona y por qué lo hice asi.
El programa elige el valor mínimo entre distintos tiempos de (atención en caja, llegada, compra, salida etc.) que
corresponden a los eventos del enunciado. Para cada cliente el programa funciona así: antes que el evento suceda,
el tiempo del evento es un número muy grande, cuando el evento sucede (es decir despues de que suceda el evento 
anterior, se setea el valor real del evento), y cuando el evento finaliza, el tiempo del evento pasa a ser un valor muy
grande nuevamente. La principal razón de porque lo hice así es que utilice la función min la cual me devuelve un error al evaluarla en una lista vacia o con alguna valor None en la lista (e.g cuando no hay 
 clientes en el supermercado etc.) y no se me ocurrió como hacerlo sin ese método.


### Parte_II

El orden de los procesos en la parte II es el siguiente: 

1. Mientras el super esté abierto llega un auto (con un cliente adentro) al estacionamiento.
2. Se estaciona, o se pone a la fila para estacionarse según prioridad.
3. Genera su carro de compras con el mismo metodo de la parte I.
4. Elige una caja según las colas, verifica si se tienen que abrir o cerrar cajas.
5. Entra a la Cola de la caja
6. Compra producto por producto
7. Sale de la caja pagando todo

En medio de eso revisa si el supermercado debe cerrar o abrir. Tiene un error que no supe arreglar que es que el evento 
de cerrar el supermercado se imprime muchas veces en la consola, se la razón del error (lo definí dentro de un while)
pero no supe donde más definirlo para lograr un mejor resultado.

## Clases:

Cada parte cuenta con 3 clases cada una: Supermercado, Cliente y Caja/Cola (I y II respectivamente)


## Alcance del programa:

Revisando a última hora me di cuenta que no agregue los productos a cada caja ni que definí la probabilidad de que 
los clientes compren productos en cajas y ya no me queda tiempo para hacerlo. De todos modos la manera de hacerlo sería
la misma que como se llena el carro solo que visitando un solo pasillo y para cada evento aumentar en 1$ la probabilidad
de compra por segundo que pasa, es decir si el tiempo del evento de llegar a la cola fue 10 y el siguiente evento fue 
en el tiempo 13: 
```
probablidad_compra = probablidad*(1,01)**(13-10)
```
y ahí calcular si es que se compra o no el producto.

