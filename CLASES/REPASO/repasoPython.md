# Repaso Python
# 1. Tipos de Datos
``"a"``  ***string cadena de texto***

``"hola"`` ***esto tambien es un string***

``"hola soy un string y te saludo"``  ***cadena larga***

### OBSERVACION :todo lo que ete entre comillas es un string
``"100"``

``"False"``

``"hola"``

### un string puede estar entre comillas simples o dobles

``100`` ***este es un tipo de dato numerico entero***

``2.1`` ***es un tipo de dato numerico de tipo flotante float.***

``False`` ***este es un tipo de dato booleano falso***

``True`` ***tipo de dato booleano verdadero***
# 2. Variables
 - ***Es donde almacenamos nuestro tipo de dato 
 esos datos pueden mutar cambiar o modificarse
como creamos una variable para almacenar nuestro datos. darle un nombre significativo o relacionado al dato que estamos almacenando***

-  ***Indiacarle a que dato esta relacionado -> asignacion =***

 - ***indicar el tipo de dato que se va almacenar -> darle el dato a guardar***

 ### primero el dato voy a pedir la edad de nadine
 ``edad_nadine=18``
 ### el nombre de un alumno
 ``nombre_alumno="edwin"``

# 3. Operadores

1. **operadores aritmeticos**
- *suma+*
- *resta-*
- *multiplicacion**
- *divicion /*


*suma* = ``45+12``

*resta* =``45-12``

*multi*=``2*5``

*divi*=``4/2``

*operacion*=``(45+12+23)/4``

**op**=``15+12+14+13/4``
### operadores de uso especial
#### - suma=45+42   *operador suma resultado 87*

#### - suma="45"+12 *operador concatenacion resultado 4512*

#### - saludo="hola"+"mundo" *concatenacion holamundo*

#### - saludo2="hola"+" "+"mundo"  *concatenar hola mundo*

#### - saludos="hola"*2 *holahola*


# 4. Datos Estructurados
### listas
#### puede alamacenar distintos tipos de datos en una sola lista separados por comas
``lista=["nombre",10,False]``

``lista-amigos=["jory","edwin","adan","chinita"]``
### objetos



- tambien al igual que las listas alamacenan distintos tipos de datos con un orden.
- para almacenar datos en un objeto necesitamos especificar un indice y un valor clave->valor
```python
alumno={
     "nombre":"jory",
    "edad":52,
    "sexo":"todos los dias"

}
```

### combinar ambas estructuras de datos
```python
``alumno={

    "nombre":"jory",
    "edad":30,
    "amigos":["anthony","edwin","china"],
    "direccion":{
        "departamento","ayacucho",
        "provincia","lucanas",
        "distrito","puquio",
        "jiron","san piter",
        "numero",152
    }

}
```
``alumnos=[{},{},{}]

# 5. Controles de flujo
## - Decisiones
***solo se ejecuta el codigo si cumple o si la condicion es verdadera, podemos hacer que si la condiciciòn sea falsa se ejecuta otro codigo***
## Sintaxis
***primero especificar el codigo que se ejecutara si cumple una condicion***

``if <condicion>:``

**el codigo que deseamos ejecutar si la condicion es verdadera**
print("ejecuta esto")
**aqui estamos fuera del if o del si este codigo siempre se ejecutara no depende del if**
``print("esto siempre ejecutara")``

### si queremos que se ejecute un codigo en caso sea falso 
```python
if <condicion falsa>:
  print("solo imprime si es verdad")
else:
  print("solo imprime  si es falso")

```
**ejemplito**
```python
if 15>18:
    print("si es verdad imprime esto")
    else:
        print("si es falso imprime esto")

condicion=True
if condicion:
    print("si es verdad imprime esto")
    else:
        print("si es falso imprime esto")

    
        
```
        
        
    





## - Ciclos











