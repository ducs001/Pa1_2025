import turtle
import random
import time
import math

# ========== CLASES DERIVADAS DE TURTLE ==========

class FiguraTortuga(turtle.Turtle):
    """Subclase que hereda de Turtle para dibujar figuras geométricas básicas."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def configurar(self, color, grosor, velocidad):
        self.color(color)
        self.pensize(grosor)
        self.speed(velocidad)

    def dibujar(self, lados=3, longitud=50):
        """Dibuja una figura regular con el número de lados y longitud especificados."""
        self.pendown()
        angulo = 360 / lados
        for _ in range(lados):
            self.forward(longitud)
            self.right(angulo)
        self.penup()

class CollatzTortuga(turtle.Turtle):
    """Subclase que grafica la secuencia de Collatz para un número dado."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def configurar(self, color="green", grosor=2, velocidad=0):
        self.color(color)
        self.pensize(grosor)
        self.speed(velocidad)

    def dibujar_collatz(self, n):
        """Dibuja la secuencia de Collatz representando el valor en eje Y."""
        self.penup()
        self.goto(-300, n)
        self.pendown()
        x = -300
        escala_y = 5

        while n != 1:
            y = n * escala_y
            self.goto(x, y)
            x += 10
            n = n // 2 if n % 2 == 0 else 3 * n + 1
        self.goto(x, escala_y)

class PatronTortuga(turtle.Turtle):
    """Subclase que dibuja patrones repetitivos como espirales y mandalas."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def configurar(self, color, grosor, velocidad):
        self.color(color)
        self.pensize(grosor)
        self.speed(velocidad)
        self.showturtle()

    def dibujar_espiral(self, n_lados, longitud, incremento):
        """Dibuja una espiral aumentando la longitud en cada paso."""
        self.pendown()
        for _ in range(n_lados):
            self.forward(longitud)
            self.right(360 / n_lados)
            longitud += incremento
        self.penup()

    def dibujar_mandala(self, n, radios, longitud_inicial):
        """Dibuja un patrón circular en forma de mandala."""
        self.pendown()
        for _ in range(n):
            self.circle(radios)
            self.right(360 / n)
            radios += longitud_inicial
        self.penup()

# ========== PROGRAMAS ==========

def programa_1():
    """Dibuja 'n' tortugas con figuras geométricas aleatorias (colores, formas, posiciones)."""
    n = int(pantalla.numinput("Cantidad", "Número de tortugas (5-50):", minval=5, maxval=50))
    for _ in range(n):
        t = FiguraTortuga()
        t.goto(random.randint(-300, 300), random.randint(-250, 250))
        color = random.choice(["red", "blue", "green", "orange", "purple", "black", "cyan"])
        t.configurar(color=color, grosor=random.randint(1, 5), velocidad=random.randint(1, 10))
        t.showturtle()
        t.dibujar(lados=random.choice([3, 4, 5, 6]), longitud=30 + random.randint(0, 20))

def programa_2():
    """Solicita un número y grafica la secuencia de Collatz."""
    num = int(pantalla.numinput("Collatz", "Número entero positivo:", minval=1))
    t = CollatzTortuga()
    t.configurar()
    t.dibujar_collatz(num)

def programa_3():
    """Dibuja un patrón gráfico tipo espiral o mandala según elección del usuario."""
    figura = PatronTortuga()
    figura.goto(0, 0)
    figura.configurar(color="purple", grosor=2, velocidad=10)

    eleccion = pantalla.textinput("Patrón Tortuga", "¿Qué patrón deseas?\nEscribe: espiral o mandala").lower()
    if eleccion == "espiral":
        n_lados = int(pantalla.numinput("Espiral", "¿Cuántos lados? 3-100", minval=3, maxval=100))
        longitud = int(pantalla.numinput("Espiral", "Longitud inicial de la línea? 10-100", minval=10, maxval=100))
        incremento = int(pantalla.numinput("Espiral", "Incremento de longitud? 1-10", minval=1, maxval=10))
        figura.dibujar_espiral(n_lados, longitud, incremento)
    elif eleccion == "mandala":
        n = int(pantalla.numinput("Mandala", "¿Cuántos círculos en el mandala 1-20?", minval=1, maxval=20))
        radios = int(pantalla.numinput("Mandala", "Radio inicial de los círculos 10-100?", minval=10, maxval=100))
        longitud_inicial = int(pantalla.numinput("Mandala", "Incremento de radio 5-50git?", minval=5, maxval=50))
        figura.dibujar_mandala(n, radios, longitud_inicial)
    else:
        turtle.write("Opción no válida")

def programa_4():
    """Dibuja múltiples pentágonos con diferentes tortugas distribuidas en pantalla."""
    cantidad = int(pantalla.numinput("Cantidad", "¿Cuántas tortugas quieres 1-100?", minval=1, maxval=100))
    color = "red"
    grosor = int(pantalla.numinput("Grosor", "Grosor (1-5):", minval=1, maxval=5))
    tamano = int(pantalla.numinput("Tamaño", "Tamaño del pentágono 20 -100:", minval=20, maxval=100))
    
    start = time.time()
    for i in range(cantidad):
        t = FiguraTortuga()
        t.configurar(color, grosor, velocidad=10)
        x = -300 + (i % 10) * 70
        y = 250 - (i // 10) * 70
        t.goto(x, y)
        t.showturtle()
        t.dibujar(5, tamano)
    print(f"Tiempo: {round(time.time() - start, 3)}s")

def programa_5():
    """Detecta teclas para elegir figura y dibuja al hacer clic en pantalla."""
    pantalla = turtle.Screen()
    pantalla.title("Dibujo con Teclado y Clic")
    pantalla.bgcolor("white")

    figura = turtle.Turtle()
    figura.hideturtle()
    figura.penup()
    figura.speed(0)

    tipo_figura = {"modo": "triangulo"}

    def tecla_t(): tipo_figura["modo"] = "triangulo"
    def tecla_c(): tipo_figura["modo"] = "cuadrado"
    def tecla_p(): tipo_figura["modo"] = "pentagono"
    def tecla_h(): tipo_figura["modo"] = "hexagono"
    def tecla_default(): tipo_figura["modo"] = "circulo"

    def al_clic(x, y):
        figura.penup()
        figura.goto(x, y)
        figura.pendown()
        modo = tipo_figura["modo"]
        lados = {"triangulo": 3, "cuadrado": 4, "pentagono": 5, "hexagono": 6}.get(modo, 0)
        if lados:
            angulo = 360 / lados
            for _ in range(lados):
                figura.forward(40)
                figura.right(angulo)
        else:
            figura.circle(7)
        figura.penup()

    pantalla.listen()
    pantalla.onkey(tecla_t, "t")
    pantalla.onkey(tecla_c, "c")
    pantalla.onkey(tecla_p, "p")
    pantalla.onkey(tecla_h, "h")
    for tecla in "abcdefghijklmnopqrstuvwxyz0123456789 ":
        if tecla not in "tcp h":
            pantalla.onkey(tecla_default, tecla)

    pantalla.onclick(al_clic)
    pantalla.mainloop()

# ========== MENÚ PRINCIPAL ==========

pantalla = turtle.Screen()
pantalla.title("Menú de Programas")
pantalla.bgcolor("white")

while True:
    eleccion = pantalla.textinput("Menú Principal",
    "Elige un programa:\n"
    "1 - Tortugas aleatorias\n"
    "2 - Secuencia de Collatz\n"
    "3 - Dibujar Patrón (Espiral o Mandala)\n"
    "4 - Secuencia de Pentágonos\n"
    "5 - Dibujar con teclado y clic\n"
    "6 - Salir")

    if eleccion == "1":
        pantalla.clearscreen()
        pantalla.title("Programa 1")
        programa_1()
    elif eleccion == "2":
        pantalla.clearscreen()
        pantalla.title("Programa 2")
        programa_2()
    elif eleccion == "3":
        pantalla.clearscreen()
        pantalla.title("Programa 3")
        programa_3()
    elif eleccion == "4":
        pantalla.clearscreen()
        pantalla.title("Programa 4")
        programa_4()
    elif eleccion == "5":
        pantalla.clearscreen()
        pantalla.title("Programa 5")
        programa_5()
    elif eleccion == "6":
        break

pantalla.bye()
