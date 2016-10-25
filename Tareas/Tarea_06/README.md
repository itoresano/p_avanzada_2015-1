# TAREA 6: README

## Archivos

- Cliente.py
- hashnsalt.py
- main.py
- Servidor.py
- passwords.420

## Funcionalidades del sistema

### Inicio:

Para inciciar el sistema se debe ejecutar el archivo main.py, se abrirá una ventana para iniciar sesión en el 
iChat-DCC, también se dará la opción de crear una registrarse si es que no se cuenta con un usuario y una contraseña
registrada. Para registrarse el programa pide un mail, el cual se chequea segun "regex" que termine por @puc.cl o @uc.cl,
pide un usuario, el cual se revisa si es que ya existe o no, esto no logré hacerlo con regex ya que por lo que entendí,
regex solo revisa "patrones" dentro de un str y no supe como hacer para que compare un string (el usuario) con una lista
de otros strings (los usuarios ya registrados) por lo que use un simple metodo ``==``. Para guardar la contraseña use
el método hash + salt, gracias a la libreria hashlib y almacene el usuario mas las contraseña "hasheada+salt" en un diccionario
serializado en el archivo "passwords.420"


### Sistema de Chat:

Lamentablemente no pude cumplir con el enunciado en la funcionalidad del chat, la funcionalidad de mi chat es parecida
a la de un foro, un cliente envia un mensaje al servidor y el servidor lo reenvia a todos los clientes y lo muestra en 
su ventana de chat.

### Servidor:

La clase servidor se instancia apenas se ejecura el archivo main.py, la cual tiene 2 threads que manejan las funciones 
escuchar y aceptar, cuando el servidor acepta un cliente lo guarda en un diccionario, y cuando le llega un mensaje lo 
reenvia a todos los clientes del diccionario.

### Cliente:

El cliente es basicamente un QWidget que tiene una funcion escuchar, la cual esta manejada por un QThread, cada vez que 
el cliente recibe un mensaje (la funcion escuchar lo decodifica) este se agrega al layout de la instancia Cliente y se 
muestra en pantalla.





