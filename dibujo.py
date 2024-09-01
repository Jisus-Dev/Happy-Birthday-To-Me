import turtle as t
import random as r
import math as m

def drawX(a, i):
    """
    Calcula la coordenada X para una posición en el círculo usando un ángulo dado.
    
    Parámetros:
    a (float): Radio del círculo.
    i (float): Ángulo en grados.
    
    Devuelve:
    float: Coordenada X calculada.
    """
    angle = m.radians(i)
    return a * m.cos(angle)

def drawY(b, i):
    """
    Calcula la coordenada Y para una posición en el círculo usando un ángulo dado.
    
    Parámetros:
    b (float): Radio del círculo.
    i (float): Ángulo en grados.
    
    Devuelve:
    float: Coordenada Y calculada.
    """
    angle = m.radians(i)
    return b * m.sin(angle)

# Definir una lista de colores para el confeti
color = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"]

# Configurar la ventana de Turtle
wn = t.Screen()
wn.title("Happy Birthday")
t.bgcolor("#d3dae8")  # Color de fondo de la ventana
t.setup(1000, 800)    # Tamaño de la ventana
t.speed(0)           # Establecer la velocidad de dibujo al máximo

# Desplazar el pastel hacia abajo en la ventana
y_offset = -100  

# Ocultar la tortuga
t.hideturtle()

# Dibujar confeti en el fondo
for _ in range(100):
    t.penup()
    x = r.randint(-t.window_width()//2, t.window_width()//2)
    y = r.randint(-t.window_height()//2, t.window_height()//2)
    t.goto(x, y)
    t.pendown()
    t.dot(r.randint(3, 8), color[r.randint(0, 7)])

# Dibujar el mensaje de cumpleaños
t.color("fuchsia")
t.pu()
t.goto(0, 0)
t.seth(90)
t.fd(210)
t.pd()
t.write("¡FELIZ CUMPLEAÑOS!", align="center", font=("Curlz MT", 50))

# Dibujar la capa inferior del pastel (blanco)
t.showturtle()
t.penup()
t.goto(150, y_offset)
t.pendown()
t.pencolor("white")
t.begin_fill()
for i in range(360):
    x = drawX(150, i)
    y = drawY(60, i) + y_offset
    t.goto(x, y)
t.fillcolor("#fef5f7")
t.end_fill()

# Dibujar la segunda capa del pastel (rosa)
t.penup()
t.goto(150, y_offset)
t.pendown()
t.begin_fill()
for i in range(180):
    x = drawX(150, -i)
    y = drawY(70, -i) + y_offset
    t.goto(x, y)
for i in range(180, 360):
    x = drawX(150, i)
    y = drawY(60, i) + y_offset
    t.goto(x, y)
t.fillcolor("#f2d7dd")
t.end_fill()

# Dibujar la capa media del pastel (azul)
t.penup()
t.goto(120, y_offset)
t.pendown()
t.begin_fill()
for i in range(360):
    x = drawX(120, i)
    y = drawY(48, i) + y_offset
    t.goto(x, y)
t.fillcolor("#cbd9f9")
t.end_fill()

# Dibujar el borde de la capa media del pastel (amarillo)
t.penup()
t.goto(120, y_offset)
t.pendown()
t.begin_fill()
t.pencolor("#fee48c")
for i in range(540):
    x = drawX(120, i)
    y = drawY(48, i) + 70 + y_offset
    t.goto(x, y)
t.goto(-120, y_offset)  # Ir a la base
t.fillcolor("#cbd9f9")
t.end_fill()

# Dibujar la capa superior del pastel (rosa claro)
t.penup()
t.goto(120, 70 + y_offset)
t.pendown()
t.pencolor("#fff0f3")
t.begin_fill()
for i in range(360):
    x = drawX(120, i)
    y = drawY(48, i) + 70 + y_offset
    t.goto(x, y)
t.fillcolor("#fff0f3")
t.end_fill()

# Dibujar la parte superior más pequeña del pastel (rosa claro)
t.penup()
t.goto(110, 70 + y_offset)
t.pendown()
t.pencolor("#fff9fb")
t.begin_fill()
for i in range(360):
    x = drawX(110, i)
    y = drawY(44, i) + 70 + y_offset
    t.goto(x, y)
t.fillcolor("#fff9fb")
t.end_fill()

# Dibujar el borde superior del pastel (rosa fuerte)
t.penup()
t.goto(120, y_offset)
t.pendown()
t.begin_fill()
t.pencolor("#ffa79d")
for i in range(180):
    x = drawX(120, -i)
    y = drawY(48, -i) + 10 + y_offset
    t.goto(x, y)
t.goto(-120, y_offset)
for i in range(180, 360):
    x = drawX(120, i)
    y = drawY(48, i) + y_offset
    t.goto(x, y)
t.fillcolor("#ffa79d")
t.end_fill()

# Dibujar el efecto de glaseado del pastel (rosa claro)
t.penup()
t.goto(120, 70 + y_offset)
t.pendown()
t.begin_fill()
t.pensize(4)
t.pencolor("#fff0f3")
for i in range(1800):
    x = drawX(120, 0.1 * i)
    y = drawY(-18, i) + 10 + y_offset
    t.goto(x, y)
t.goto(-120, 70 + y_offset)
t.pensize(1)
for i in range(180, 360):
    x = drawX(120, i)
    y = drawY(48, i) + 70 + y_offset
    t.goto(x, y)
t.fillcolor("#fff0f3")
t.end_fill()

# Dibujar la segunda base del pastel (cafe)
t.penup()
t.goto(80, 70 + y_offset)
t.pendown()
t.begin_fill()
t.pencolor("#6f3732")
t.goto(80, 120 + y_offset)
for i in range(180):
    x = drawX(80, i)
    y = drawY(32, i) + 120 + y_offset
    t.goto(x, y)
t.goto(-80, 70 + y_offset)
for i in range(180, 360):
    x = drawX(80, i)
    y = drawY(32, i) + 70 + y_offset
    t.goto(x, y)
t.fillcolor("#6f3732")
t.end_fill()

# Dibujar la parte superior de la base (rosa claro)
t.penup()
t.goto(80, 120 + y_offset)
t.pendown()
t.pencolor("#ffaaa0")
t.begin_fill()
for i in range(360):
    x = drawX(80, i)
    y = drawY(32, i) + 120 + y_offset
    t.goto(x, y)
t.fillcolor("#ffaaa0")
t.end_fill()

# Dibujar la parte superior de la base más pequeña (rosa claro)
t.penup()
t.goto(70, 120 + y_offset)
t.pendown()
t.pencolor("#ffc3be")
t.begin_fill()
for i in range(360):
    x = drawX(70, i)
    y = drawY(28, i) + 120 + y_offset
    t.goto(x, y)
t.fillcolor("#ffc3be")
t.end_fill()

# Dibujar el glaseado de la base (rosa claro)
t.penup()
t.goto(80, 120 + y_offset)
t.pendown()
t.begin_fill()
t.pensize(3)
t.pencolor("#ffaaa0")
for i in range(1800):
    x = drawX(80, 0.1 * i)
    y = drawY(-12, i) + 80 + y_offset
    t.goto(x, y)
t.goto(-80, 120 + y_offset)
t.pensize(1)
for i in range(180, 360):
    x = drawX(80, i)
    y = drawY(32, i) + 120 + y_offset
    t.goto(x, y)
t.fillcolor("#ffaaa0")
t.end_fill()

# Dibujar la vela izquierda
t.penup()
t.goto(-56, 120 + y_offset)
t.pendown()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 60
    y = drawY(1, i) + 120 + y_offset
    t.goto(x, y)
t.goto(-56, 170 + y_offset)
for i in range(540):
    x = drawX(4, i) - 60
    y = drawY(1, i) + 170 + y_offset
    t.goto(x, y)
t.goto(-64, 120 + y_offset)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(-56, 120 + 10 * i + y_offset)
    t.penup()
    t.goto(-64, 120 + 10 * i + y_offset)
    t.pendown()
t.penup()
t.goto(-60, 170 + y_offset)
t.pendown()
t.goto(-60, 180 + y_offset)
t.pensize(1)

# Dibujar la llama de la vela izquierda
t.penup()
t.goto(-56, 190 + y_offset)
t.pendown()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 60
    y = drawY(10, i) + 190 + y_offset
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()

# Dibujar la vela central
t.penup()
t.goto(4, 120 + y_offset)
t.pendown()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i)
    y = drawY(1, i) + 120 + y_offset
    t.goto(x, y)
t.goto(4, 170 + y_offset)
for i in range(540):
    x = drawX(4, i)
    y = drawY(1, i) + 170 + y_offset
    t.goto(x, y)
t.goto(-4, 120 + y_offset)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(4, 120 + 10 * i + y_offset)
    t.penup()
    t.goto(-4, 120 + 10 * i + y_offset)
    t.pendown()
t.penup()
t.goto(0, 170 + y_offset)
t.pendown()
t.goto(0, 180 + y_offset)
t.pensize(1)

# Dibujar la llama de la vela central
t.penup()
t.goto(4, 190 + y_offset)
t.pendown()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i)
    y = drawY(10, i) + 190 + y_offset
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()

# Dibujar la vela derecha
t.penup()
t.goto(64, 120 + y_offset)
t.pendown()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) + 60
    y = drawY(1, i) + 120 + y_offset
    t.goto(x, y)
t.goto(64, 170 + y_offset)
for i in range(540):
    x = drawX(4, i) + 60
    y = drawY(1, i) + 170 + y_offset
    t.goto(x, y)
t.goto(56, 120 + y_offset)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(64, 120 + 10 * i + y_offset)
    t.penup()
    t.goto(56, 120 + 10 * i + y_offset)
    t.pendown()
t.penup()
t.goto(60, 170 + y_offset)
t.pendown()
t.goto(60, 180 + y_offset)
t.pensize(1)

# Dibujar la llama de la vela derecha
t.penup()
t.goto(64, 190 + y_offset)
t.pendown()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) + 60
    y = drawY(10, i) + 190 + y_offset
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()

# Dibujar el mensaje adicional en la parte inferior de la pantalla
t.color("fuchsia")
t.pu()
t.goto(0, -330)
t.seth(90)
t.pd()
t.write("JISUS DEV", align="center", font=("Curlz MT", 50))

# Finalizar el dibujo
t.hideturtle()
t.done()