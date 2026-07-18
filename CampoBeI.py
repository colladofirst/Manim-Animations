from manim import *

class CampoB(VGroup):
 def __init__(
        self,
        x_range=(-2, 2),
        y_range=(-1, 1),
        spacing_x=2.25,
        spacing_y=2.5,
        tam_cruz=0.12,
        color=GREEN,
        **kwargs
    ):
        super().__init__(**kwargs)

        cruces = VGroup()

        for x in range(x_range[0], x_range[1] + 1):
            for y in range(y_range[0], y_range[1] + 1):

                cruz = VGroup(
                    Line(tam_cruz * UL, tam_cruz * DR),
                    Line(tam_cruz * DL, tam_cruz * UR),
                ).set_color(color)

                cruz.move_to(np.array([x * spacing_x, y * spacing_y, 0]))
                cruces.add(cruz)

        self.campo = cruces

        self.add(self.campo)


class TestCampoB(Scene):
    def construct(self):
        campo = CampoB()
        self.add(campo)
        
class CorrienteInd(VGroup):
    def __init__(
        self,
        radio=0.5, 
        color=BLUE,
        sentido="antihorario",
        **kwargs
    ):
        super().__init__(**kwargs)
        
        if sentido == "antihorario":
            flecha = CurvedArrow(
                start_point=DOWN * radio,
                end_point=LEFT * radio,
                angle= 11*PI/6,
                color=color,
                stroke_width=6,  #anchura linea
                tip_length=0.2,  #tamaño punta flecha
            )
        elif sentido == "horario":
            flecha = CurvedArrow(
                start_point=DOWN * radio,
                end_point=RIGHT * radio,
                angle= PI*3/4,
                color=color,
                stroke_width=6,
                tip_length=1,
            )
        else:
            raise ValueError("El sentido debe ser 'horario' o 'antihorario'.")
        
        texto= MathTex(r"I").move_to(flecha.get_center()).set_color(color).scale(1.25).set_z_index(1)
        
        fondo = Circle(radius=radio*3, 
                       fill_color=BLACK, #Cambiar si tu fondo es de otro color
                       fill_opacity=1,
                       stroke_width=0    #no borde
                       ).move_to(flecha.get_center()).set_z_index(0)
                
        Corriente= VGroup(fondo, flecha, texto)
        Corriente.move_to(ORIGIN)
        self.add(Corriente)

class TestCorrienteInd(Scene):
    def construct(self):
        corriente = CorrienteInd()
        self.add(corriente)
        
            