def puede_ver_pelicula(edad, tiene_autorizacion):
    return edad>=15 or tiene_autorizacion
print(puede_ver_pelicula(12, False)) # False
print(puede_ver_pelicula(12, True) ) # True
print(puede_ver_pelicula(16, False) )# True
print(puede_ver_pelicula(18, True) ) # True



#Ejercicio 2
# Crear una función esta_en_rango que tome como argumentos tres números, un valor, un número minimo y un número maximo, y devuelva si el valor se encuentra entre los números minimo y maximo (si el valor es igual a uno de los extremos se considera que está dentro del rango)

def esta_en_rango(valor, minimo, maximo):
    return valor>=minimo and valor<=maximo

print("EJERCICIO 2")
print(esta_en_rango(3, 1, 10))# True
print(esta_en_rango(1, 1, 10))# True
print(esta_en_rango(10, 1, 10))# True
print(esta_en_rango(12, 1, 10))# False
print(esta_en_rango(-3, 1, 10))# False


#EJERCICO 3
#Crear una función puede_avanzar que tome como argumento un string con el color del semáforo y devuelva si puede avanzar.
def puede_avanzar(colo_semaforo):
    return colo_semaforo=="verde" 
print("Ejercicio 3")
print(puede_avanzar('verde'))# True
print(puede_avanzar('amarillo'))# False
print(puede_avanzar('rojo') )# False


#Ejercicio 4
#Crear una función es_vocal que tome como argumento un string letra y devuelva si letra es una vocal.
def es_vocal(letra):
    vocales=["a","e","i","o","u"]
    return letra in vocales
print("Ejercicio4")
print(es_vocal('a'))# True
print(es_vocal('n'))# False

#ejercicio 5
#Crear una función es_consonante que tome como argumento un string letra y devuelva si es una consonante
def es_consonante(letra):
    return  not es_vocal(letra)
print("EJERCICIO 5")
print(es_consonante('a')) # False
print(es_consonante('n'))# True
print(es_consonante('z'))



#Ejercicio 6 
#Crear una función es_hora_valida que tome como argumento un string hora con el formato HH:mm y determine si es una hora válida del día o no
def es_hora_valida(hora):
    horas, minutos= str.split(hora,":")
    return int(horas)<=24 and int(minutos)<=60
print("EJERCICIO6 6")
print(es_hora_valida('12:23'))# True
print(es_hora_valida('12:65'))# False
print(es_hora_valida('28:05'))# False
print(es_hora_valida('00:00'))# True


# EJERCICIO 7
#Crear una función puede_renovar_carnet que tome como argumentos tres booleanos, paso_test, tiene_multas_impagas y pago_impuestos, y devuelva si una persona está habilitada para renovar su carnet de conducir. Una persona puede renovar su carnet si pasó los tests, no tiene multas impagas y pagó todos los impuestos

def puede_renovar_carnet(paso_test, tiene_multas_impagas, pago_impuestos):
    return paso_test and not tiene_multas_impagas and  pago_impuestos
print("EJERCICIO 7")

print(puede_renovar_carnet(True, True, True))# False
print(puede_renovar_carnet(True, True, False))# False
print(puede_renovar_carnet(True, False, True))# True
print(puede_renovar_carnet(True, False, False))# False
print(puede_renovar_carnet(False, True, True))# False
print(puede_renovar_carnet(False, True, False))# False
print(puede_renovar_carnet(False, False, True))# False
print(puede_renovar_carnet(False, False, False))# False
  
   
#Ejercicio 8
#Crear una función puede_graduarse que tome como argumentos dos números asistencia y materias_aprobadas y un booleano tesisAprobada, y devuelva si una persona puede gruadarse. Una persona puede graduarse si tiene un 75% de asistencia o más, 50 materias aprobadas o más y la tesis aprobada.
def puede_graduarse(asistencia, materias_aprobadas, tesisAprobada):
    return asistencia>=75 and materias_aprobadas>=50 and tesisAprobada
print("EJercicio 8")
print(puede_graduarse(80, 50, True))# True
print(puede_graduarse(80, 50, False))# False
print(puede_graduarse(80, 45, True))# False
print(puede_graduarse(80, 45, False))# False
print(puede_graduarse(65, 50, True))# False
print(puede_graduarse(33, 55, False))# False
print(puede_graduarse(42, 45, True))# False
print(puede_graduarse(28, 45, False))# False 
  
 
  
#Ejercicio 9
#Definí una función comienza_con_a que, al aplicarla con un string, me diga si el mismo comienza con la letra ‘a’, sin importar si la palabra está escrita en minusculas o mayúsculas
def comienza_con_a(palabra):
    return str.startswith(palabra,"a") or str.startswith(palabra,"A")
print("EJERCICIO 9")
print(comienza_con_a("aguja")) #true
print(comienza_con_a("AGUA")) #true
print(comienza_con_a("bote")) #false
  

#ejercicio 10
#Definí la función es_multiplo_de_3 que dice si un número se puede dividir por 3. Por ejemplo:  
def es_multiplo_de_3(n):
    return n%3==0
print("Ejercicio 10")
print(es_multiplo_de_3(9)) # true  
print(es_multiplo_de_3(4)) #false
print(es_multiplo_de_3(27))#true
print(es_multiplo_de_3(10))#false


#ejercicio 11
#Definí la función es_bisiesto que indica si un año tiene 366 días.
def es_bisiesto(anio):
    return anio%400==0 or anio%4==0
print("ejercicio 11")
print(es_bisiesto(2000))
print(es_bisiesto(2024))
print(es_bisiesto(2008))

