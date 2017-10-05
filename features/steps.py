# -*- coding: utf-8 -*-
from lettuce import step, world
from AreaFiguras import AreaFiguras

@step(u'Dado que ingreso el radio "([^"]*)"')
def dado_que_ingreso_el_radio_group1(step, rad):
	world.area = AreaFiguras()
	world.area.circulo(int(rad))

@step(u'Dado que ingreso los lados "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_el_radio_group1(step, ladoa, ladob):
	world.area = AreaFiguras()
	world.area.rectangulo(int(ladoa),int(ladob))

@step(u'Dado que ingreso el lado "([^"]*)"')
def dado_que_ingreso_el_radio_group1(step, lado):
	world.area = AreaFiguras()
	world.area.cuadrado(int(lado))

@step(u'Dado que ingreso "([^"]*)" , "([^"]*)" , "([^"]*)"')
def dado_que_ingreso_el_radio_group1(step, base_mayor,base_menor,altura):
	world.area = AreaFiguras()
	world.area.trapezio(float(base_mayor),float(base_menor), int(altura))

@step(u'cuando realizo la operación')
def cuando_realizo_la_operacion(step):
    pass

@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
    assert float(esperado) == world.area.obtener_resultado(), 'El resultado esperado es '+esperado+ ' y el obtenido es '+str(world.area.obtener_resultado())

