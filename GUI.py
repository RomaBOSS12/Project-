import pygame 
import sys 
import ex1 
import ex2 
import os 

  
# initializing the constructor 
pygame.init() 
  
# screen resolution 
screen = pygame.display.set_mode((1000, 650))
bg_img = pygame.image.load("Desert.gif")
bg = pygame.transform.scale(bg_img, (1000, 650))

width = 1000
i = 0
mainClock = pygame.time.Clock()
FPS=30
   
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (60,40,20) 
  
# stores the width of the 
# screen into a variable 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 
  
# defining a font 
smallfont = pygame.font.SysFont('Corbel',35) 
bigfont = pygame.font.SysFont('comicsansms',72) 
# rendering a text written in 
# this font 
text = smallfont.render('quit' , True , [255,255,255]) 

text2 = smallfont.render('start' , True , [255,255,255]) 

text3 = bigfont.render('Nonogram' , True , [60,20,200]) 


def Start(bg, i):
    while True: 
        
        for ev in pygame.event.get(): 
            
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                
                #if the mouse is clicked on the 
                # button the game is terminated 
                if width/2-50 <= mouse[0] <= width/2+90 and height/2 <= mouse[1] <= height/2+40: 
                    pygame.quit() 
                
                #if the mouse is clicked on the 
                if width/2-50 <= mouse[0] <= width/2+90 and height/2-50 <= mouse[1] <= height/2-10: 
                    print("start the game")
                    Menu() 
        
        

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 

        #Create looping background
        screen.blit(bg, (i, 0))
        screen.blit(bg, (width+i, 0))
        if i == -width:
            screen.blit(bg, (width+i, 0))
            i = 0
        i -= 0.2
                    
        # fills the screen with a color 
        #screen.fill((60,200,200)) 
        
        # stores the (x,y) coordinates into 
        # the variable as a tuple 
        mouse = pygame.mouse.get_pos() 
        
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        if width/2-50 <= mouse[0] <= width/2+90 and height/2 <= mouse[1] <= height/2+40: 
            pygame.draw.rect(screen,color_light,[width/2-50,height/2,140,40]) 
            
        else: 
            pygame.draw.rect(screen,color_dark,[width/2-50,height/2,140,40]) 

        # stores the (x,y) coordinates into 
        # the variable as a tuple 
        mouse = pygame.mouse.get_pos() 
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        if width/2-50 <= mouse[0] <= width/2+90 and height/2-50 <= mouse[1] <= height/2-10: 
            pygame.draw.rect(screen,color_light,[width/2-50,height/2-50,140,40]) 
            
        else: 
            pygame.draw.rect(screen,color_dark,[width/2-50,height/2-50,140,40]) 
        
        # superimposing the text onto our button 
        screen.blit(text3 , (width/2-120,height/2-170))
        screen.blit(text , (width/2-30,height/2)) 
        screen.blit(text2 , (width/2-30,height/2-50)) 



        
        # updates the frames of the game 
        pygame.display.update()
        mainClock.tick(60)  
def Menu():
    bg_img = pygame.image.load("MainMenu.jpg")
    bg = pygame.transform.scale(bg_img, (1000, 650))

    # defining a font 
    font = pygame.font.SysFont('comicsansms',30) 
    # rendering a text written in 
    # this font 
    main = font.render('Main' , True , [255,255,255]) 
    daily = font.render('My collection' , True , [255,255,255]) 
    collection = font.render('Quit' , True , [255,255,255]) 
    challenge = font.render('Daily Challenges' , True , [255,255,255]) 
    career = font.render('Career Mode' , True , [255,255,255]) 
    play_ch = font.render('Play' , True , [255,255,255]) 
    play_lvl = font.render('Play' , True , [255,255,255]) 




    while True: 
      
        for ev in pygame.event.get(): 
            
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                
                #if the mouse is clicked on the 
                # button the game is terminated 
                if width/2-470 <= mouse[0] <= width/2-270 and height/2 - 210 <= mouse[1] <= height/2-170: 
                    Menu() 
                    pygame.quit()  
                
                #if the mouse is clicked on the 
                if width/2-470 <= mouse[0] <= width/2 - 270 and height/2 - 160 <= mouse[1] <= height/2- 120: 
                    print("Open My Collection AKA Batch")
                    path = "Batch"
                    # Check whether the specified path exists or not
                    isExist = os.path.exists(path)
                    if not isExist:

                        # Create a new directory because it does not exist
                        os.makedirs(path)
                        print("The new directory is created!")
                    os.startfile(path) 
                
                if width/2-470 <= mouse[0] <= width/2 - 270 and height/2 - 110 <= mouse[1] <= height/2- 70: 
                    print("Quit")  
                    pygame.quit() 

                if width/2-100 <= mouse[0] <= width/2 + 50 and height/2 - 160 <= mouse[1] <= height/2- 120: 
                    print("Open the challenge") 
                    ex2.Challenge()

                if width/2+220 <= mouse[0] <= width/2 + 370 and height/2 - 160 <= mouse[1] <= height/2- 120: 
                    print("Open the level game") 
                    ex1.Nonogram() 
    
    

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 

        screen.fill((0,0,0))

        #Create looping background
        screen.blit(bg, (0, 0)) 
                    
        # fills the screen with a color 
        #screen.fill((60,200,200)) 
        
        # stores the (x,y) coordinates into 
        # the variable as a tuple 
        mouse = pygame.mouse.get_pos() 
        
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        if width/2-470 <= mouse[0] <= width/2-190 and height/2 - 210 <= mouse[1] <= height/2-170: 
            pygame.draw.rect(screen,color_light,[width/2-470,height/2 - 210,280,40]) 
            
        else: 
            pygame.draw.rect(screen,color_dark,[width/2-470,height/2 - 210,280,40]) 

       
        # stores the (x,y) coordinates into 
        # the variable as a tuple 
        mouse = pygame.mouse.get_pos() 
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        if width/2-470 <= mouse[0] <= width/2-190 and height/2 - 160 <= mouse[1] <= height/2-120: 
            pygame.draw.rect(screen,color_light,[width/2-470,height/2-160,280,40]) 
            
        else: 
            pygame.draw.rect(screen,color_dark,[width/2-470,height/2-160,280,40]) 
       
       
        # stores the (x,y) coordinates into 
        # the variable as a tuple 
        mouse = pygame.mouse.get_pos() 
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        if width/2-470 <= mouse[0] <= width/2-190 and height/2 - 110 <= mouse[1] <= height/2-70: 
            pygame.draw.rect(screen,color_light,[width/2-470,height/2-110,280,40]) 
            
        else: 
            pygame.draw.rect(screen,color_dark,[width/2-470,height/2-110,280,40]) 

#*********************************************************************************************
         # stores the (x,y) coordinates into 
        # the variable as a tuple 
        mouse = pygame.mouse.get_pos() 
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        if width/2-100 <= mouse[0] <= width/2 + 50 and height/2 - 160 <= mouse[1] <= height/2- 120: 
            pygame.draw.rect(screen,color_light,[width/2-100,height/2-160,150,40]) 
        else: 
            pygame.draw.rect(screen,color_dark,[width/2-100,height/2-160,150,40]) 


         # stores the (x,y) coordinates into 
        # the variable as a tuple 
        mouse = pygame.mouse.get_pos() 
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        if width/2+220 <= mouse[0] <= width/2 + 370 and height/2 - 160 <= mouse[1] <= height/2- 120: 
            pygame.draw.rect(screen,color_light,[width/2+220,height/2-160,150,40]) 
            
        else: 
            pygame.draw.rect(screen,color_dark,[width/2+220,height/2-160,150,40]) 

        
        # superimposing the text onto our button 
        screen.blit(main , (width/2-450,height/2 - 210))
        screen.blit(daily , (width/2-450,height/2-160)) 
        screen.blit(collection , (width/2-450,height/2-110)) 
        screen.blit(challenge , (width/2-120,height/2-210)) 
        screen.blit(career , (width/2+200,height/2-210))  
        screen.blit(play_ch , (width/2-70,height/2-160)) 
        screen.blit(play_lvl , (width/2+250,height/2-160))



        
        # updates the frames of the game 
        pygame.display.update()
        mainClock.tick(60)  

# def Challenge():


# def Level(): 

Start(bg, i) 