"""
Luis Leyva
Johan Longoria
"""
class AreaFiguras():
    
    def __init__(self):
        self.resultado = 0

    def obtener_resultado(self):
        return self.resultado

    def circulo(self,radio):
    	import math
    	self.resultado = round(math.pi * (radio**2),2)

    def rectangulo(self,lado_a,lado_b):
    	self.resultado = lado_a * lado_b

    def cuadrado(self,lado):
    	self.resultado = lado **2

    def trapezio(self,base_mayor,base_menor,altura):
    	self.resultado = altura * ((base_mayor+base_menor)/2)
