# Actividad 21
### Distribución de puntajes
| R1 | R2 | R3 | R4 | Bonus | Descuento |
|:--------|:--------|:--------|:--------|:--------|:---|
| 1 | 1 | 1.2 | 0 | 0 | 0 |

| Nota |
|:-----|
| **4.2** |

- **R1 (1.50 pts):** Validar que el usuario del sistema sea un cajero para entrar al sistema.
- **R2 (1.00 pts):** Conectar los m ́etodos de la interfaz, otorg ́andole funcionalidad.
- **R3 (1.75 pts):** Definición de la clase cliente de forma que permita ser serializada con los datos pedidos.
- **R4 (1.75 pts):** Generar el archivo de salida – por cliente – en la carpeta ClientesDB con el nombre de la forma id.walkcart
- **Bonus (0.60 pts)** Para el administrador, que pueda entrar con el nombre WalkcartUnlimited y generar el archivo TOP.walkcart con los datos solicitados.

### Comentarios
- R1: validas pero no dices si hubo o no un error. Simplemente pareciera que no funciona el botón
- No te pedían guardar el último gasto. Solo te pedían el acumulado.
- La gestión de archivos está mal hecha. Si vas a leer un archivo, entonces debes abrirlo con el flag w, si lo vas a leer entonces el flag debe ser r. No puedes leer y escribir un archivo con el mismo objeto File. 
