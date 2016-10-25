# TAREA 5: README

## Archivos

En la carpeta tarea_05 los archivos son:

- main.py
- patiwi.py
- Monedas.py
- Pocmon.py
- Timer.py
- belenciwi.py
- marquiwi.py
- jaimiwi.py
- mapa.txt
- partidas
- imagenes

## Funcionalidades del Sistema:

### Main

Para iniciar el programa y abrir la interfaz gráfica se debe ejecutar el archivo main.py, con lo que se abre la interfaz
gráfica. Luego para poder trabajar en la interfaz, aparecen 3 botones:

 - NUEVA PARTIDA
 - GUARDAR PARTIDA
 - CARGAR PARTIDA
 
"NUEVA PARTIDA" comienza una nueva partida desde cero.
"CARGAR PARTIDA" habre una nueva pantalla con una lista de partidas antiguas (contenidas en la carpeta partida) mas un
 cuadro de texto en el cual si escribimos el numero de la partida se puede cargar la partida.
 "GUARDAR PARTIDA" Guarda la partida actual, es decir en cero.

### Pocmon.py

En este archivo se maneja al pocmon, la principal funcionalidad es de revisar si es que el movimiento del pocmon esta
permitido o no, la forma de revisarlo es que si el siguiente pixel en la direccion que va el pocmon no es una 
muralla el pocmon se mueve, si no deja de moverse, sin embargo hay un pequeño ajuste, si esque se cambia de direccion 
para tratar de doblar en una esquina, el programa admite que se apriete el boton, 5 pixeles antes de la posicion ideal o
5 pixeles despues, lo que hace el programa es que mueve al pocmon a la posicion ideal.
Ejemplo: la esquina esta en (100,100) si el pocmon esta en (100,95) y se aprieta la tecla para cambiar de direccion el programa
automaticamente mueve al pocmon al lugar (100,100) con la direccion de movimiento cambiada.
Tambien hay un thread que da una señal al metodo TryMove del pocmon cada 0,01 segundos, por lo que el pocmon avanza a 
100 pixeles por segundo

### Patiwi.py, Belenciwi.py, jaimiwi.py, marquiwi.py

Estos archivos controlan el movimiento de los fantasmas de forma muy parecida al pocmon, los fantasams se mueven de
forma aleatorioa, ya que no tuve tiempo de programas los alogritmos a-star necesarios. Si tocan al pocmon el pocmon pierde 
una vida, y belenciwi se come las monedas rojas. 



### Timer.py 

Esta clase controla el tiempo que se despliega en la clase board, gracias a un thread que envia una señal cada 1 segundo

### Especificaciones.

Achique las imagenes del pacman y de los fantasmas ya que no supe modificar su tamaño dentro de la interfaz grafica
es por eso que los nombres de las imagenes son diferentes, el tamaño usado fue de 25x25 pixeles para todas las imagenes.

## Alcance del programa:

El codigo que escribi permite jugar una partida normal de pacman, sin embargo las funciones de cargar partias esta
un poco bugueada, el fin del juego (cuando las vidas se acaban) también esta bugueado.
Las partidas se guardan en un archivo .pacman, donde el nombre del archivo es la fecha en el momento en que se guardo.