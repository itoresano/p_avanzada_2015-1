# Actividad 15
### Distribución de puntajes

- **R1 (1 puntos):** Test que compruebe credenciales para retirar dinero
- **R2 (1 puntos):** Test que verifique que se saca dinero solo cuando está disponible
- **R3 (1 puntos):** Test que compruebe que una vez retirado el dinero se actualice
- **R4 (1 puntos):** Test que verifique cuenta de un tercero para transferir
- **R5 (1 puntos):** Test que compruebe montos actualizados de las 2 partes
- **R6 (1 puntos):** Test que verifique que la transferencia no se realice si encuentra errores
- **R7 (1 puntos):** Bonus

### Obtenido por el alumno

| R1 | R2 | R3 | R4 | R5 | R6 | R7  | Descuento |
|:--------|:--------|:--------|:--------|:--------|:--------|:--------|:--------|
| 0.7 | 0.8 | 1 | 0.2 | 1 | 1 | 0 | 0 |

| Nota |
|:-----|
| **5.7** |

### Comentarios
* Faltó verificar si el usuario que quiere hacer login existe, pero su clave es incorrecta.
* Al verificar si se saca dinero solo cuando está disponible se debería comparar el dinero que se tenía antes con el nuevo, no si es mayor que 0.
* El test de verificar cuenta de un tercero, es verificar la función buscar_tercero, lo que se hizo fue verificar que la transferencia no se realice si encuentra errores.
