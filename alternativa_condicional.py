#EJERCICIO 1 
#Definí una función inversa, que al aplicarla con un número cualquiera me devuelve el resultado de dividir a 1 por ese número.
def inversa(n):
    if  not n==0:
        return 1/n
    else:
        return 0
print(inversa(4))
print(inversa(0.5))
print(inversa(0))


#EJERCICIO 2 
#Crear una función par_o_impar que acepte como argumento un numero y devuelva el string par si el numero es par, o el string impar si el numero es impar
def par_o_impar(numero):
    if numero%2==0:
        return "es par"
    else:
        return "impar"
print("Ejercicio 2")
print(par_o_impar(2))
print(par_o_impar(3))


#ejercicio 3
#Crear una función positivo_o_negativo que acepte como argumento un numero y devuelva el string positivo si el numero es positivo, o el string negativo si el numero es negativo

def positivo_o_negativo(numero):
    if numero<0:
        return "negativo"
    else:
        return "positivo"
print("Ejercicio 3")
print(positivo_o_negativo(-3))


#Ejercicio 4 
#Crear una función avanzar_semaforo que acepte como argumento un string color_actual y devuelva un string con el siguiente color del semáforo, siguiendo el orden: verde -> amarillo -> rojo -> verde

def  avanzar_semaforo(color_actual):
    if color_actual=="verde":
        return "amarillo"
    elif color_actual=="amarillo":
        return "rojo"
    elif color_actual=="rojo":
        return "verde"
    else:
        return "color incorrecto"

print("Ejercicio 4")

print(avanzar_semaforo('verde') ) # 'amarillo'
print(avanzar_semaforo('amarillo'))# 'rojo'
print(avanzar_semaforo('rojo'))# 'verde'


#Ejercicio 5
#Crear una función obtener_dias_mes que tome como argumento un string mes y devuelva un número dependiendo de la cantidad de días que tenga ese me
def obtener_dias_mes(mes):
    mesCon31=["enero","marzo","mayo","julio","agosto","octubre","diciembre"]
    mesCon30=["abril","junio","septiembre","noviembre"]

    if mes in mesCon31:
        return "Tiene 31 dias"
    elif mes in mesCon30:
        return "Tiene 30 dias"
    else:
        return "Tiene 28 dias"
print(obtener_dias_mes("enero"))
print(obtener_dias_mes("abril"))


#Ejercicio 6
#Crear una función obtener_generacion que tome como argumento un número anio_nacimiento y devuelva un string con la generación a la que pertenece, siguientdo estas reglas:
def obtener_generacion(anio_nacimiento):
    if anio_nacimiento >=1949 and anio_nacimiento<=1968:
        return "Baby boomer"
    elif anio_nacimiento >=1969 and anio_nacimiento<=1980:
        return "Generación X"
    elif anio_nacimiento >=1981 and anio_nacimiento<=1993:
        return "Generacion Millennials" 
    elif anio_nacimiento >=1994 and anio_nacimiento<=2010:
        return "Generación Z"

print("EJERCICIO 7")
print(obtener_generacion(1960))
print(obtener_generacion(1970))
print(obtener_generacion(1982))
print(obtener_generacion(1995))
print(obtener_generacion(1994))
print(obtener_generacion(2010))



#Ejercicio 7
#Crear una función obtener_sensacion que tome como argumento un número temperatura y devuelva un string dependiendo de la temperatura, con las siguientes reglas:



def obtener_sensacion(temperatura):
    if temperatura<0:
        return "¡Está helando!"
    elif temperatura>=0 and temperatura<15:
        return "¡Hace frío!"
    elif temperatura>=15 and temperatura<25:
        return "Está lindo"
    elif temperatura<=25 and temperatura<30:
        return "Hace calor"
    elif temperatura>=30:
        return "Hace mucho calor"
print("Ejercicio 7")
print(obtener_sensacion(0))
print(obtener_sensacion(10))
print(obtener_sensacion(15))
print(obtener_sensacion(16))
print(obtener_sensacion(25))



#Ejercicio 8
#Crear una función obtener_nota que tome como argumento un número puntaje y devuelva un string dependiendo del puntaje redondeado, con las siguientes reglas

def obtener_nota(puntaje):
 
    if round(puntaje) < 6:
        return "Desaprobado"
    elif round(puntaje) >=6 and round(puntaje)<7:
        return "Regular"
    elif round(puntaje)>=7 and round(puntaje)<8:
        return "Bueno"
    elif round(puntaje)>8 and round(puntaje)<9:
        return "Muy bueno"
    elif round(puntaje)==10:
        return "Excelente"
    else :
        return "Puntaje Invalido"
print("Ejercicio 8")
print(obtener_nota(7) )# "Bueno"
print(obtener_nota(9.6)) # "Excelente"
print(obtener_nota(12))  # "Puntaje inválido"

#Ejercicio 9
#Crear una función jugar_piedra_papel_tijera que tome como argumentos dos strings que representen una jugada (piedra, papel, tijera) y dependiendo el devuelva un string con un mensaje avisando qué jugada ganó (o si hubo empate)

def jugar_piedra_papel_tijera(a,b):
    if a=="tijera" and b=="piedra":
        return "gano piedra"
    elif a=="tijera" and b=="papel":
        return "gano tijera"
    elif a=="papel" and b=="tijera":
        return "Gano tijera"
    elif a=="papel" and b=="piedra":
        return "gano papel"
    elif a=="piedra" and b=="tijera":
        return "Gano piedra"
    elif a=="piedra" and b=="papel":
        return "gano papel"
    elif a==b:
        return "Empate!"
    else:
        return "Parametros Invalidos"
print("EJERCICIO 9")
print(jugar_piedra_papel_tijera('tijera', 'piedra'))# ¡Ganó piedra!
print(jugar_piedra_papel_tijera('piedra', 'tijera'))  # ¡Ganó piedra!
print(jugar_piedra_papel_tijera('papel', 'piedra'))  # ¡Ganó papel!
print(jugar_piedra_papel_tijera('piedra', 'papel'))   # ¡Ganó papel!
print(jugar_piedra_papel_tijera('papel', 'tijera'))   # ¡Ganó tijera!
print(jugar_piedra_papel_tijera('tijera', 'papel'))  # ¡Ganó tijera!
print(jugar_piedra_papel_tijera('piedra', 'piedra')) # ¡Empate!
print(jugar_piedra_papel_tijera('papel', 'papel') )   # ¡Empate!
print(jugar_piedra_papel_tijera('tijera', 'tijera'))  # ¡Empate!




# ejercicio 10
#
def celsius_a_farenheit(gradosC):
    gradosFarenheit = gradosC * 1.8 + 32.
    return gradosFarenheit
print(celsius_a_farenheit(0)) 
print(celsius_a_farenheit(10)) 


def farenheit_a_celsius(gradosF):
    gradosCelsius = (gradosF - 32) / 1.8
    return gradosCelsius
print("Ejercicio 10")
print(farenheit_a_celsius(32))
print(farenheit_a_celsius(50))

#ejercicio 11
#
def hace_frio_celsius(grados):
    return grados<8
print("celsius")
print(hace_frio_celsius(10))
print(hace_frio_celsius(0))

def hace_frio_farenheit(grados):
    return hace_frio_celsius(farenheit_a_celsius(grados))

print("hace frio en farenheit")
print(hace_frio_farenheit(50))
print(hace_frio_farenheit(32))

# ejercicio 12
#Trabajamos con tres enteros que representan el nivel de un río en tres días consecutivos 📆. Por ejemplo: medimos los días 1, 2 y 3, y las mediciones son: 22 cm, 283 cm, y 294 cm.

def maximo_entre_tres(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else :
        return c
print(maximo_entre_tres(22, 1, 1))

def minimo_entre_tres(a,b,c):
    if a<b and a<c:
        return a 
    elif b<a and b<c:
        return b 
    else:
        return c
print("Maximo entre")
print(minimo_entre_tres(22, 1, 0))


def dispersion(a,b,c):
    return maximo_entre_tres(a,b,c) -minimo_entre_tres(a,b,c)

print("Dispersion")
print(dispersion(22, 283, 294))

#ejercicio 14
#dias_parejos: son días parejos si la dispersión es chica (menos de 30 cm)
def dias_parejos(a,b,c):
    return dispersion(a,b,c)<30
print("Ejercicio 14")
print(dias_parejos(110, 98, 100)) #True

def dias_locos(a,b,c):
    return dispersion(a,b,c) >100

def dias_normales(a,b,c):
    return not dias_locos(a,b,c) and not dias_parejos(a,b,c)
print(dias_normales(1, 200, 500))


#ejercicio 15
#Definí la función peso_pino, recibe la altura de un pino en metros y devuelve su peso.
#Los pinos se usan para llevarlos a una fábrica de muebles, a la que le sirven árboles de entre 400 y 1000 kilos, un pino fuera de este rango no le sirve a la fábrica.
def peso_pino(metros):
    if metros<=3:
        return (metros*100) * 3
    elif metros>3:
        return (((metros *100)-300)*2) + 900
print("PESO DE PINO") 
print(peso_pino(4))
# Definí la función es_peso_util, recibe un peso en kg y responde si un pino de ese peso le sirve a la fábrica

def es_peso_util(kg):
    return kg >=400 and kg<=1000
#Definí la función sirve_pino, recibe la altura de un pino y responde si un pino de ese peso le sirve a la fábrica.
def sirve_pino(metros):
    return es_peso_util(peso_pino(metros))
print("SIRVE PINO?")
print((sirve_pino(3)))


def punto_para_setenta(carta):
    if carta==1:
        return 5.5
    elif carta==10 or carta==11 or carta==12:
        return  0.5
    else:
        return carta
print(punto_para_setenta(8))