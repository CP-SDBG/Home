#Komet dræber spil - skyd kometerne ned inden de rammer dig!
import random
import math

WIDTH = 600
HEIGHT = 800

# Spiller
ship = Actor('ship')
ship.pos = (WIDTH // 2, HEIGHT // 2)
ship.angle = 0
ship.vx = 0
ship.vy = 0

# Stjerner
stars = []
for _ in range(200):
    stars.append({
        "x": random.randint(-WIDTH, WIDTH),
        "y": random.randint(-HEIGHT, HEIGHT),
        "size": random.choice([1, 2])

    })

def draw():
    # Rens vinduet
    screen.clear()

    # Tegn stjerner
    for star in stars:
        screen.draw.filled_circle((star["x"], star["y"]), star["size"], "white")

    # Tegn Spiller
    ship.draw()

def update():
    # Roter spiller
    if keyboard.left:
        ship.angle += 4
    if keyboard.right:
        ship.angle -= 4

    # Bevæg spiller fremad
    if keyboard.up:
        rad = math.radians(ship.angle)
        ship.vx += -math.sin(rad) * 0.2
        ship.vy -= math.cos(rad) * 0.2

    # Friktion og position
    ship.x += ship.vx
    ship.y += ship.vy
    ship.vx *= 0.98
    ship.vy *= 0.98

    # Skærmgrænser (wrap around)
    if ship.x < 0:
        ship.x = WIDTH
    if ship.x > WIDTH:
        ship.x = 0
    if ship.y < 0:
        ship.y = HEIGHT
    if ship.y > HEIGHT:
        ship.y = 0

