from curses import ncurses_version
from logging.config import dictConfig
import re
from shutil import register_archive_format
from xml.dom import registerDOMImplementation
from tp_macowins import *
import pytest


# #####################  Tests de ejercicio 1  #####################

# def test_registrar_un_producto():
#     reiniciar_listas()
#     #registrar_producto(remera_talle_m)
#     registrar_producto({"codigo": 100, "nombre": "remera talle m", "categoria": "remera", "precio": 4500})
#     assert len(codigos) == 1
#     assert len(productos) == 1
#     assert productos[0]["stock"] == 0

# def test_registrar_dos_productos():
#     reiniciar_listas()
#     registrar_producto(remera_talle_s)
#     registrar_producto(remera_talle_m)
#     assert len(codigos) == 2
#     assert len(productos) == 2

# def test_no_registrar_productos_existentes():
#     reiniciar_listas()
#     with pytest.raises(ValueError) as auxiliar:
#         registrar_producto(remera_talle_s)
#         registrar_producto(remera_talle_m)
#         registrar_producto(remera_talle_s)
#     assert str(auxiliar.value) == "Producto ya registrado"
#     assert len(productos) == 2
    

# #####################  Tests de ejercicio 2  #####################

# def test_recarga_de_stock_codigo_inexiste():
#     reiniciar_listas()
#     with pytest.raises(ValueError) as auxiliar:
#         recargar_stock(100, 200)
#     assert str(auxiliar.value) == "Codigo de producto ingresado no existe"
    

# def test_recarga_de_stocks_a_dos_productos():
#     reiniciar_listas()
#     registrar_producto(remera_talle_m)
#     registrar_producto(remera_talle_s)
#     recargar_stock(100, 200)
#     recargar_stock(99, 50)
#     assert productos[0]["stock"] == 200
#     assert productos[1]["stock"] == 50
#     recargar_stock(99, 50)
#     assert productos[1]["stock"] == 100


# #####################  Tests de ejercicio 3  #####################
# # agregar test cn productos registrados y codigos inexistentes
# def func_auxiliar_registra_dos_productos_y_recarga_stock_a_dos():
#     reiniciar_listas()
#     registrar_producto(remera_talle_m)
#     registrar_producto(remera_talle_s)
#     registrar_producto(pulserita)
#     recargar_stock(100, 200)
#     recargar_stock(1098, 200)

# def test_hay_stock_de_un_codigo_inexistente():
#     reiniciar_listas()
#     assert not hay_stock(99)

# def test_hay_stock_de_un_codigo_existente_con_stock():
#     func_auxiliar_registra_dos_productos_y_recarga_stock_a_dos()
#     assert hay_stock(100)

# def test_de_un_codigo_existente_sin_stock():
#     func_auxiliar_registra_dos_productos_y_recarga_stock_a_dos()
#     assert not hay_stock(99)

# def test_de_un_codigo_inexistente_cuando_hay_productos_cargados():
#     func_auxiliar_registra_dos_productos_y_recarga_stock_a_dos()
#     assert not hay_stock(98767)

# #####################  Tests de ejercicio 4  #####################

# def test_calcular_precio_final_si_es_extranejero_y_precio_mayor_a_70_con_precio_original_4500():
#     assert calcular_precio_final(remera_talle_m,True) == 4500
    
# def test_calcular_precio_si_no_es_extranjero_y_precio_es_menor_a_70_con_precio_original_50():
#     assert calcular_precio_final(pulserita,False) == 60.5


# #####################  Tests de ejercicio 5  #####################

# def test_registrar_dos_productos_de_la_misma_categoria_debe_devolver_una_categoria():
#     reiniciar_listas()
#     registrar_producto(remera_talle_m)
#     registrar_producto(remera_talle_s)
#     assert contar_categorias(productos) == 1

# def test_registrar_tres_productos_siendo_dos_de_la_misma_debe_devolver_dos_categorias():
#     reiniciar_listas()
#     registrar_producto(remera_talle_m)
#     registrar_producto(remera_talle_s)
#     registrar_producto(pulserita)
#     assert contar_categorias(productos) == 2


# #####################  Tests de ejercicio 6  #####################

# def func_aux_registra_tres_prod_recarga_stock_de_dos_y_realiza_dos_compras():
#     reiniciar_listas()
#     registrar_producto(remera_talle_m)
#     registrar_producto(remera_talle_s)
#     registrar_producto(pulserita)
#     recargar_stock(100,200)
#     recargar_stock(99,50)
#     realizar_compra(100, 100)
#     realizar_compra(99,50)


# def test_realizar_dos_compras_de_codigo_existente_debe_agregar_dos_ventas():
#     func_aux_registra_tres_prod_recarga_stock_de_dos_y_realiza_dos_compras()
#     assert len(ventas) == 2


# def test_realizar_dos_compras_de_codigo_existente_con_stock_debe_descuentar_sus_stocks():
#     func_aux_registra_tres_prod_recarga_stock_de_dos_y_realiza_dos_compras()
#     assert hay_stock(100)
#     assert not hay_stock(99)


# def test_realizar_una_compra_de_codigo_existente_con_stock_insuficiente():    
#     with pytest.raises(ValueError) as auxiliar:
#         func_aux_registra_tres_prod_recarga_stock_de_dos_y_realiza_dos_compras()
#         realizar_compra(100, 150)
#     assert str(auxiliar.value) == "No hay stock suficiente para la venta"


# def test_realizar_una_compra_de_codigo_existente_con_stock_insuficiente_no_debe_aumentar_ventas():
#     with pytest.raises(ValueError) as auxiliar:
#         func_aux_registra_tres_prod_recarga_stock_de_dos_y_realiza_dos_compras()
#         realizar_compra(100, 150)
#     assert len(ventas) == 2


# def test_realizar_una_compra_de_codigo_inexistente():
#     func_aux_registra_tres_prod_recarga_stock_de_dos_y_realiza_dos_compras()    
#     assert realizar_compra(99999, 10) == "Código incorrecto o cantidad de items no puede ser menor a 1"


# def test_realizar_una_compra_de_0_items_a_codigo_existente():
#     func_aux_registra_tres_prod_recarga_stock_de_dos_y_realiza_dos_compras()    
#     assert realizar_compra(100, 0) == "Código incorrecto o cantidad de items no puede ser menor a 1"


# #####################  Tests de ejercicio 7  #####################

# def test_eliminar_el_producto_sin_stock_de_tres_productos():
#     reiniciar_listas()
#     registrar_producto(remera_talle_m)
#     registrar_producto(remera_talle_s)
#     registrar_producto(pulserita)
#     recargar_stock(100,200)
#     recargar_stock(99,50)
#     discontinuar_productos(productos)
#     assert len(productos) == 2

# def test_eliminar_tres_productos_sin_stock_de_una_lista_de_tres_productos_sin_stock():
#     reiniciar_listas()
#     registrar_producto(remera_talle_m)
#     registrar_producto(remera_talle_s)
#     registrar_producto(pulserita)
#     discontinuar_productos(productos)
#     assert len(productos) == 0

# def test_hay_tres_productos_con_stock_no_deberia_eliminar_ninguno():
#     reiniciar_listas()
#     registrar_producto(remera_talle_m)
#     registrar_producto(remera_talle_s)
#     registrar_producto(pulserita)
#     recargar_stock(100,200)
#     recargar_stock(99,50)
#     recargar_stock(1098,100)
#     discontinuar_productos(productos)
#     assert len(productos) == 3


# #####################  Tests de ejercicio 8  #####################

# def test_realizar_una_compra_del_dia_de_100_unidades_de_un_producto_que_cuesta_4500_debe_devolver_450000():
#     reiniciar_listas()
#     registrar_producto(remera_talle_m)
#     registrar_producto(remera_talle_s)
#     registrar_producto(pulserita)
#     recargar_stock(100,200)
#     recargar_stock(99,50)
#     realizar_compra(100,100)
#     assert valor_ventas_del_dia() == 450000


# #a la lista de ventas se le agrega dos productos comprados con otras fechas
# def test_ventas_del_dia_de_150_unidades_entre_dos_productos_debe_devolver_675000():
#     reiniciar_listas()
#     registrar_producto(remera_talle_m)
#     registrar_producto(remera_talle_s)
#     registrar_producto(pulserita)
#     recargar_stock(100,200)
#     recargar_stock(99,50)
#     realizar_compra(100,100)
#     realizar_compra(99,50)
#     ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
#     ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
#     assert valor_ventas_del_dia() == 675000
    


# #####################  Tests de ejercicio 9  #####################


# def test_cuatro_ventas_dos_de_este_año_debe_devovler_dos_ventas_del_anio():
#     reiniciar_listas()
#     registrar_producto(remera_talle_m)
#     registrar_producto(remera_talle_s)
#     registrar_producto(pulserita)
#     recargar_stock(100,200)
#     recargar_stock(99,50)
#     realizar_compra(100,100)
#     realizar_compra(99,50)
#     ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
#     ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
#     assert len(ventas_del_anio()) == 2 


# #####################  Tests de ejercicio 10  #####################

# def test_tres_productos_mas_vendidos_debe_devolver_los_nombres_de_los_tres_productos_mas_vendidos_en_orden_ascendente():
#     reiniciar_listas()
#     registrar_cinco_productos()
#     recargar_stock_a_cinco_productos()
#     realizar_compra_a_cinco_productos()
#     assert productos_mas_vendidos(3)  == ["pantalon talle m", "campera talle l", "pulserita de tela verde"]


# #####################  Tests de ejercicio 11  #####################

# def test_en_una_lista_de_cinco_productos_actualizar_precio_a_categoria_remera_mal_escrita_en_un_50_porciento_debe_actualizar_el_precio_a_6750():
#     reiniciar_listas()
#     registrar_cinco_productos()
#     actualizar_precios_por_categoria(" reMera ",50)
#     assert productos[0]["precio"] == 6750
#     assert productos[1]["precio"] == 6750


# def test_actualizar_precio_a_categoria_accesorios_mal_escrita_en_50_porciento_debe_actualizar_el_precio_a_75():
#     reiniciar_listas()
#     registrar_cinco_productos()
#     actualizar_precios_por_categoria(" aCceSoriOs",50)
#     assert productos[2]["precio"] == 75








# #funciones auxiliares
# def registrar_cinco_productos():
#     registrar_producto(remera_talle_m)
#     registrar_producto(remera_talle_s)
#     registrar_producto(pulserita)
#     registrar_producto(campera_talle_l)
#     registrar_producto(pantalon_talle_m)

# def recargar_stock_a_cinco_productos():
#     recargar_stock(100,200)
#     recargar_stock(99,200)
#     recargar_stock(1098,200)
#     recargar_stock(555,200)
#     recargar_stock(444,200)

# def realizar_compra_a_cinco_productos():
#     realizar_compra(100,25)
#     realizar_compra(99,50)
#     realizar_compra(1098,100)
#     realizar_compra(555,150)
#     realizar_compra(444,200)
class Local:
    def __init__(self):
        self.productos=[]
        self.codigo=[]
        self.ventas=[]
        
        
    def reiniciar_listas(self):
    
        self.productos.clear()
        self.ventas.clear()
        self.codigo.clear()

    

    def registrar_producto(self,objeto):
        
        if  objeto.codigo_producto() in self.codigo:
            raise ValueError("Producto ya registrado")
        else:

            
            self.productos.append(objeto.descripcion_producto())
            #self.productos[0]["stock"]=0
            objeto.descripcion_producto().update({"stock":0})
            self.codigo.append(objeto.codigo_producto())

    def recargar_stock(self,codigo,stock):
    
        if codigo not in self.codigo:
            raise ValueError("Codigo de producto ingresado no existe")
        else:
            for producto in self.productos:
                if producto["codigo"] == codigo:
                    producto["stock"] += stock


    def hay_stock(self,codigo):
        for producto in self.productos:
            if producto["codigo"] == codigo and producto["stock"] > 0:
                return True
    
        return False

    def contar_categorias(self):
        categorias = []
        for producto in self.productos: 
            if producto["categoria"] not in categorias:
                categorias.append(producto["categoria"])
        return len(categorias) 

    def realizar_compra(self,codigo_de_producto, cantidad_de_items_a_comprar):
    
        for producto in self.productos:
            if producto["codigo"] == codigo_de_producto and cantidad_de_items_a_comprar > 0:
                hay_stock_para_vender = producto["stock"] - cantidad_de_items_a_comprar
                if hay_stock_para_vender < 0:
                    raise ValueError('No hay stock suficiente para la venta')   
                else:
                    producto["stock"] = hay_stock_para_vender
                    venta = {
                    "codigo_producto": producto["codigo"],
                    "cantidad": cantidad_de_items_a_comprar,
                    "fecha": hoy,
                    "precio_total": producto["precio"] * cantidad_de_items_a_comprar
                    }
                    self.ventas.append(venta)
            
    
    def discontinuar_productos(self):
        
        dic_aux = self.productos[:]
        for producto in dic_aux:
            if producto["stock"] == 0:
                self.productos.remove(producto)

    def valor_ventas_del_dia(self):
        suma_ventas_del_dia = 0
        subtotal = 0
        for venta_de_hoy in self.ventas:
            if venta_de_hoy["fecha"] == hoy:
                subtotal = venta_de_hoy["precio_total"] #* venta_de_hoy["cantidad"]
                suma_ventas_del_dia += subtotal
        return suma_ventas_del_dia

    def ventas_del_anio(self):
        ventas_del_anio_actual = []
        anio_actual = hoy[:4]
        for producto in self.ventas:
            if producto["fecha"][:4] == anio_actual:
                ventas_del_anio_actual.append(producto)
        return ventas_del_anio_actual

    def productos_mas_vendidos(self,cantidad):
        lista_mas_vendidos = []
        nombres_mas_vendidos = []
        for producto_venta in self.ventas:
            for producto in self.productos:
                if producto["codigo"] == producto_venta["codigo_producto"]:
                    producto_y_cantidad = {
                        "nombre": producto["nombre"],
                        "cantidad": producto_venta["cantidad"]
                    }
                    lista_mas_vendidos.append(producto_y_cantidad)
        ventas_ordenadas_may_a_menor = sorted(lista_mas_vendidos, key=itemgetter("cantidad"), reverse=True)
        for producto in ventas_ordenadas_may_a_menor:
            if producto["nombre"] not in nombres_mas_vendidos:
                nombres_mas_vendidos.append(producto["nombre"])
        return nombres_mas_vendidos[:cantidad]

    def actualizar_precios_por_categoria(self,categoria,porcentaje):
    
        categoria_reconocida = categoria.lower().strip()
        for producto in self.productos:
            if producto["categoria"] == categoria_reconocida:
                producto["precio"] += producto["precio"] * porcentaje / 100

    def buscar_prenda_por_codigo_devoler_stock(self,codigo):

        for i in self.productos:
            if i["codigo"]==codigo:
                return i["stock"]


            



class Prenda:
    def __init__(self,diccionario):

        self.diccionario=diccionario
    
    def calcular_precio_final(self, es_extranjero):

        if self.diccionario["precio"] > 70 and es_extranjero:
            return self.diccionario["precio"]
        else:
            costo_final = self.diccionario["precio"] * 1.21
            return costo_final
    
    def nueva(self,diccionario):
        
    
    def promocion(self,descontarPromocion):
        self.diccionario["precio"]-=descontarPromocion


    def descripcion_producto(self):
       return self.diccionario
    def nombre_producto(self):
        return self.diccionario["nombre"]
    def codigo_producto(self):
        return self.diccionario["codigo"]
    def categoria_producto(self):
        return self.diccionario["categoria"]
    def precio_producto(self):
        return self.diccionario["precio"]
    
    
  

nuevolocal=Local()
remera_m=Prenda(remera_talle_m)
pulsera=Prenda(pulserita)
remera_s=Prenda(remera_talle_s)
campera_l=Prenda(campera_talle_l)
pantalon_m=Prenda(pantalon_talle_m)

def realizar_compra_a_cinco_productos():
    nuevolocal.realizar_compra(100,25)
    nuevolocal.realizar_compra(99,50)
    nuevolocal.realizar_compra(1098,100)
    nuevolocal.realizar_compra(555,150)
    nuevolocal.realizar_compra(444,200)

def recargar_stock_a_cinco_productos():
    nuevolocal.recargar_stock(100,200)
    nuevolocal.recargar_stock(99,200)
    nuevolocal.recargar_stock(1098,200)
    nuevolocal.recargar_stock(555,200)
    nuevolocal.recargar_stock(444,200)
def registrar_cinco_productos():
    nuevolocal.registrar_producto(remera_m)
    nuevolocal.registrar_producto(remera_s)
    nuevolocal.registrar_producto(pulsera)
    nuevolocal.registrar_producto(campera_l)
    nuevolocal.registrar_producto(pantalon_m)


####################EJERCICIO 1############################
def test_se_agregra_productos_a_lista_():
    nuevolocal=Local()
    nuevolocal.registrar_producto(remera_m)
    assert len(nuevolocal.productos)==1
def test_se_agregra_productos_repetido_se_espera_el_RAISE_exception():
    nuevolocal=Local()
    nuevolocal.reiniciar_listas()
    with pytest.raises(ValueError) as auxiliar:

        nuevolocal.registrar_producto(pulsera)
        nuevolocal.registrar_producto(pulsera)
        
    assert str(auxiliar.value) == "Producto ya registrado"

def test_al_REGISTRAR_producto_se_espera_que_ingrese_con_stock_en_0():

    nuevolocal=Local()
    nuevolocal.reiniciar_listas()
    nuevolocal.registrar_producto(pulsera)
    assert nuevolocal.buscar_prenda_por_codigo_devoler_stock(1098)==0
    
def test_registro_2_productos_se_espera_que_productos_tenga_2():
    nuevolocal=Local()
    nuevolocal.reiniciar_listas()
    nuevolocal.registrar_producto(pulsera)
    nuevolocal.registrar_producto(remera_m)
    assert len(nuevolocal.productos) ==2

####################EJERCICIO 2############################
def test_recarga_stock_20_a_un_producto_devuelve_20():
    nuevolocal.reiniciar_listas()
    nuevolocal.registrar_producto(remera_m)
    nuevolocal.recargar_stock(100,20)
    assert nuevolocal.buscar_prenda_por_codigo_devoler_stock(100)==20

def test_cargar_stock_con_codigo_inexistente_en_productos_devuelve_exepcion():
    nuevolocal.reiniciar_listas()
    with pytest.raises(ValueError) as auxiliar:
        nuevolocal.recargar_stock(1000,10)
    assert str(auxiliar.value) == "Codigo de producto ingresado no existe"
    assert len(nuevolocal.productos)==0

####################EJERCICIO 3############################

def test_no_hay_stock_en_un_producto_recien_registrado_deberia_dar_false_():
    nuevolocal.reiniciar_listas()
    nuevolocal.registrar_producto(remera_m)
    assert not nuevolocal.hay_stock(100)

def test_cargar_stock_a_un_producto_registrado_y_preguntar_si_tiene_stock_devuelve_True_():
    nuevolocal=Local()
    nuevolocal.registrar_producto(remera_m)
    nuevolocal.recargar_stock(100,100)
    assert nuevolocal.hay_stock(100)



# def test_foo():
#     remera_m=Prenda(remera_talle_m)
#     assert remera_m.diccionario==remera_talle_m
#     print(remera_m.diccionario)

##################ejercicio 4###################
def test_precio_final_remera_m_y_sea_turista_es_4500():
    
    assert remera_m.calcular_precio_final(True)==4500

def test_precio_final_pulserita_y_no_sea_turista_es_60_5():
    
    assert pulsera.calcular_precio_final(False)==60.5
##############ejercicio 5################
def test_agrego_2_productos_distintas_categorias_deberia_devolver_2():
    nuevolocal=Local()
    nuevolocal.reiniciar_listas()
    nuevolocal.registrar_producto(remera_m)
    nuevolocal.registrar_producto(pulsera)
    assert nuevolocal.contar_categorias()==2

def test_registrar_2_productos_misma_categoria_devuelve_1():
    nuevolocal=Local()
    nuevolocal.reiniciar_listas()
    nuevolocal.registrar_producto(remera_m)
    nuevolocal.registrar_producto(remera_s)
    assert nuevolocal.contar_categorias()==1

######################ejercico 6#######################3

def test_realizar_una_comora_de_un_producto_decrementa_su_stock_De_100_a_80():
    nuevolocal=Local()
    nuevolocal.reiniciar_listas()
    nuevolocal.registrar_producto(remera_m)
    nuevolocal.recargar_stock(100,100)
    nuevolocal.realizar_compra(100,20)
    assert nuevolocal.buscar_prenda_por_codigo_devoler_stock(100)==80


def test_al_realizar_una_compra_se_agregar_el_producto_a_ventas_y_largo_de_ventas_es_1():
    nuevolocal=Local()
    nuevolocal.reiniciar_listas()
    nuevolocal.registrar_producto(remera_m)
    nuevolocal.recargar_stock(100,100)
    nuevolocal.realizar_compra(100,20)
    assert len(nuevolocal.ventas)==1

def test_al_realizar_una_compra_se_agregar_el_producto_a_ventas_y_largo_de_ventas_es_2():
    nuevolocal=Local()
    nuevolocal.reiniciar_listas()
    nuevolocal.registrar_producto(remera_m)
    
    nuevolocal.recargar_stock(100,100)
    nuevolocal.realizar_compra(100,20)
    nuevolocal.realizar_compra(100,10)
    assert len(nuevolocal.ventas)==2


###########################ejercico 7##############################


def test_remueve_todos_los_productos_con_stock_en_0():
    nuevolocal.reiniciar_listas()
    nuevolocal.registrar_producto(remera_m)
    nuevolocal.registrar_producto(remera_s)
    nuevolocal.discontinuar_productos()
    assert len(nuevolocal.productos)==0

def test_elimina_el_producto_sin_stock_de_tres_productos_la_lista_productos_debe_ser_2():
    nuevolocal.reiniciar_listas()
    nuevolocal.registrar_producto(remera_m)
    nuevolocal.registrar_producto(remera_s)
    nuevolocal.registrar_producto(pulsera)
    nuevolocal.recargar_stock(100,200)
    nuevolocal.recargar_stock(99,50)
    nuevolocal.discontinuar_productos()
    assert len(nuevolocal.productos) == 2

def test_hay_tres_productos_con_stock_no_deberia_eliminar_ninguno_largo_de_Lista_debe_ser_3():
    nuevolocal.reiniciar_listas()
    nuevolocal.registrar_producto(remera_m)
    nuevolocal.registrar_producto(remera_s)
    nuevolocal.registrar_producto(pulsera)
    nuevolocal.recargar_stock(100,200)
    nuevolocal.recargar_stock(99,50)
    nuevolocal.recargar_stock(1098,100)
    nuevolocal.discontinuar_productos()
    assert len(nuevolocal.productos) == 3

###########################ejercico 8##############################
# def valor_ventas_del_dia():
#     suma_ventas_del_dia = 0
#     subtotal = 0
#     for venta_de_hoy in ventas:
#         if venta_de_hoy["fecha"] == hoy:
#             subtotal = venta_de_hoy["precio_total"] #* venta_de_hoy["cantidad"]
#             suma_ventas_del_dia += subtotal
#     return suma_ventas_del_dia

def test_realizar_una_compra_del_dia_de_100_unidades_de_un_producto_que_cuesta_4500_debe_devolver_450000():
    
    nuevolocal.reiniciar_listas()
    nuevolocal.registrar_producto(remera_m)
    nuevolocal.registrar_producto(remera_s)
    nuevolocal.registrar_producto(pulsera)
    nuevolocal.recargar_stock(100,200)
    nuevolocal.recargar_stock(99,50)
    nuevolocal.realizar_compra(100,100)
    assert nuevolocal.valor_ventas_del_dia() == 450000

#a la lista de ventas se le agrega dos productos comprados con otras fechas
def test_ventas_del_dia_de_150_unidades_entre_dos_productos_debe_devolver_675000():
    nuevolocal.reiniciar_listas()
    nuevolocal.registrar_producto(remera_m)
    nuevolocal.registrar_producto(remera_s)
    nuevolocal.registrar_producto(pulsera)
    nuevolocal.recargar_stock(100,200)
    nuevolocal.recargar_stock(99,50)
    nuevolocal.realizar_compra(100,100)
    nuevolocal.realizar_compra(99,50)
    nuevolocal.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    nuevolocal.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    assert nuevolocal.valor_ventas_del_dia() == 675000


    # #####################  Tests de ejercicio 9  #####################


def test_cuatro_ventas_dos_de_este_año_debe_devovler_dos_ventas_del_anio():
    nuevolocal.reiniciar_listas()
    nuevolocal.registrar_producto(remera_m)
    nuevolocal.registrar_producto(remera_s)
    nuevolocal.registrar_producto(pulsera)
    nuevolocal.recargar_stock(100,200)
    nuevolocal.recargar_stock(99,50)
    nuevolocal.realizar_compra(100,100)
    nuevolocal.realizar_compra(99,50)
    nuevolocal.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    nuevolocal.ventas.append({"codigo_producto":100,"cantidad":10,"fecha":"31-12-1990","precio_total":45000})
    assert len(nuevolocal.ventas_del_anio()) == 2
# #####################  Tests de ejercicio 10  #####################

def test_tres_productos_mas_vendidos_debe_devolver_los_nombres_de_los_tres_productos_mas_vendidos_en_orden_ascendente():
    nuevolocal.reiniciar_listas()
    nuevolocal.registrar_producto(pantalon_m)
    nuevolocal.registrar_producto(campera_l)
    nuevolocal.registrar_producto(pulsera)
    nuevolocal.registrar_producto(remera_s)
    nuevolocal.registrar_producto(remera_m)
    recargar_stock_a_cinco_productos()
    realizar_compra_a_cinco_productos()

    
    assert nuevolocal.productos_mas_vendidos(3)  == ["pantalon talle m", "campera talle l", "pulserita de tela verde"]


# #####################  Tests de ejercicio 11  #####################

def test_en_una_lista_de_cinco_productos_actualizar_precio_a_categoria_remera_mal_escrita_en_un_50_porciento_debe_actualizar_el_precio_a_6750():
    nuevolocal.reiniciar_listas()
    registrar_cinco_productos()
    nuevolocal.actualizar_precios_por_categoria(" reMera ",50)
    assert nuevolocal.productos[0]["precio"] == 6750
    assert nuevolocal.productos[1]["precio"] == 6750


def test_actualizar_precio_a_categoria_accesorios_mal_escrita_en_50_porciento_debe_actualizar_el_precio_a_75():
    nuevolocal.reiniciar_listas()
    registrar_cinco_productos()
    nuevolocal.actualizar_precios_por_categoria(" aCceSoriOs",50)
    assert nuevolocal.productos[2]["precio"] == 75