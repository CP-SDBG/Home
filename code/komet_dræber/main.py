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

# Skud
bullets = []

# Kometer
meteors= []

# Stjerner
stars = []
for _ in range(200):
    stars.append({
        "x": random.randint(-WIDTH, WIDTH),
        "y": random.randint(-HEIGHT, HEIGHT),
        "size": random.choice([1, 2])
    })

# Game
score = 0
lives = 3
game_over = False

def draw():
    # Rens vinduet
    screen.clear()

    # Tegn stjerner
    for star in stars:
        screen.draw.filled_circle((star["x"], star["y"]), star["size"], "white")

    # Tegn Spiller
    ship.draw()

    # Tegn skud
    for b in bullets:
        b.draw()

    # Tegn Kometer
    for m in meteors:
        m.draw()

    # Game
    if game_over:
        screen.draw.text("GAME OVER", center=(WIDTH/2, HEIGHT/2), fontsize=60, color="red", owidth=1.0)
        screen.draw.text("Tryk R for at genstarte", center=(WIDTH/2, HEIGHT/2+50), fontsize=40, color="white")
    else:
        screen.draw.text(f"Point: {score}", (10, 10), fontsize=40, color="white")
        screen.draw.text(f"Lives: {lives}", (10,50), fontsize=40, color="white")


def update():
    global game_over
    if game_over:
        return

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

    # Kollision mellem skud og komet
    for b in bullets[:]:
        for m in meteors[:]:
            if b.colliderect(m):
                dx = m.x - b.x
                dy = m.y - b.y
                distance = math.hypot(dx, dy)
                if distance <= (m.width/2):
                    global score
                    score += 1
                    bullets.remove(b)
                    meteors.remove(m)
                    break

    # Kollision med komet og spiller
    for m in meteors:
        if m.colliderect(ship):
            dx = ship.x - m.x
            dy = ship.y - m.y
            distance = math.hypot(dx, dy)
            if distance <= (m.width/2):
                meteors.remove(m)
                global lives
                lives -= 1
                if lives < 1:
                    game_over = True
                else:
                    ship.pos = WIDTH/2,HEIGHT/2

                break

    # Skud
    for b in bullets:
        b.x += b.vx
        b.y += b.vy
    for b in bullets:
        if not (0 <= b.x <= WIDTH and 0 <= b.y <= HEIGHT):
            bullets.remove(b)

    # Spawn kometer
    if random.random() < 0.03:
        spawn_meteor()

    # Kometerne
    for m in meteors:
        m.x += m.vx
        m.y += m.vy
        if not (0 <= m.x <= WIDTH and 0 <= m.y <= HEIGHT):
            meteors.remove(m)

def on_key_down(key):
    # Afgiv skud
    if key == keys.SPACE:
        bullet = Actor('bullet')
        bullet.pos = ship.pos
        bullet.angle = ship.angle
        angle_rad = math.radians(bullet.angle)
        bullet.vx = -math.sin(angle_rad) * 8
        bullet.vy = -math.cos(angle_rad) * 8
        bullets.append(bullet)
    elif key == keys.R and game_over:
        reset_game()

def spawn_meteor():
    size = random.choice(["meteor_small", "meteor_large"])
    meteor = Actor(size)

    start_side= random.choice(['top', 'bottom', 'left', 'right'])
    if start_side == 'top':
        meteor.x = random.randint(0, WIDTH)
        meteor.y = 0
    elif start_side == 'bottom':
        meteor.x = random.randint(0, WIDTH)
        meteor.y = HEIGHT
    elif start_side == 'left':
        meteor.x = 0
        meteor.y = random.randint(0, HEIGHT)
    elif start_side == 'right':
        meteor.x = WIDTH
        meteor.y = random.randint(0, HEIGHT)

    meteor.vx = random.uniform(-1.5, 1.5)
    meteor.vy = random.uniform(1, 3)

    meteors.append(meteor)

def reset_game():
    global game_over, score, lives, meteors, bullets
    game_over = False
    score = 0
    lives = 3
    meteors = []
    bullets = []
    ship.pos = (WIDTH/2, HEIGHT/2)
    ship.angle = 0
    ship.vx = 0
    ship.vy = 0
