# Actividad 18
### Distribución de puntajes

- **R1 (3.0 puntos):** Crear la interfaz con todos sus widgets en Qt Designer
- **R2 (1.0 puntos):** Al solicitar una nueva operación, se generan número aleatorios (coherentes con la
operación) y son mostrados en la interfaz
- **R3 (1.0 puntos):** Al revisar la respuesta, ésta es verificada correctamente según lo que respondió el usuario y se entrega el feedback correcto (i.e: avisa cuado es correcto o incorrecto).
- **R4 (1.0 puntos):** Informar al usuario cuál es el valor correcto de la operación.


### Obtenido por el alumno

| R1 | R2 | R3 | R4 | Descuento |
|:--------|:--------|:--------|:--------|:--------|
| 2.5 | 1 | 0.7 | 1 | 0.3 |

| Nota |
|:-----|
| **5.9** |

### Comentarios
* Este código cumple con lo que se pide pero está malo
```python
def calcular(self):
    if self.label_signo.text() == "+":
        self.primer_num.setText(str(random.randint(0, 20)))
        self.segundo_num.setText(str(random.randint(0, 20)))
            
    if self.label_signo.text() == "-":
        self.primer_num.setText(str(random.randint(0,20)))
        self.segundo_num.setText(str(random.randint(0,int(self.primer_num.text()))))
    
    if self.label_signo.text() == "*":
        self.primer_num.setText(str(random.randint(0,20)))
        self.segundo_num.setText(str(random.randint(0,20)))
    
    if self.label_signo.text() == "/":
        self.primer_num.setText(str(random.randint(0,20)))
        self.segundo_num.setText(str(random.randint(1,20)))
```
Cada vez que se haga un llamado a ```calcular()``` tu código va a verificar que ```label_signo```  sea suma, resta, multiplicación y división.
Este flujo debe ser manejado con ```if```, ```elif``` y ```else```. Descuento de 0.3
* Los textbox se usan para ingresar cosas, no como labels. Para los operandos había que utilizar labels. De hecho ocurre que puedo cambiar los valores de los operando y eso no debería pasar.
* Solo debe haber un intento por operación