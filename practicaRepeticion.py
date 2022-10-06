#ejercicio 1
"""Definí una función obtener_indice que tome como argumento un valor cualquiera valor y un lista cualquiera lista y devuelva el índice del primer ítem con dicho valor en la lista, o -1 si no hay ninguno."""


def obtener_indice(valor,lista):
    posicion=0
    if valor in lista:
        #Si valor esta dentro de la lista itero la lista ,sino retorno -1
        for i in lista:
            if i==valor:   
                return posicion
            else :
                posicion+=1
        return posicion
    else :
        return -1

#ejercicio 2
#Definí una función repetir que tome como argumento un valor valor y un número entero cantidad, y devuelva una lista con valor repetido cantidad de veces.


def repetir(valor, cantidad):
    
    
    #lista+= [valor]* cantidad
    return [valor for i in range(cantidad)]

#ejercicio 3
#Definí una función sumar_impares_hasta que tome como argumento un número numero y que devuelva la suma de todos los impares empezando desde 0 hasta dicho numero inclusive.

def sumar_impares_hasta(numero):
    suma=0
    for i in range(numero+1):
     
        
        if not i%2==0:
            print(i)
            suma+=i
            
    return suma  
#ejercicio 4
#Definí una función cuenta_regresiva que tome como argumento un número entero numero_inicial y que devuelva un lista con cuyo primer ítem sea numero_inicial y los demás ítems sean números enteros sucesivos descendientes, hasta llegar a 0.

def cuenta_regresiva(numero_inicial):
    listaRegresiva=[]
    
    for i in range(numero_inicial+1):
        print(i)
        listaRegresiva+=[numero_inicial-i]
    return listaRegresiva


#ejercicio 4
#Definí una función invertir que tome como argumento un lista lista y que devuelva un lista con los mismos valores pero en orden invertido.

def invertir(lista):
    contadorNeg=0
    nueva=[]
    for i in lista:
        contadorNeg=contadorNeg-1
        nueva+=[lista[contadorNeg]]
    return nueva

#print([5, 7, 99, 34, 54, 2, 12][::-1])

#Definí una función remover_duplicados que tome como argumento un lista lista y que devuelva un lista con los mismos valores de lista pero sin valores duplicados.

def remover_duplicados(lista):
    a=[]
    """for i in lista:
        if i not in nuevalist:
            #si el primer elemento de LISTA no esta en mi nuevlist, lo agrego a mi nuevalist
            #si el segundo elemento ....
            nuevalist+=[i]"""
    [a.append(i) for i in lista if i not in a]
    return a

#ejercicoo 5
#Definí una función repetir_letras que tome como argumento un string palabra y un número entero cantidad, y devuelva una string donde cada letra de palabra esté repetida cantidad de veces.


def repetir_letras(palabra,cantidad):
    palabrax=""
    for i in palabra:
        
        palabrax+=i*cantidad
    return palabrax

#ejercicio 6
#Definí una función capitalizar_palabras tome como argumento un string string y devuelva un string donde cada palabra está capitalizada (con la primera letra máyuscula). Dejar las demás letras como están.

def capitalizar_palabras(string):
    capitalizada=""
    contador=0
    for i in string.split():
        contador+=1
        capitalizada+=i.title()+" "       
            
        

            
    return capitalizada     

#ejercicio 7

def sumar_seccion(lista, comienzo, cantidad):
    suma=0
    for i in lista[comienzo:comienzo+cantidad]:
        suma+=i
    return   suma


#ejercicio 8
#Definí una función es_subconjunto que tome como argumento dos listas, subconjunto y conjunto, y devuelva True si subconjunto es realmente subconjunto de conjunto, es decir, si todos los valores de subconjunto están en conjunto.

def es_subconjunto(subconjunto,conjunto):
    sub=0
    return False not  in [i in conjunto for i in subconjunto]
# recorro subconjunto y pregunto si en cada iteracion de subconjunto esta en conjunto
#la lista comprimida me devuele booleanos
#si false no se encuentra en la lista comprimida ,devuelve true

#ejercicio 9
#Definí una función tiene_bloque que tome como argumento un lista lista y devuelva True si dicho lista tiene un bloque de 3 o más ítems consecutivos idénticos, o False si no tiene.


def tiene_bloque(lista):
    
    return [lista[i] for i in range(len(lista)) if lista[i]==lista[2]]
   #incompleto     


#ejercicio 10
#Definí una función es_palindromo que tenga como parámetro un string palabra y devuelva True si dicha palabra es palíndroma, es decir, si puede leerse de igual manera de izquierda a derecha que de derecha a izquierda, o False sino.
def es_palindromo(palabra):
    return "".join(invertir(palabra)) == palabra



#ejercicio 10 
#Definí un procedimiento agregar_al_principio que agregue un elemento al principio de una lista (y no al final, como lo haría push)
unos_numeros = [3, 5, 9]
unos_strings = ["mundo", "!"]
def agregar_al_principio(lista,elemento):
   global unos_numeros
   global unos_strings
   lista=[elemento]+lista
   print(lista)
      
        
