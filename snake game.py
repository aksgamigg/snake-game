# Modules
from turtle import Turtle, Screen
import time as t
import random as r

# Functions
def lef():
    snake_blocks[0].left(90)

def righ():
    snake_blocks[0].right(90)

def powerupgen():
    global powers, poweruptype, poweronscreen
    power = r.randint(0,1000)
    if power > 990:
        powertype = r.randint(1,3)
        poweronscreen = True
        if powertype == 1:
            powerupx = r.randint(-270, 270)
            powerupy = r.randint(-270, 270)
            powerup = Turtle()
            powerup.penup()
            powerup.color('blue')
            powerup.shape('circle')
            powerup.setpos(powerupx, powerupy)
            powers.append(powerup)
        elif powertype == 2:
            powerupx = r.randint(-270, 270)
            powerupy = r.randint(-270, 270)
            powerup = Turtle()
            powerup.penup()
            powerup.color('purple')
            powerup.shape('circle')
            powerup.setpos(powerupx, powerupy)
            powers.append(powerup)
        else:
            powerupx = r.randint(-270, 270)
            powerupy = r.randint(-270, 270)
            powerup = Turtle()
            powerup.penup()
            powerup.color('darkgreen')
            powerup.shape('circle')
            powerup.setpos(powerupx, powerupy)
            powers.append(powerup)
        poweruptype = powerup.color()
        poweruptype = poweruptype[0]

def fruitgen():
    global fruits
    fruitx = r.randint(-270, 270)
    fruity = r.randint(-270, 270)
    fruit = Turtle()
    fruit.penup()
    fruit.color('red')
    fruit.shape('circle')
    fruit.setpos(fruitx, fruity)
    fruits.append(fruit)

def snakegen():
    global snake_blocks
    new_snake = Turtle()
    new_snake.color('green')
    new_snake.shape('square')
    new_snake.speed(0)
    new_snake.penup()
    snake_blocks.append(new_snake)
    for it in range(0, len(snake_blocks), 2):
        snake_blocks[it].color('dark green')

def gameover():
    global game_on
    screen.update()
    game_on = False
    tu.goto(0, 0)
    tu.pencolor('White')
    tu.write(arg='GAME OVER', align='center', font=('Arial', 28, "bold"))
    screen.onkey(None, 'Left')
    screen.onkey(None, 'Right')
    screen.onkey(None, 'a')
    screen.onkey(None, 'd')
    screen.onkey(None, 'space')

def collision():
    global snake_blocks
    global game_on
    x = snake_blocks[0].xcor()
    y = snake_blocks[0].ycor()
    for i1 in range(1, len(snake_blocks)-1):
        xi = snake_blocks[i1].xcor()
        yi = snake_blocks[i1].ycor()
        if -19<=x-xi<=19 and -19<=y-yi<=19:
            gameover()
            return
        elif x >= 300 or y >= 300:
            gameover()
            return
        elif x <= -300 or y <= -300:
            gameover()
            return

def pause():
    global game_pause
    game_pause = True
    if game_pause:
        tu.goto(0, 0)
        tu.pencolor('white')
        tu.write(arg="Game Paused", align='center', font=('Arial', 28, "bold"))
        screen.update()
        while game_pause:
            t.sleep(0.1)
            screen.listen()
            screen.onkey(key='space', fun=unpause)
            screen.update()

def unpause():
    global game_pause
    if game_pause:
        tu.goto(0, 0)
        tu.clear()
        tusetup()
        game_pause = False
        screen.onkey(key='space', fun=pause)
        ttimer()


def scorewriting():
    global score
    global scorestring
    tu.goto(x=0, y=250)
    tu.clear()
    scorestring = f"{gamemode.title()} Mode    Highscore:{highscore}    Score:{score}"
    tu.pencolor('white')
    tu.write(arg=scorestring, align='center', font=('Arial', 18, 'bold'))

def tusetup():
    scorewriting()
    tu.goto(-300, -300)
    tu.pencolor('white')
    tu.pd()
    for i3 in range(4):
        tu.fd(600)
        tu.lt(90)
    tu.pu()

def ttimer():
    a = 3
    tu.pencolor('white')
    for i4 in range(3):
        tu.clear()
        tusetup()
        tu.goto(0, 0)
        tu.write(arg=str(a), align='center', font=('Arial', 38, 'bold'))
        screen.update()
        t.sleep(1)
        a-=1
    tu.clear()
    tusetup()
    tu.goto(0, 0)
    tu.write(arg="Go!", align='center', font=('Arial', 38, 'bold'))
    t.sleep(0.2)
    tu.clear()
    tusetup()

def cheatcodes():
    global cheat_codes, cheats, gamespeed, screen, score, cheatson
    screen.title("Cheat Codes Run")
    msg  = "Enter a cheatcode:"
    slowprompt = "By how many centiseconds do you want to slow your snake(Min: 0, Max: 10):"
    speedprompt = f"How many centiseconds do you want to set the gamespeed\nThe default is {gamespeed*100}\nThe minimum you can set it is 3 and the maximum is 20:"
    while True:
        cheats = screen.textinput(title="Cheats Activation", prompt= msg).lower().strip()
        if cheats in cheat_codes:
            cheatson = True
            break
        else:
            msg = "Please enter a valid cheatcode:"

    if cheats == "slow":
        while True:
            slowtime = screen.textinput(prompt=slowprompt, title="Slow Your Snake")
            try:
                slowtime = int(slowtime)
                if 10>slowtime>0:
                    break
                else:
                    slowprompt = "Please enter a valid slowing time in the range of 0-10:"
            except ValueError:
                slowprompt = "Please enter a valid slowing time in the range of 0-10:"
        slowtime /= 100
        gamespeed += slowtime

    if cheats == "setspeed":
        while True:
            gspeed = screen.textinput(prompt=speedprompt, title="Slow Your Snake")
            try:
                gspeed = int(gspeed)
                if 10 > gspeed > 0:
                    break
                else:
                    speedprompt = "Please enter a valid slowing time in the range of 0-10:"
            except ValueError:
                speedprompt = "Please enter a valid slowing time in the range of 0-10:"
        gspeed /= 100
        gamespeed = gspeed

    if cheats == "bigsnake":
        cheats = "invincible"
        for _ in range(10):
            snakegen()
        score += 10

    if cheats == "biggersnake":
        cheats = "invincible"
        for _ in range(25):
            snakegen()
        score += 25

    if cheats == "disablecheat":
        cheats = ""
    controlactivation()

def endingscreen():
    global tu, game_on
    tu.clear()
    tusetup()
    tu.goto(0, 0)
    tu.write(arg="Thanks for Playing!", align='center', font=('Arial', 28, 'bold'))
    screen.update()
    t.sleep(1.5)
    game_on = False
    exit()

def controlactivation():
    screen.listen()
    screen.onkey(key='Left', fun=lef)
    screen.onkey(key='Right', fun=righ)
    screen.onkey(key='a', fun=lef)
    screen.onkey(key='d', fun=righ)
    screen.onkey(key='space', fun=pause)
    screen.onkey(key='/', fun=cheatcodes)
    screen.onkey(key='q', fun=endingscreen)

def game():
    global game_on, gamespeed, highscore, score, gamemode, speedup1, speedup2, snake_blocks, screen, cheats, fruits, tu, scoremultiplier, poweronscreen, poweruptype, powers
    while game_on:
        t.sleep(gamespeed)
        screen.update()
        if not poweronscreen:
            powerupgen()
        for i in range(len(snake_blocks)-1, 0, -1):
            new_x = snake_blocks[i-1].xcor()
            new_y = snake_blocks[i-1].ycor()
            snake_blocks[i].goto(new_x, new_y)
        snake_blocks[0].forward(20)
        if snake_blocks[0].distance(fruits[0])<=19:
            snakegen()
            fruits[0].hideturtle()
            fruits.pop(0)
            score += 1*scoremultiplier
            if score > highscore:
                highscore = score
                with open("highscore.txt", "w") as hs:
                    hs.write(str(highscore))
            tusetup()
            fruitgen()
        if poweronscreen:
            if snake_blocks[0].distance(powers[0])<=19:
                powers[0].hideturtle()
                powers.pop(0)
                poweronscreen = False
                if poweruptype == "blue":
                    for _ in range (2):
                        snakegen()
                    score += 2
                    tusetup()
                elif poweruptype == "darkgreen":
                    score += 5
                    tusetup()
                else:
                    if scoremultiplier < 5:
                        scoremultiplier += 1
        if cheats != "invincible":
            collision()
        if not speedup1:
            speedup1 = True
            if score >= 10:
                gamespeed -= 0.004
        if not speedup2:
            speedup2 = True
            if score >= 25:
                gamespeed -= 0.006

    if not game_on:
        while True:
            ans = screen.textinput(title="Replay Option", prompt="Do you want to play the game again?").lower().strip()
            if ans in ["yes", "y", "no", "n", "quit", "restart", "replay", "continue"]:
                break
        if ans in ["no", "n", "quit"]:
            endingscreen()
        elif ans == "continue":
            game_on = True
            cheats = "invincible"
            tu.clear()
            tusetup()
            for a in range(len(snake_blocks)-1, 0, -1):
                absicsa = snake_blocks[a].xcor()
                ordinate = snake_blocks[a].ycor()
                snake_blocks[a].goto(absicsa-20, ordinate)
            controlactivation()
            game()
        else:
            screen.clear()

# Resources and base setup
with open("highscore.txt", "r") as hs:
    highscore = int(hs.read())
cheatson = False
while True:
    gamespeed = 0
    game_on = True
    game_pause = False
    score = 0
    scoremultiplier = 1
    scorestring = f"Score:{score}"
    fruits = []
    powers = []
    poweruptype = ""
    poweronscreen = False
    cheats = ""
    cheat_codes = ["invincible", "slow", "setspeed", "bigsnake", "biggersnake", "disablecheat"]
    speedup1 = False
    speedup2 = False

    screen = Screen()
    screen.setup(600, 600)
    screen.bgcolor('black')
    screen.title('Snake Game')
    screen.tracer(0)

    snake_blocks = []
    for i in range(3):
        snakegen()

    tu = Turtle()
    tu.hideturtle()
    tu.penup()
    tu.goto(-300, -300)
    tu.pencolor('white')
    tu.pd()
    for i in range(4):
        tu.fd(600)
        tu.lt(90)
    tu.pu()
    tu.goto(x=0, y=250)
    tu.write(arg = scorestring, align='center', font=('Arial', 18, 'bold'))



    while True:
        gamemode = screen.textinput(title=f"Game mode", prompt="Choose a game mode: Easy, Medium, Hard, Extreme or Impossible?").strip().lower()
        if gamemode in ["easy", "medium", "hard", "extreme", "impossible"]:
            if gamemode == "easy":
                gamespeed = 0.075
            elif gamemode == "medium":
                gamespeed = 0.06
            elif gamemode == "hard":
                gamespeed = 0.05
            elif gamemode == "extreme":
                gamespeed = 0.04
            else:
                gamespeed = 0.03
            break

    ttimer()

    controlactivation()

    fruitgen()
    powerupgen()
    game()