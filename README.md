# PRODUCTO ACADEMICO 2 
En este segundo producto académico aplicamos los principios de la programación orientada a objetos usando la librería Turtle, creando clases que heredan y amplían la funcionalidad de la clase base para generar gráficos personalizados. A través de este proyecto, comprendimos conceptos clave como herencia, polimorfismo y encapsulamiento, desarrollando programas visuales que integran figuras geométricas, patrones repetitivos y secuencias matemáticas de forma dinámica e interactiva.

Tecnologías usadas 
-Python (POO)
-vim
-Diagramas UML en mermaid (Clases y Casos de Uso)
```mermaid
classDiagram
    class Turtle {
        +color(...)
        +pensize(...)
        +speed(...)
        +forward(distance: float)
        +right(angle: float)
        +penup()
        +pendown()
        +hideturtle()
        +showturtle()
        +goto(x: float, y: float)
        +circle(radius: float)
    }

    class FiguraTortuga {
        +__init__()
        +configurar(color: str, grosor: int, velocidad: int)
        +dibujar(lados: int = 3, longitud: int = 50)
    }

    class CollatzTortuga {
        +__init__()
        +configurar(color: str = "green", grosor: int = 2, velocidad: int = 0)
        +dibujar_collatz(n: int)
    }

    class PatronTortuga {
        +__init__()
        +configurar(color: str, grosor: int, velocidad: int)
        +dibujar_espiral(n_lados: int, longitud: int, incremento: int)
        +dibujar_mandala(n: int, radios: int, longitud_inicial: int)
    }

    FiguraTortuga --|> Turtle
    CollatzTortuga --|> Turtle
    PatronTortuga --|> Turtle