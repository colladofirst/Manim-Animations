from manim import *

class CampoB(VGroup):
    def __init__(
        self,
        x_range=(-2, 2),
        y_range=(-1, 1),
        spacing_x=2.25,
        spacing_y=2.5,
        tam=0.12,
        sentido="-k", #+i,-i,+j,-j,+k,-k
        color=GREEN,
        **kwargs
    ):
        super().__init__(**kwargs)
        
        self.campo= VGroup()
        
        if sentido == "+i":
                    Campo = VGroup(
                        Arrow(LEFT * tam*10, RIGHT * tam*20, buff=0).shift(UP*0.5),
                        Arrow(RIGHT * tam*-10, RIGHT * tam*20, buff=0),
                        Arrow(RIGHT * tam*-10, RIGHT * tam*20, buff=0).shift(DOWN*0.5),
                    ).set_color(color).set_stroke_width(6)
                    
                    Campo.move_to(ORIGIN)
                    self.campo.add(Campo)
                    
        elif sentido == "-i":
            Campo = VGroup(
                        Arrow(RIGHT * tam*10, LEFT * tam*20, buff=0).shift(UP*0.5),
                        Arrow(RIGHT* tam*10, LEFT * tam*20, buff=0),
                        Arrow(RIGHT * tam*10, LEFT * tam*20, buff=0).shift(DOWN*0.5),
                    ).set_color(color).set_stroke_width(6)
            Campo.move_to(ORIGIN)
            self.campo.add(Campo)
            
        elif sentido == "+j":
            Campo = VGroup(
                Arrow(UP * tam*-10, UP * tam*20, buff=0).shift(RIGHT*0.5),
                Arrow(UP * tam*-10, UP * tam*20, buff=0),
                Arrow(UP * tam*-10, UP * tam*20, buff=0).shift(LEFT*0.5),
            ).set_color(color).set_stroke_width(6)
            Campo.move_to(ORIGIN)
            self.campo.add(Campo)

        
        elif sentido == "-j":
            Campo = VGroup(
                Arrow(UP * tam*10, DOWN * tam*20, buff=0).shift(RIGHT*0.5),
                Arrow(UP * tam*10, DOWN * tam*20, buff=0),
                Arrow(UP * tam*10, DOWN * tam*20, buff=0).shift(LEFT*0.5),
            ).set_color(color).set_stroke_width(6)
            Campo.move_to(ORIGIN)
            self.campo.add(Campo)
        
        elif sentido == "+k":
            for x in range(x_range[0], x_range[1] + 1):
                for y in range(y_range[0], y_range[1]+1):
                    campo= VGroup(
                        Circle(radius=tam*0.1, color=color, fill_opacity=1).shift(RIGHT*x*spacing_x + UP*y*spacing_y),
                        Circle(radius=tam, color=color, fill_opacity=0).shift(RIGHT*x*spacing_x + UP*y*spacing_y)
                    )
                    self.campo.add(campo)
            
        elif sentido == "-k":
            for x in range(x_range[0], x_range[1] + 1):
                for y in range(y_range[0], y_range[1] + 1):
                    cruz = VGroup(
                        Line(tam * UL, tam * DR),
                        Line(tam * DL, tam * UR),
                    ).set_color(color)

                    cruz.move_to(np.array([x * spacing_x, y * spacing_y, 0]))
                    self.campo.add(cruz)    
            
        else:
            raise ValueError("Sentido no válido. Debe ser '+i', '-i', '+j', '-j', '+k' o '-k'.")
        
        
        self.add(self.campo)
        
class TestCampoB(Scene):
    def construct(self):
        campo1 = CampoB(sentido="+i", color=GREEN)
        campo2 = CampoB(sentido="-i", color=RED).shift(DOWN*3)
        campo3 = CampoB(sentido="+j", color=BLUE).shift(RIGHT*3)
        campo4 = CampoB(sentido="-j", color=YELLOW).shift(LEFT*3)
        campo5 = CampoB(sentido="+k", color=ORANGE)
        campo6 = CampoB(sentido="-k", color=PURPLE)
        
        self.add(campo5)
        
