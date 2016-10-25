# TAREA 7: README

## Archivos

En la carpeta tarea_07 los archivos son:

- main.py
- cargar_datos.py
- interfaz.ui
- test1.png

## Funcionalidades del Sistema:

### main.py

Al ejecutarse el programa, se abre la interfaz grafica que cuenta con las cuatro opciones de input indicadas en el enunciado
luego la funcionalidad de cada input es relativamente similar:
Para cada input el programa asocia uno o mas viajes al input y para cada viaje, dependiendo si es aereo, terrestre o acuatico
decide que api usar y que parametros agregar a la url inicial:

Antes de hacer el ``requests.get()`` se revisa si el url tiene mas de 2046 caracteres ya que la api no acepta un largo mayor
Finalmente muestra para cada viaje un marker para la ciudad de origen y otro para la ciudad de destino y un path acorde
al tipo de ruta. Los markers tienen la letra C correspondiente a Ciudad.

### cargar_datos.py

Serie de funciones que transforman los datos de los archivos de texto en diccionarios. Y que asigna un color para cada país
de la lista de ciudades. El numero de colores es limitado por lo que si hay muchos paises la funcion falla

### interfaz.ui

Interfaz creada a partir de QtDesigner similar a la expuesta en el enunciado.

### Alcance del Programa

El programa crea todas las rutas solicitadas por el usuario mientras el url no sea mayor a 2046 caracteres. El tamaño del mapa mostrado
es siempre el mismo independiente de que ciudades contenga el viaje, y no se nota la diferencia entre viajes terrestres y aereos
sin embargo en el papel (o código) si son diferentes.


### Indicaciones extras

En el enunciado en el punto 4. se indica lo siguente:

> Ciudades: las ciudades poseen un smbolo caracteristico que sea visible en el mapa. El color de este
simbolo es igual para las ciudades del mismo pais. Recordar que las ciudades se encuentran en el archivo
cities.txt

> Terminales: cada terminal tiene un simbolo caracteristico que depende del tipo y el tamañno. Las
terminales se encuentran en el archivo hubs.txt.

A mi entender estos 2 puntos se contradicen ya que o se marca la ciudad o se marca la terminal en la interfaz gráfica, por
un tema de comodidad y funcionalidad decidí marcar el origen y destino con las ciudades. Sin embargo hacerlo con las terminales sería basicamente
lo mismo solo que se tendría que agregar al parametro markers de la url los siguientes datos:

- size (correspondiente a los 3 tamaños posibles de terminales)
- icon (url a una imágen, uno para cada tipo de terminal)

Mi razón para esto fue que agregar mas parámetros al url final aumentaría la probabilidad de que el largo sea mayor a 2046,
sobre todo por el url del icono.

.
___

Diferencié distintos metodos de creacion de rutas o path, para las rutas aereas y terrestres, ya que considerando que solo hay
6 rutas acuaticas, y que en cada una de ellas se puede llegar al otro destino en linea recta entre ambas ciudades/puertos,
usé el método "aereo" para las rutas acuaticas, ya que en las issues del foro especificaron que solo se iba a probar el programa con 
un subconjunto de los datos entregados.



