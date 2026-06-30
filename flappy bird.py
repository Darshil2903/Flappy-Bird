import pygame
from pygame.locals import*
import sys
import random
import time


FPS= 50
SCREENWIDTH= 500
SCREENHEIGHT= 700
SCREEN= pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY= SCREENHEIGHT*0.8
HIGHSCORE=0
GAME_SPRITES={}
GAME_SOUNDS={}

BIRD ='\\Darshil Folder\\darshil python practise\\Pygame\\bird.png'
BIRD1 ='\\Darshil Folder\\darshil python practise\\Pygame\\bird1.png'
PIPE ='\\Darshil Folder\\darshil python practise\\Pygame\\pipe.png'
BASE ='\\Darshil Folder\\darshil python practise\\Pygame\\base.jpeg'
BACKGROUND='\\Darshil Folder\\darshil python practise\\Pygame\\background.jpeg'
MESSAGE ="\\Darshil Folder\\darshil python practise\\Pygame\\messages.png"
CLICK='\\Darshil Folder\\darshil python practise\\Pygame\\Click.png'

def WelcomeScreen(GAME_SPRITES):
    Birdx=int(SCREENWIDTH/5+30)
    Birdy=int(SCREENHEIGHT/2)
    Messagey=SCREENHEIGHT*0.10

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or(event.type==KEYDOWN and event.key == K_ESCAPE):
                # A=GAME_SPRITES['bird'].get_height()
                # print(A)
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_KP_ENTER or event.key==K_UP):
                return
            else:
                pygame.Surface.blit(SCREEN,GAME_SPRITES['background'],(0, 0))
                pygame.Surface.blit(SCREEN,GAME_SPRITES['pipe1'],(20,-335)) #350,450
                pygame.Surface.blit(SCREEN,GAME_SPRITES['pipe2'],(20,217))#50,-50
                pygame.Surface.blit(SCREEN,GAME_SPRITES['pipe1'],(400,-100))#50,-50
                pygame.Surface.blit(SCREEN,GAME_SPRITES['pipe2'],(400,455))#50,-50
                pygame.Surface.blit(SCREEN,GAME_SPRITES['base'],(0,GROUNDY+30))
                pygame.Surface.blit(SCREEN,GAME_SPRITES['Message'],(50,Messagey))
                pygame.Surface.blit(SCREEN,GAME_SPRITES['bird1'],(Birdx,Birdy))
                pygame.Surface.blit(SCREEN,GAME_SPRITES['click'],(50,GROUNDY+30))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def Crash(pipedir,BirdStart,Game,pipe1):
    if -5<pipedir<=175:
        if BirdStart <=(pipe1['y1']+380):
            
            print(" YOU CRASHED!!")
            

            return True
        if BirdStart+45>=(pipe1['y2'] ):
            print(" YOU CRASHED!!")
           
            return True
    
def getpipe(pipe):
    pipe['y1']=-1*random.randint(0,325)
    pipe['y2']=pipe['y1']+555
    return pipe

def out(HIGHSCORE,POINT):
   pass
    
def MainGame():
    
    pipe={}
    POINT=0
    pipe1=getpipe(pipe)
    pipedir=SCREENWIDTH+100
    GroundX=0
    GROUNDY= SCREENHEIGHT*0.8  
    Birdx=SCREENWIDTH*0.2
    BirdFall=-5.5
    BirdStart=SCREENHEIGHT/2
    Game=True
    while Game==True:
        SCREEN.blit(GAME_SPRITES['pipe1'],(pipedir,pipe1['y1'])) 
        SCREEN.blit(GAME_SPRITES['pipe2'],(pipedir,pipe1['y2']))
        if pipedir<=-100:
            POINT+=1
            pipedir+=SCREENWIDTH+10+100
            pipe1=getpipe(pipe)
        pipedir-=7
        crash=Crash(pipedir,BirdStart,Game,pipe1)
        if crash is True:
            out(HIGHSCORE,POINT)
            print('Your Score Is:',POINT)
            # POINT==0
            
            POINT==0
            WelcomeScreen(GAME_SPRITES)
            BirdStart=SCREENHEIGHT/2
            Game==False
            return
        
        SCREEN.blit(GAME_SPRITES['base'],(GroundX,GROUNDY+30))
        for event in pygame.event.get():
            if event.type == QUIT or(event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN and event.key == K_SPACE:
                BirdStart-=50
                pipedir-=10
                 


                
                pygame.display.update()
                SCREEN.blit(GAME_SPRITES['bird'],(Birdx,BirdStart))
               
                
            
            FPSCLOCK.tick(FPS)
        if BirdStart==520 or (BirdStart<=0):
            print('Your Score Is:',POINT)
            # POINT==0
            out(HIGHSCORE,POINT)
            WelcomeScreen(GAME_SPRITES)
            Game=False
            print("you are dead")
            BirdStart=SCREENHEIGHT/2
            return
            
        else:
            pygame.display.update()
            pygame.Surface.blit(SCREEN,GAME_SPRITES['background'],(0, 0))
            pygame.Surface.blit(SCREEN,GAME_SPRITES['base'],(0,GROUNDY+10))
            SCREEN.blit(GAME_SPRITES['bird'],(Birdx,BirdStart))
            
            FPSCLOCK.tick(FPS)
            BirdStart-=BirdFall   
      
        
if __name__ == "__main__":
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    pygame.display.set_caption('FLappy Bird by Darshil')
    GAME_SPRITES['Message']= pygame.image.load(MESSAGE)
     
    GAME_SPRITES['pipe2']=pygame.image.load(PIPE).convert_alpha()
    GAME_SPRITES['pipe1']=pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180)
    GAME_SPRITES['base']=  pygame.image.load(BASE).convert_alpha()
    GAME_SPRITES['bird']= pygame.image.load(BIRD).convert_alpha()
    GAME_SPRITES['bird1']= pygame.image.load(BIRD1).convert_alpha()
    GAME_SPRITES['background']= pygame.image.load(BACKGROUND).convert_alpha()
    GAME_SPRITES['click']= pygame.image.load(CLICK).convert_alpha()

while True:
    WelcomeScreen(GAME_SPRITES)
    MainGame()