from math import prod
from tp_macowins import *
import pytest

class PorPrecio:
    def __init__(self,codigo):
        
        self.codigo=codigo

    def correponde_al_producto(self,productos,valor):
        
        for producto in productos:
            if producto["codigo"]==self.codigo and producto["precio"]<valor:
                producto["precio"]= valor
class PorStock:
    def __init__(self,codigo):
        self.codigo=codigo
    
        self.stock=Local()
    def correponde_al_producto(self,productos,valor):
        for producto in productos:
            if producto["codigo"]==self.codigo and producto["stock"]>0:
                producto["precio"]= valor

        
