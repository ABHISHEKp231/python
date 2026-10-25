import turtle

# Screen setup
screen = turtle.Screen()
screen.title("Swami Ayyappa - Python Drawing")
screen.bgcolor("black")
screen.setup(width=800, height=800)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Helper functions
def circle(x, y, r, color):
    t.penup()
    t.goto(x, y - r)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

def polygon(points, color):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for p in points[1:]:
        t.goto(p)
    t.goto(points[0])
    t.end_fill()


# -------------------------
# Temple background
# -------------------------

rectangle(-350, 300, 700, 500, "#3b1708")

# Temple pillars
rectangle(-300, 250, 70, 450, "#d28b25")
rectangle(230, 250, 70, 450, "#d28b25")

# Temple roof
polygon([
    (-350, 300),
    (350, 300),
    (270, 400),
    (-270, 400)
], "#8b1a1a")

polygon([
    (-270, 400),
    (270, 400),
    (200, 470),
    (-200, 470)
], "#d49a28")


# -------------------------
# Aura
# -------------------------

circle(0, 40, 240, "#d88b16")
circle(0, 40, 215, "#ffd45a")


# -------------------------
# Body
# -------------------------

# Torso
polygon([
    (-110, -20),
    (110, -20),
    (145, -230),
    (-145, -230)
], "#8b4513")

# Clothing
polygon([
    (-145, -180),
    (145, -180),
    (120, -300),
    (-120, -300)
], "#f0a51a")


# -------------------------
# Head
# -------------------------

circle(0, 100, 85, "#a96b32")


# Hair
polygon([
    (-70, 135),
    (-45, 195),
    (0, 215),
    (45, 195),
    (70, 135),
    (50, 165),
    (0, 185),
    (-50, 165)
], "#24130b")


# -------------------------
# Crown
# -------------------------

polygon([
    (-65, 165),
    (-45, 235),
    (0, 275),
    (45, 235),
    (65, 165),
    (35, 190),
    (0, 215),
    (-35, 190)
], "#d89b19")

# Crown jewel
circle(0, 225, 10, "#e31b23")


# -------------------------
# Eyes
# -------------------------

circle(-30, 115, 7, "black")
circle(30, 115, 7, "black")

# Tilak
polygon([
    (-8, 150),
    (8, 150),
    (0, 115)
], "#e21b23")


# -------------------------
# Nose
# -------------------------

t.penup()
t.goto(0, 110)
t.pendown()
t.setheading(-90)
t.forward(25)


# -------------------------
# Smile
# -------------------------

t.penup()
t.goto(-25, 82)
t.pendown()
t.setheading(-40)

for _ in range(20):
    t.forward(2)
    t.left(4)


# -------------------------
# Necklace
# -------------------------

t.penup()
t.goto(-60, 45)
t.pendown()
t.color("#ffd700")
t.setheading(-20)

for _ in range(7):
    t.circle(12, 60)
    t.circle(-12, 60)

# Necklace beads
for x in range(-50, 51, 20):
    circle(x, 20, 6, "#ffd700")


# -------------------------
# Arms
# -------------------------

# Left arm
t.penup()
t.goto(-100, -30)
t.pendown()
t.color("#a96b32")
t.width(35)
t.setheading(-130)
t.forward(160)

# Right arm
t.penup()
t.goto(100, -30)
t.pendown()
t.setheading(-50)
t.forward(160)

t.width(1)


# -------------------------
# Hands
# -------------------------

circle(-200, -135, 25, "#a96b32")
circle(200, -135, 25, "#a96b32")


# -------------------------
# Feet / seated position
# -------------------------

circle(-85, -285, 35, "#a96b32")
circle(85, -285, 35, "#a96b32")


# -------------------------
# Decorative lamps
# -------------------------

for x in [-300, 300]:
    circle(x, -100, 18, "#ffcc33")
    rectangle(x - 8, -120, 16, 70, "#c58a20")


# -------------------------
# Text
# -------------------------

t.penup()
t.goto(0, -370)
t.color("#ffd700")
t.write(
    "Swamiye Saranam Ayyappa",
    align="center",
    font=("Arial", 24, "bold")
)

screen.mainloop()

