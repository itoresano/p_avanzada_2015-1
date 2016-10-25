# TAREA 2: README

## Archivos:

En la carpeta tarea_02 los archivos que contienen mi codigo son:
* `main.py`
* `Ubicacion.py`
* `Subgrilla.py`
* `carga_matrices.py`

## Funcionalidades del programa:

###Consulta 3:

El programa hace casi todo lo que pide el enunciado menos la consulta 3 que no la realiza
al 100%, mi idea en un principio era hacer una especie de laberinto siendo las murallas la
ubicacion por la que no tenia que pasar y en el caso que no hubiera un camino posible, hacer
una exepcion y poder pasar la menor cantidad de "murallas" posibles. Para esto tenia pensado
usar un **A* algorithm** pero no supe escribir uno por mi cuenta.  Luego trate con un algoritmo
para grafos, pero tampoco dio resultado, asi que deje una funcion que encuentra el camino mas corto
para un grafo.

La funcion asociada a la consulta 3 eso si, crea una estructura de datos en la cual, la ubicacion1
y ubicacion2 estan en los extremos de la estructura, y a partir de eso crea un grafo de nodos


###Consulta 4 y 5:

La forma en que ambas funciones cuentan la cantidad de subgrillas o ubicaciones segun los 
datos ingresados es en forma de cruz, osea solo direccion vertical u horizontal.
Lo hice de esta forma por que asi fue como se aclaró la duda de la consulta 4 y 5
en el foro del repo.

## Clases:

###Ubicacion:
Esta clase es la creadora de los nodos de mi subgrilla, cada nodo tiene su coordenada x e y,
data y zoom correspondiente a su par en la lista multidemensional, aparte se le pueden
settear y obtener las ubicaciones adyacentes para poder recorrer la subgrilla de manera
eficiente.

###Subgrilla:
Esta clase es la que contiene la estructura de datos que se muestra en la interfaz,
solamente se inicializa con el zoom y las coordenadas del centro de la subgrilla y desde
ahi se construyen el resto de los datos, tales como la estructura de datos formada por los 
nodos (instancias de la clase Ubicacion), la lista correspondiente a la estructura, para
desplegarla en la interfaz y la creacion de un grafo para encontrar caminos optimos entre 
los puntos.
También se pueden settear y obtener los valores del zoom, centro y lado de la estructura.
Una de sus funciones es "mover_centro" que basicamente mueve el centro en 4 direcciones
posibles con una magnitud igual al largo del lado de la estructura lo cual genera una
 nueva estructura de datos adyacente a la anterior.

## Funciones extras:
Las funciones que se encuentran en el archivo `carga_matrices` son dos:
* cargar_matriz que basicamente carga a una lista los datos de cada archivo de texto
* encontrar_ubicaciones que retorna una lista con todos los tipos de ubicaciones, pero tambien puede retornar los tipos de continente, pais, comuna etc...









