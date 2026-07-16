from manim import *

class Resistencia(VGroup):
    def __init__(self, ancho=2.5, altura=0.3, n_dientes=8, **kwargs):
        super().__init__(**kwargs)

        puntos = []

        for i in range(n_dientes + 1):
            x = -ancho/2 + i * ancho / n_dientes

            if i == 0 or i == n_dientes:
                y = 0
            else:
                y = altura if i % 2 else -altura

            puntos.append([x, y, 0])

        zigzag = VMobject()
        zigzag.set_points_as_corners(puntos)

        etiqueta = MathTex("R")
        etiqueta.next_to(zigzag, UP)

        self.add(zigzag, etiqueta)
        
class Bateria(VGroup):
    def __init__(self,
                 separacion=0.9,
                 altura=1,
                 **kwargs):

        super().__init__(**kwargs)

        corta = Line(
            [0, -altura/2, 0],
            [0, altura/2, 0]
        )

        larga = Line(
            [separacion, -altura, 0],
            [separacion, altura, 0]
        )

        etiqueta = MathTex("V")
        etiqueta.next_to(
            VGroup(corta, larga),
            UP
        )

        self.add(corta, larga, etiqueta)
class Condensador(VGroup):
    def __init__(self,
                 separacion=0.9,
                 altura=1,
                 **kwargs):

        super().__init__(**kwargs)

        placa1 = Line(
            [0, -altura/2, 0],
            [0, altura/2, 0]
        )

        placa2 = Line(
            [separacion, -altura/2, 0],
            [separacion, altura/2, 0]
        )

        etiqueta = MathTex("C")
        etiqueta.next_to(
            VGroup(placa1, placa2),
            UP
        )

        self.add(placa1, placa2, etiqueta)
class Bobina(VGroup):
    def __init__(
        self,
        n_espiras=6,
        ancho=0.7,
        alto=0.28,
        separacion=0.18,
        **kwargs
    ):
        super().__init__(**kwargs)

        bobina = VGroup()

        for i in range(n_espiras):
            e = Ellipse(
                width=2*ancho,
                height=2*alto
            )
            e.shift(DOWN * i * separacion)
            e.color = WHITE
            bobina.add(e)

        # Que se solapen ligeramente
        bobina.arrange(DOWN, buff=-0.22)

        terminal_sup = Line(
            bobina.get_top()+UP*0.5,
            bobina.get_top()
        )

        terminal_inf = Line(
            bobina.get_bottom(),
            bobina.get_bottom()+DOWN*0.5
        )

        etiqueta = MathTex("L").next_to(bobina, UP)

        BOBINAFINAL= VGroup(bobina, terminal_sup, terminal_inf)
        BOBINAFINAL.rotate(-PI/2)
        
        self.add (BOBINAFINAL)
        self.add(etiqueta.next_to(BOBINAFINAL, UP))
        
class VarillaMovil(VGroup):
    def __init__(
        self,
        largo=2,
        ancho=0.5,
        **kwargs
    ):
        super().__init__(**kwargs)

        varilla = Rectangle(
        width=ancho,
        height=largo,
        fill_color=BLACK,
        fill_opacity=1,
        stroke_color=WHITE,
        stroke_width=2
)

        bordes = VGroup(
            Line(varilla.get_corner(UL), varilla.get_corner(UR)),
            Line(varilla.get_corner(DL), varilla.get_corner(DR)),
            Line(varilla.get_corner(UL), varilla.get_corner(DL)),
            Line(varilla.get_corner(UR), varilla.get_corner(DR))
        )
        bordes.set_stroke("#FFFFFF", 2)
        bordes.set_fill(opacity=1)
        
        Varilla=VGroup(varilla, bordes)
        self.add(Varilla)
        
class TestComponentes(Scene):
    def construct(self):

        bateria = Bateria()
        resistencia = Resistencia()
        condensador = Condensador()
        bobina = Bobina()

        bateria.move_to(UL * 2)
        resistencia.move_to(UR * 2)
        condensador.move_to(DL * 2)
        bobina.move_to(DR * 2)

        self.play(
            Create(bateria),
            Create(resistencia),
            Create(condensador),
            Create(bobina)
        )
        self.play(
            Uncreate(bateria),
            Uncreate(resistencia),
            Uncreate(condensador),
            Uncreate(bobina)
            
        )
        self.wait()
        self.play(
            Create (VarillaMovil())
        )
        self.wait(1)