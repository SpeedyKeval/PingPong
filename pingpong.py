import pygame as game
import random, math

## to start the module it is mandatory (constructor call) 
game.init()

WIDTH = 800
HEIGHT = 600

def start_randomly():
    global ballxch, ballych
    
    sign = [1,-1]
    
    # Randomly initialization of ball movement and speed
    ballxch = (random.uniform(0.3,1.1)*4) * random.choice(sign)
    ballych = (random.uniform(0.3,1.1)*4) * random.choice(sign)
    
    # Angle between initial x change and y change 
    ''' Important in terms of initialization of both the change units as they don't give a bad start to the game '''
    ang = math.degrees(math.atan(ballych/ballxch))
    
    while ang <= 1 and ang >= 85:
        ballxch = random.uniform(0.3,1.1)*4
        ballych = random.uniform(0.3,1.1)*4
        
        ang = math.degrees(math.atan(ballych/ballxch))

def text(string,style="monospace",size=15,width=1,color=(255,255,0)):
    myfont = game.font.SysFont(style, size)
    # render text
    label = myfont.render(string, size, color)
    return label
    
start_randomly()

# Accelerating the speed of the ball
ACC = (random.uniform(0.3,1.1)*2, random.uniform(0.3,1.1)*2)

## form a frame or window to start (main frame)
## set_mode(window_size,flag,depth)
gameDis = game.display.set_mode((WIDTH+130,HEIGHT))

## title to the window 
game.display.set_caption('Hi Pygame')

clock = game.time.Clock()

crashed = False

## load an image to pygame module
car = game.image.load('Ball.png')

## rescale the size 
ball = game.transform.scale(car,(25,25))

# Position of the ball 
ballx,bally = WIDTH/2-12,HEIGHT/2-4

# Starting position of the ball
START = (ballx,bally) 

left_change = 0
right_change = 0

# Position of the left Padle initially 
startposl = [20,HEIGHT/2-30]
endposl = [20,HEIGHT/2+30]

# Position of the Right Padle initially
startposr = [780,HEIGHT/2-30]
endposr = [780,HEIGHT/2+30]

# index = 0 for left padle score and index = 1 for the right padle
score = [0,0]

while not crashed:
    for event in game.event.get():
        if event.type == game.QUIT:
            crashed = True
    
    ## fill the background colour
    gameDis.fill((0,0,0))
    
    #Line just after the padle on left
    game.draw.line(gameDis,(255,255,0),(24,0),(24,600))
    
    #Line just before the padle on the right
    game.draw.line(gameDis,(255,255,0),(776,0),(776,600))
    
    # Line at the center of the frame
    game.draw.line(gameDis,(255,255,255),(WIDTH/2,0),(WIDTH/2,HEIGHT),1)    
    # Box playing area
    game.draw.rect(gameDis,(0,255,0),[0,0,800,600],10)
    # Cricle at center
    game.draw.circle(gameDis,(255,255,255),[int(WIDTH/2)-1,int(HEIGHT/2)+5],50,2)
    
    # Instruction 
    gameDis.blit(text('Press "R"'),(820,200))
    gameDis.blit(text('for Restart'),(820,230))
    
    ballx += ballxch
    bally += ballych
    
    if ballx >= WIDTH-35:
        if startposr[1]+40 >= bally and startposr[1]-20 <= bally:
            ballxch, ballych = -ballxch, ballych+ACC[1]
        else:
            # Score of the First Player
            score[0] += 10
            
            ballx, bally = START
            start_randomly()
    elif ballx <= 10:
        if startposl[1]+40 >= bally and startposl[1]-20 <= bally:
            ballxch, ballych = -ballxch, ballych+ACC[1]
        else:
            # Score of the First Player 
            score[1] += 10
            
            ballx, bally = START
            start_randomly()
    
    gameDis.blit(text('Player 1:'+str(score[0])),(820,70))
    gameDis.blit(text('Player 2:'+str(score[1])),(820,100))
    
    if bally <= 10:
        ballxch, ballych = ballxch, -ballych
    elif bally >= HEIGHT-43:
        ballxch, ballych = ballxch, -ballych
    
    ## display the image on the frame
    gameDis.blit(ball,(ballx, bally))
    
    if event.type == game.KEYDOWN:
        if event.key == game.K_w:
            left_change = -5
        elif event.key == game.K_s:
            left_change = 5
        elif event.key == game.K_DOWN:
            right_change = 5
        elif event.key == game.K_UP:
            right_change = -5
        elif event.key == game.K_r:
            ballx, bally = START
            score = [0,0]
            start_randomly()
            
    if event.type == game.KEYUP:
        if event.key == game.K_w or event.key == game.K_s:
            left_change = 0
        if event.key == game.K_UP or event.key == game.K_DOWN:
            right_change = 0

    # Left paddle movement according to the size of the window
    if startposl[1] >= 20 and endposl[1] <= HEIGHT-20:
        startposl[1] += right_change
        endposl[1] += right_change
    elif startposl[1] < 20 and right_change == +5:
        startposl[1] += right_change
        endposl[1] += right_change
    elif endposl[1] > HEIGHT-20 and right_change == -5:
        startposl[1] += right_change
        endposl[1] += right_change
    #y += right_change
    
    if startposr[1] >= 20 and endposr[1] <= HEIGHT-20:
        startposr[1] += left_change
        endposr[1] += left_change
    elif startposr[1] < 20 and left_change == +5:
        startposr[1] += left_change
        endposr[1] += left_change
    elif endposr[1] > HEIGHT-20 and left_change == -5:
        startposr[1] += left_change
        endposr[1] += left_change
    
    game.draw.line(gameDis, (255,255,0), startposl, endposl, 10)
    game.draw.line(gameDis, (255,255,0), startposr, endposr, 10)
    game.display.update()
    clock.tick(60)
    
game.quit()