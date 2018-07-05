import pygame
import random
import time
black=(0,0,0)            #game_over
grey=(158,169,156)       # bg color
red=(255,0,0)           #score_display_color
poison=(49,41,88)     #food_color
dark_green=(54,116,14)  #sapola color
area=(800,600)          #area[0]=length,area[1]=height      

pygame.init()
screen=pygame.display.set_mode(area)
pygame.display.set_caption("sapola")
game_over=False

time_manager=pygame.time.Clock()             #for managing the fps
font_msg=pygame.font.SysFont(None,25)
font_score=pygame.font.SysFont(None,25)

chitthi="""YOU LOST...!!!
press:(p) to play_again...
      (q) to quit..."""





def python(unit_len,unit_wid,python_units):    #python is sapola 
    for i in python_units:
        rec=pygame.draw.rect(screen,dark_green,[i[0],i[1],unit_len,unit_wid])
    return rec


def message(msg,color):                     #game_over message
    text=font_msg.render(msg,True,color)
    screen.blit(text,[area[0]/3.0,area[1]/3.0])
    
def score_display(score,color):               #displaying the score_card
    text=font_score.render(score,True,color)
    screen.blit(text,[area[0]/5,area[1]/5])
    
def food(screen,color,x,y,length,width):        #zeher_bhog (generates food)
    rec=pygame.draw.rect(screen,color,[x,y,length,width])
    return rec

def eye(color,x,y,unit_len,eye_len,eye_wid):    #aankh ka color  (color of eye)
    aankh=pygame.draw.rect(screen,color,[x+(unit_len/2),y+(unit_len/2),eye_len,eye_wid])
    return aankh

def game():                          #bhaiya_ji game chalaenge  (starts game)
    unit_len=10
    unit_wid=10
    food_wid=20
    food_len=20
    x,y=(area[0]/2),(area[1]/2)
    direct="east"
    eye_len,eye_wid=2,2
    x_change=0
    y_change=0
    score=0
    food_x=round(random.randrange(0,area[0]-unit_len))
    food_y=round(random.randrange(0,area[1]-unit_len))
    python_units=[]
    py_len=1
    fps=10
    exit=False
    game_over=False
    
    while not exit:
        
        while game_over==True:
            screen.fill(black)
            message(chitthi,red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        exit=True
                        game_over=False
                    elif event.key==pygame.K_p:
                        game()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    if direct=="east" or direct=="west":
                        direct="north"
                            
                                
                elif event.key==pygame.K_DOWN:
                    if direct=="east" or direct=="west":
                        direct="south"
                    
                elif event.key==pygame.K_LEFT:
                    if direct=="north" or direct=="south":
                        direct="west"
                            
                elif event.key==pygame.K_RIGHT:
                    if direct=="north" or direct=="south":
                        direct="east"
        
        
            
        screen.fill(grey)
        food(screen,poison,food_x,food_y,food_len,food_wid)
        python_head=[]
        python_head.append(x)
        python_head.append(y)
        python_units.append(python_head)
        
        if len(python_units)>py_len:
            del(python_units[0])
        score_display("score:"+str(score),red)
        python(unit_len,unit_wid,python_units)
        eye(black,x,y,unit_len,eye_len,eye_wid)
        pygame.display.update()
        
        
        if (x>=food_x and x<=food_x+unit_len) and (y>=food_y and y<=food_y+unit_len):
            score+=100
            food_x=round(random.randrange(0,area[0]-unit_len))
            food_y=round(random.randrange(0,area[1]-unit_len))
            py_len+=1
        
        if x>area[0] or x<0 or y>area[1] or y<0:
            game_over=True
        
        if [x,y] in python_units[:-1]:
            game_over=True
            
            
        if direct=='south':
            y_change=10
            x_change=0
        if direct=='north':
            y_change=-10
            x_change=0
        if direct=='east':
            x_change=10
            y_change=0
        if direct=='west':
            x_change=-10
            y_change=0
        
        time_manager.tick(fps)
        
        x=x+x_change
        y=y+y_change
        
        
    pygame.quit()
    quit()
            
            
game()