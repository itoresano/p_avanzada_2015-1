# TAREA 4: README

## Archivos

En la carpeta tarea_04 los archivos son:

- main.py
- drag.py
- Clases.py
- PyTest.py
- conftest.py
- interfaz.ui

## Funcionalidades del Sistema:

### Main

Para iniciar el programa y abrir la interfaz gráfica se debe ejecutar el archivo main.py, con lo que se abre la interfaz
gráfica. Luego para poder trabajar en la interfaz, el método es el siguiente, se pueden agregar 3 "tipos" de bloques:

 - Input
 - Operación (suma, resta, multiplicación etc..)
 - Output
 
El input corresponde a un numero, la operación corresponde al signo de la operación pedida y el output es el bloque en 
que se quiere mostrar el resultado final de la operación completa
Una vez que tenemos todos los bloques que necesitamos para nuestra operación, realizamos las conexiones entre
bloques, esto se logra, seleccionando el checkbox de cada bloque y luego apretando el botón "Realizar conexiones".
En los casos en que el orden de las partes de la operación importan, (resta, división, potencia) hay que realizar la
conexión del primer termino primero y luego la del segundo por separado: Ejemplo, si queremos calcular 10-3, primero 
seleccionamos el bloque 10 y el bloque - y conectamos, luego seleccionamos el bloque 3 y el bloque - y conectamos.
Ejemplo general, si queremos calcular (3+2)x(5+1) seleccionamos los bloques 3, + y 5, apretamos en realizar conexión,
luego seleccionamos los bloques 5, + y 1 y apretamos en realizar conexiones, luego seleccionamos ambos bloques +
y el bloque x y nuevamente apretamos en realizar conexiones, finalmente seleccionamos el bloque x y el bloque output
y apretamos el botón. Como resultado final el bloque que anteriormente tenía como texto "output" ahora tiene como texto
el resultado de la operación.

### drag.py

El archivo drag.py define los dos objetos que hay en el área de trabajo, uno es el "dropbox" o el área de trabajo en si
misma que tiene la propiedad de que los objetos en el puedan ser arrastrados. El otro objeto es un "DraggableWidget"
es decir un Qwidget normal de PyQt4 pero con la propiedad de ser arrastrable, este "DraggableWidget" es hijo del 
dropbox. Cada DraggableWidget tiene como atributo su posición dentro del dropbox y también su tipo (numero, operación o 
output), el tipo es una clase dentro de las clases definidas en el modulo clase.py.

### Clases.py

En el módulo Clases.py se definen las clases correspondientes a los tipos de bloques que se pueden agregar al área de
trabajo (Numero, Suma, Resta, ... , Output). Las clases correspondientes a operaciones matemáticas tienen cada una un
atributo "hijos" que es una lista de widgets, es decir el bloque +, tiene como atributo ``` self.tipo = Suma()```, 
si es que se quiere sumar 3 + 5, luego de realizar la conexión entre los 3 bloques, los hijos del bloque + son los
bloques 3 y 5. También cada clase correspondiente a operaciones matemáticas contiene un método que retorna un booleano
según si se puede agregar un hijo o no, por ejemplo si el bloque + ya tiene 2 hijos (ya que solo recibe 2 entradas), el
método retorna False, también retorna False si es que se quiere hacer una operación prohibida (ejemplo 0 en el
denominador, es decir el valor del hijo que se quiere agregar como 2do hijo sea 0) y finalmente tiene un método que
calcula la operación matemática correspondiente según los hijos del bloque.

### PyTest.py y conftest.py

Para testear las funciones matemáticas del programa, cree una nueva clase (Widget), que emula el atributo ``` self.tipo``` 
de la clase DraggableWidget, ya que instanciar esa clase en el modulo PyTest.py me resulto imposible, pero ambas tienen
el atributo ```self.tipo``` que es una instancia de una de las clases del modulo Clases.py. Por lo tanto lo que hice fue
testear las operaciones entre Widgets.

### interfaz.ui

Este archivo corresponde a la interfaz gráfica diseñada en QtDesigner.

## Alcance del programa:

En el código que escribí se pueden realizar todas las funcionalidades pedidas menos la de borrar conexiones singulares,
la cual se puede hacer borrando los bloques conectados, pero no se pueden borrar las conexiones exclusivamente.
El programa tiene sus debilidades, tales como empezar a hacer conexiones entre muchos bloques sin que estas operaciones
tengan lógica, en ese caso lo peor que podría pasar es que el output tome como valor None. También otra "falla" es que 
el programa no es amigable con los errores, es decir si el usuario crea una conexión involuntariamente, tendrá que
borrar todos los bloques de la conexión y crearlos de nuevo para que funcione bien el programa. Sin embargo si el
programa se utiliza bien no deberían haber mas errores.