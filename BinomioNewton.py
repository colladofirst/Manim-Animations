from manim import *
import numpy as np

class Introducción(Scene):
    def construct(self):
        watermark = Text(
            "Math.py",    
            font_size=28,
            color=WHITE
            )
        watermark.set_opacity(0.5)
        watermark.to_corner(DR, buff=0.3)
        self.play(
                FadeIn(watermark, shift=UP * 0.2),
                run_time=1
            )
        self.play(
                watermark.animate.set_opacity(0.3),
                run_time=1
            )
        texto = Text("How do we know this is true?", font_size=40, color=WHITE)
        fórmula= MathTex(r"(a+b)^n = \sum_{i=0}^n \binom{n}{i} a^{n-i} b^i \qquad \forall a,b \in \mathbb{R}", font_size=30, color=WHITE)
        texto.shift(UP*2)
        Caja = SurroundingRectangle(
            fórmula,
            color=RED,
            buff=0.2 #espacio entre eq y borde
        )
        Glow = Caja.copy().set_stroke(width=12, opacity=0.3)
        
        self.play(Write(texto))
        self.play(
            Write(fórmula),
            Create(Caja),
            Write(Glow),
            run_time=5
        )
        self.wait(2)
        self.play(
            Unwrite(texto),
            Unwrite(fórmula),
            Uncreate(Caja),
            Unwrite(Glow)
        )
        
class Explanation (Scene):
    def construct(self):
        watermark = Text(
            "Math.py",    
            font_size=28,
            color=WHITE
            )
        watermark.set_opacity(0.3)
        watermark.to_corner(DR, buff=0.3)
        self.add(watermark)
            
        texto= Text("First of all we must do some previous aclarations:", font_size=30, color=WHITE)
        texto.shift(UP*2)
        
        texto1= Text("1. This theorem is valid for any scalars", font_size=30, color=WHITE).scale(0.8).shift(LEFT*1)
        texto2= MathTex(r"a,b \in \mathbb{C}", font_size=30, color=WHITE).shift(RIGHT*2.5).scale(1.2)
        conj = VGroup(texto1, texto2)
        conj.shift(UP*0.5)
        
        texto3= Text("2. This theorem is also valid for any exponent", font_size=30, color=WHITE).scale(0.8).shift(LEFT*2)
        texto4= MathTex(r"n \in \mathbb{N},\: n  \in \mathbb{R}\:", font_size=30, color=WHITE).scale(1.2).shift(RIGHT*2.5)  
        texto5 =Text("and").scale(0.5).shift(RIGHT*4 + UP*0.05)
        texto6= MathTex(r"n \in \mathbb{C}", font_size=30, color=WHITE).shift(DOWN*0.5)
        conj2= VGroup(texto3, texto4, texto5, texto6)
        
        self.play(
            Write(texto),
            Write(conj),
            Write(conj2)
        )
        self.wait(8)
        
        self.play(
            Unwrite(texto),
            Unwrite(conj),
            Unwrite(conj2)
        )
        texto7= Text("In this video we will only prove when n is a natural number, but the \n proof for n when it's a real or complex number will be in another video", font_size=30, color=WHITE)
        texto7.scale(0.7)
        
        self.play(Write(texto7))
        self.wait(5)
        self.play(Unwrite(texto7))
        
class Proof(Scene):
    def construct(self):
        watermark = Text(
            "Math.py",    
            font_size=28,
            color=WHITE
            )
        watermark.set_opacity(0.3)
        watermark.to_corner(DR, buff=0.3)
        self.add(watermark)
        
        texto= Text ("We will prove the theorem by induction on n", font_size=30, color=WHITE)
        texto.shift(UP*2)
        
        self.play(Write(texto))
        self.wait(3)
        self.play(Transform (texto, Text("For the base case, we will prove that the theorem is valid for n=0", font_size=30, color=WHITE)))
        self.wait(3)
        self.play(Unwrite(texto))
        
        texto1= Text("In the left side of the equation we have:", font_size=30, color=WHITE).shift(UP*1.5)
        texto2= MathTex(r"(a+b)^0 = 1", font_size=30, color=WHITE).scale(1.2)
        
        self.play( 
                  Write(texto1),
                  Write(texto2)
        )
        self.wait(3)
        self.play(
            Unwrite(texto1),
            Unwrite(texto2)
        )
        
        texto3= Text("On the other hand, in the right side we have:", font_size=30, color=WHITE).shift(UP*1.5)
        texto4= MathTex(r" \sum_{i=0}^0 \binom{0}{i} a^{0-i} b^i = \binom{0}{0}a^{0} b^{0}=1", font_size=30, color=WHITE).scale(1.2)
        self.play(
            Write(texto3),
            Write(texto4)
        )
        self.wait(4)
        self.play(
            Unwrite(texto3),
            Unwrite(texto4)
        )
        Texto5= Text("We can see that both sides are equal, so the base case is true", font_size=30, color=WHITE)
        self.play(Write(Texto5))
        self.wait(3)
        self.play(Transform(Texto5, Text("Now lets assume that the theorem is valid for n, \n \t \t \twill be valid for n+1?", font_size=30, color=WHITE)))
        self.wait(4)
        self.play(Unwrite(Texto5))
        
        texto6=Text("For n+1 in the left side of the equation we have:", font_size=30, color=WHITE).shift(UP*1.5)
        texto7= MathTex(r"(a+b)^{n+1}", font_size=30, color=WHITE).scale(1.2)
        self.play(
            Write(texto6),
            Write(texto7)
        )
        self.wait(3)
        self.play(
            Transform(texto6, Text("This also equals to:", font_size=30, color=WHITE).shift(UP*1.5)),
            Transform(texto7,MathTex(r"(a+b)^{n}(a+b)", font_size=30, color=WHITE).scale(1.2))
        )
        self.wait(3)
        self.play(
            Transform(texto6, Text("Since we assumed that the theorem is valid for n:", font_size=30, color=WHITE).shift(UP*1.5)),
            Transform(texto7, MathTex(r"(a+b)^{n+1}=(a+b)\cdot \sum_{i=0}^n \binom{n}{i} a^{n-i} b^i", font_size=30, color=WHITE).scale(1.2)))
        
        self.wait(5)
        
        self.play(
            Transform(texto6, Text("Distributing the (a+b) and separating the sumatory we have:", font_size=30, color=WHITE).shift(UP*1.5)),
            Transform(texto7, MathTex(r"(a+b)^{n+1}=\sum_{i=0}^n \binom{n}{i} a^{n+1-i}b^i + \sum_{i=0}^n \binom{n}{i} a^{n-i} b^{i+1}", font_size=30, color=WHITE).scale(1.2))
        )
        self.wait(5)
        
        self.play(
            Unwrite(texto6),
            Unwrite(texto7)
        )
        
        texto8= Text("Now we have to realize a smart trick", font_size=30, color=WHITE).shift(UP*1.5)
        self.play(Write(texto8))
        self.wait(3)
        self.play(
            Transform(texto8, Text("If we change the index of the first sumatory with j=i+1, we have:", font_size=30, color=WHITE).shift(UP*1.5))
        )
        texto9= MathTex(r"\sum_{j=1}^{n+1}\binom{n}{j-1} a^{n-j+1} b{j}", font_size=30, color=WHITE).scale(1.2)
        self.play(Write(texto9))
        self.wait(5)
        
        self.play(
            Transform(texto8,Text("Since j is a dummy variable, we can change it for i again. Having then", font_size=30, color=WHITE).shift(UP*1.5)),
            Transform(texto9, MathTex(r"(a+b)^{n+1}=\sum_{i=1}^{n+1}\binom{n}{i-1} a^{n-i+1} b^i + \sum_{i=0}^n \binom{n}{i} a^{n-i+1} b^i", font_size=30, color=WHITE).scale(1.2))
        )
        self.wait(5)
        
        self.play(
            Transform(texto8,Text("Since the scalar terms are the same, we can sum them",font_size=30, color=WHITE).shift(UP)),
            Transform(texto9, MathTex(r"(a+b)^{n+1}=\sum_{i=0}^{n+1} \left( \binom{n}{i-1} + \binom{n}{i} \right) a^{n-i+1} b^i", font_size=30, color=WHITE).scale(1.2).shift(DOWN*0.5))
        )
        
        self.wait(5)
        
        self.play ( Unwrite(texto8))
        
        texto10 = Text(
            "Remembering Pascal's identity:",
        font_size=30,
        color=WHITE
        )

        texto11 = MathTex(
        r"\binom{n}{r}= \binom{n-1}{r} + \binom{n-1}{r-1}",
        font_size=36,
        color=WHITE
        )

        # 🔥 Agrupar y ordenar
        grupo_pascal = VGroup(texto10, texto11).arrange(DOWN, buff=0.4)

        # 🔥 Posicionar TODO junto
        grupo_pascal.to_corner(UL, buff=0.5)
        grupo_pascal.shift(LEFT*0.5).scale(0.8)
     
        #  🔥 Recuadro sobre TODO el bloque (no solo la fórmula)
        box = SurroundingRectangle(grupo_pascal, color=RED, buff=0.3)

        # 🔥 Glow más limpio
        glow = box.copy().set_stroke(width=8, opacity=0.2)

        self.play(
        FadeOut(texto8),
        Write(grupo_pascal),
        Create(box),
        Create(glow)
        )

        self.wait(5)
        
    
        
        self.play(
            Unwrite(grupo_pascal),
            Unwrite(glow),
            Unwrite(box),
            Transform(texto9, MathTex(r"(a+b)^{n+1}=\sum_{i=0}^{n+1} \binom{n+1}{i} a^{n+1-i} b^i", font_size=30, color=WHITE).scale(1.2))
        )
        texto12=Text("Since this is the form of our theorem for n+1, Q.E.D.",font_size=30,color=WHITE).shift(UP*1.5)
        self.play(Write(texto12))
        self.wait(5)
        self.play (
            Unwrite(texto12),
            Unwrite(texto9)
        )
        
        
class Prueba(Scene):
    def construct(self):
    
     texto10 = Text(
        "Remembering Pascal's identity:",
        font_size=30,
        color=WHITE
        )

     texto11 = MathTex(
        r"\binom{n}{r}= \binom{n-1}{r} + \binom{n-1}{r-1}",
        font_size=36,
        color=WHITE
        )

     # 🔥 Agrupar y ordenar
     grupo_pascal = VGroup(texto10, texto11).arrange(DOWN, buff=0.4)

     # 🔥 Posicionar TODO junto
     grupo_pascal.to_corner(UL, buff=0.5)
     grupo_pascal.shift(LEFT*0.8, UP*0.2).scale(0.8)
     
     # 🔥 Recuadro sobre TODO el bloque (no solo la fórmula)
     box = SurroundingRectangle(grupo_pascal, color=RED, buff=0.3)

     # 🔥 Glow más limpio
     glow = box.copy().set_stroke(width=8, opacity=0.2)

     self.play(
        # FadeOut(texto8),
        Write(texto10),
        Write(texto11),
        Create(box),
        Create(glow)
     )

     self.wait(5)
        
    