from manim import *

from componentes import Resistencia, Bobina, VarillaMovil

class Circuito(Scene):
    def construct(self):

        R = Resistencia().shift(LEFT *3 +UP*2)
        L = Bobina().shift(RIGHT*2 + UP*2)
        Varilla = VarillaMovil().shift(RIGHT * 3 + DOWN*1.5)

        #circuito parte de arriba
        cable1 = Line(R.get_right(), L.get_left()).shift(DOWN*0.3)
        cable2 =Line(L.get_right(), L.get_right() + RIGHT*3).shift(DOWN*0.3)
        PARTESUPERIOR = VGroup(R, L, cable1, cable2)
        self.add(PARTESUPERIOR)
        
        
        #circuito partes horizontales
        cable3= Line(R.get_left(), R.get_left() + DOWN*5).shift(DOWN*0.3)
        Varilla.scale([1,3.25,1])
        Varilla.move_to(cable2.get_bottom() + DOWN*2.5, RIGHT*2)
        
    
        
        
        #circuito parte de abajo
        cable4 = Line(cable3.get_bottom(), cable3.get_bottom() + RIGHT*11)
        #iMPORTANTE: cable4 debe añadirse primero para que la varilla se superponga encima
        CABLES= VGroup(cable3, cable4)
        self.add(CABLES)
        self.add(Varilla)
        
        CIRCUITO_RL = VGroup(PARTESUPERIOR,CABLES)
        
        
        