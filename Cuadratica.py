import numpy as np
from manim import *
MAIN_COLOR = "#ffffff"

class Inicio (Scene):
    def construct(self):
            title = Text ("Where does this come from?", color=MAIN_COLOR)
            title.to_edge(UP)
            '''
            title_glow = title.copy()
            title_glow.set_stroke(width=25, opacity=0.2)
            title_glow.set_color(MAIN_COLOR)
            
            self.add(title_glow)'''
            
            self.add(title)
            self.play(Write(title))
            eq = MathTex(r"x= \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", color="#d8d27a")
            eq.scale (1.5)
            
            box=SurroundingRectangle(eq,buff = 0.25, color=RED)
            glow= box.copy().set_stroke(width=10, opacity=0.15)

            self.play(Write(eq))
            self.add(glow)
            self.play(Create(box))
            self.wait(1)
            self.play(FadeOut(eq), FadeOut(title),FadeOut(box),FadeOut(glow))
            
class Demostracion (Scene):
    def construct (self):
        #-------------------------------------------------#
        # TEXTO INICIAL
        #-------------------------------------------------#
        text1= Text ("Let's start writting the general form of a 2º grade Polynomial:", color=MAIN_COLOR)
        text1.scale (0.5)
        text1.shift (UP*1.5)
        self.play(Write (text1)) 
        #-------------------------------------------------#
        # P(X) GENÉRICO
        #-------------------------------------------------#
        Poly= MathTex (r"P(x)= ax^2 + bx + c", color=MAIN_COLOR) 
        Poly.scale (0.7)
        self.play(Write (Poly))
        self.wait (2)
        
        self.play(Unwrite(text1))
        #-------------------------------------------------#
        # IGUALAMOS A 0
        #-------------------------------------------------#
        text1 = Text ("To find the roots of any polynomial, we need to solve the equation P(x)=0", color=MAIN_COLOR)          
        text1.scale (0.5)
        text1.shift (UP*1.5)
        
        self.play(Write (text1))
        self.play(Transform (Poly, MathTex (r"ax^2 + bx + c = 0", color=MAIN_COLOR)))
        self.wait (2)
        
        self.play(Unwrite(text1))
        
        self.play(Transform (Poly, MathTex (r"ax^2 +bx = -c", color=MAIN_COLOR)))
        self.wait (2)
        
        #-------------------------------------------------#
        # DIVIDIMOS ENTRE A
        #-------------------------------------------------#
        text1= Text ("Let's divide the both sides by a to isolate the x^2 term:", color=MAIN_COLOR)
        text1.scale (0.5)
        text1.shift (UP*1.5)
        self.play(Write (text1))
        
        self.play(Transform (Poly, MathTex (r"x^2 + \frac{b}{a}x = -\frac{c}{a}", color=MAIN_COLOR)))
        self.wait (2)
        
        self.play(Unwrite(text1))
        
        #-------------------------------------------------#
        # IDENTIDADES Y CAJAS
        #-------------------------------------------------#
        text1= Text ("Remembering this identity:", color=MAIN_COLOR)
        text1.scale (0.5)
        text1.to_corner(UL)
        
        text2 = MathTex (r"(a+b)^2 = a^2 + 2ab + b^2", color="#64ebf5ff")
        text2.scale (0.7)
        text2.to_corner(UL)
        text2.shift(DOWN*1, RIGHT*1)
        
        box = SurroundingRectangle(text2,buff=0.25, color=RED)
        glow= box.copy().set_stroke(width=10, opacity=0.15)
        
        
        self.play(FadeIn (text1))
        self.play(FadeIn (text2))
        self.add(glow)
        self.play(Create(box))
        self.wait (2)
        
        self.play(FadeOut(text1), FadeOut(text2),FadeOut(box),FadeOut(glow))
        
        text1= Text ("We can complete the square noticing that in our case: ", color=MAIN_COLOR)
        text1.scale (0.5)
        text1.shift (UP*1.5)
        text1.to_corner(UL)
        
        text2 = MathTex (r"x^2 + \frac{b}{a}x =(x+ \frac{b}{2a})^2 - (\frac{b}{2a})^2", color="#64ebf5ff")
        text2.scale(0.7)
        text2.to_corner(UL)
        text2.shift(DOWN*1, RIGHT*1)
        
        box = SurroundingRectangle(text2,buff=0.25, color=RED)
        glow= box.copy().set_stroke(width=10, opacity=0.15)
        
        
        self.play(FadeIn (text1))
        self.play(FadeIn (text2))
        self.add(glow)
        self.play(Create(box))
        self.wait (4)
        
        self.play(FadeOut(box),FadeOut(glow))
        self.play(FadeOut(text1), FadeOut(text2))
        #-------------------------------------------------#
        # VUELTA A LA ECUACIÓN TRAS CUADRADO
        #-------------------------------------------------#
        text1= Text ("So we can rewrite the equation as:", color=MAIN_COLOR)
        text1.scale (0.5)
        text1.shift (UP*1.5)
        self.play(Write (text1))
        
        self.play(Transform (Poly, MathTex (r"(x+ \frac{b}{2a})^2 - (\frac{b}{2a})^2 = -\frac{c}{a}", color=MAIN_COLOR)))
        self.wait (2)
        
        self.play(Unwrite(text1))
        #-------------------------------------------------#
        #Despejamos x
        #-------------------------------------------------#
        text1= Text ("Isolating the square term:", color=MAIN_COLOR)
        text1.scale (0.5)
        text1.shift (UP*1.5)
        self.play(Write (text1))
        
        self.play(Transform (Poly, MathTex (r"(x+ \frac{b}{2a})^2 = (\frac{b}{2a})^2 -\frac{c}{a}", color=MAIN_COLOR)))
        self.wait (2)
        
        self.play(Transform (Poly,MathTex (r"(x + \frac{b}{2a})^2 = \frac{b^2 - 4ac}{4a^2}", color=MAIN_COLOR)))
        self.wait (2)
        
        self.play(Unwrite(text1))
        #-------------------------------------------------#
        # RAICES A AMBOS LADOS
        #-------------------------------------------------#
        text1= Text ("Now we just need to take the square root of both sides:", color=MAIN_COLOR)
        text1.scale (0.5)
        text1.shift (UP*1.5)
        
        text2= Text ("Since by applying the square root we loose the sign information,\n" 
                     "          we need to add a ± on the right side:", color=MAIN_COLOR)
        text2.scale (0.5)
        text2.shift (UP*1.5)
        self.play(Write (text1))
        
        self.play(Unwrite(text1))
        
        self.play(Write (text2))
        self.play(Transform(Poly, MathTex (r"\sqrt{(x +\frac{b}{2a})^2} = \pm \sqrt{\frac{b^2 -4ac}{4a^2}} ")))
        
        self.wait(2)
        self.play(Transform(Poly, MathTex(r"x + \frac {b}{2a} = \pm \frac{\sqrt{b^2 -4ac}}{2a}")))
        
        self.play(Unwrite(text2))
        #-------------------------------------------------#
        # FINAL DEMOSTRACIÓN
        #-------------------------------------------------#
        text1 = Text ("Finally, we leave the x alone on the equation:")
        text1.scale(0.5)
        text1.shift(UP*1.5)
        self.play(Write(text1))
        
        box = SurroundingRectangle(Poly,buff=0.25, color=RED)
        glow= box.copy().set_stroke(width=10, opacity=0.15)
        
        self.play(Transform(Poly,MathTex(r"x = -\frac{b}{2a} \pm \frac{ \sqrt{b^2 -4ac}}{2a} ")))
        
        self.wait(2)
        
        self.play(Transform(Poly,MathTex (r"x = \frac{-b \pm \sqrt{b^2 -4ac}}{2a}")))
        self.add(glow)
        self.play(Create(box))
        self.wait(2)
        
        
        self.play(Unwrite(text1))
        self.play(FadeOut(Poly))
        self.play(FadeOut(glow),FadeOut(box))
        self.wait(1)
                    
# manim -pql Cuadratica.py Demostracion