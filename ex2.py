import pygame
import ImageWriter
import cv2 

def Challenge():
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((1,1))
            self.image.fill((200,30,30))
            self.rect = self.image.get_rect(center = (400,400))
            self.current_health = 200
            self.target_health = 500
            self.max_health = 1000
            self.health_bar_length = 400
            self.health_ratio = self.max_health / self.health_bar_length
            self.health_change_speed = 5

        def get_damage(self,amount):
            if self.target_health > 0:
                self.target_health -= amount
            if self.target_health < 0:
                self.target_health = 0

        def get_health(self,amount):
            if self.target_health < self.max_health:
                self.target_health += amount
            if self.target_health > self.max_health:
                self.target_health = self.max_health

        def update(self):
            self.basic_health()
            self.advanced_health()
            
        def basic_health(self):
            pygame.draw.rect(screen,(255,0,0),(500,10,self.target_health / self.health_ratio,25))
            pygame.draw.rect(screen,(255,0,255),(500,10,self.health_bar_length,25),4)

        def advanced_health(self):
            transition_width = 0
            transition_color = (255,0,0)

            if self.current_health < self.target_health:
                self.current_health += self.health_change_speed
                transition_width = int((self.target_health - self.current_health) / self.health_ratio)
                transition_color = (0,255,0)

            if self.current_health > self.target_health:
                self.current_health -= self.health_change_speed 
                transition_width = int((self.target_health - self.current_health) / self.health_ratio)
                transition_color = (255,255,0)

            health_bar_width = int(self.current_health / self.health_ratio)
            health_bar = pygame.Rect(500,45,health_bar_width,25)
            transition_bar = pygame.Rect(health_bar.right,45,transition_width,25)
            
            pygame.draw.rect(screen,(255,0,0),health_bar)
            pygame.draw.rect(screen,transition_color,transition_bar)	
            pygame.draw.rect(screen,(255,0,255),(500,45,self.health_bar_length,25),4)
    
    # initialise the pygame font
    pygame.font.init()
    
    # Total window
    screen = pygame.display.set_mode((1000, 650))
    
    # Title and Icon
    pygame.display.set_caption("NONOGram")
    img = pygame.image.load('download.jpg')
    pygame.display.set_icon(img) 

    clock = pygame.time.Clock()
    player = pygame.sprite.GroupSingle(Player())
    
    ext = 50
    ext = ext - ext//5 



    x = 0
    y = 0 
    val = 0



    #*******************************************************************************************************************************
    file = 'Batch/GUIpanda2.jpg'
    pic = ImageWriter.loadPicture(file) 
    height = ImageWriter.getHeight(pic)
    width = ImageWriter.getWidth(pic)
    print("***********", height, width)
    ratio = height//ext 
    dif = height/ext
    print("********",ratio)
    black = 0
    line = []
    grid = []

    for x in range(0, width, ratio): 
        for y in range(0, height, ratio):   
            if ImageWriter.getColor(pic,x,y) == [0,0,0]:    
                black = 1
            else: 
                black = 0
            line += [black] 
        grid += [line] 
        line = [] 
    print(grid) 

    fakegrid = []
    line = [] 

    for x in range(0, width, ratio):
        for y in range(0, height, ratio):    
            line += [0] 
        fakegrid += [line] 
        line = [] 
    print(fakegrid) 

    CountRow = []
    seq = []
    count = 0
    for j in range(len(grid[0])):
        for i in range(len(grid)):

            if grid[i][j] == 1:
                count += 1
            else:
                if count != 0:
                    seq += [str(count)]
                    count = 0
        if count !=0:
            seq+= [str(count)]
            count = 0
        CountRow += [seq] 
        seq = [] 
    print(CountRow)

    CountCol = [] 
    seq = ""
    count = 0
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if grid[i][j] == 1:
                count += 1
            else:
                if count != 0:
                    seq += [str(count)]
                    count = 0
        if count !=0:
            seq += [str(count)] 
        CountCol += [seq] 
        seq = []
        count = 0
    print(CountCol) 



    
    # Load test fonts for future use
    font1 = pygame.font.SysFont("comicsans", 10)
    font2 = pygame.font.SysFont("comicsans", 20)
    def get_cord(pos):
        global x
        x = pos[0]//dif 
        
        global y
        y = pos[1]//dif
        print(x,y)
        return [x,y] 



    def draw():
        # Draw the lines
            
        for i in range (ext):
            for j in range (ext):
                if fakegrid[i][j] == 1:
    
                    # Fill blue color in already numbered grid
                    pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))
    
                    # Fill grid with default numbers specified
                if fakegrid[i][j] == 2:
                    fakegrid[i][j] == 0
                    text1 = font1.render("x", 1, (0, 0, 0))
                    screen.blit(text1, (i * dif +3, j * dif - 5)) 
                    

        for j in range(len(CountRow)):
            List1 = CountRow[j] 
            k = 0
            for i in range(len(List1)):              
                text1 = font1.render(List1[i], 1, (0, 0, 0))
                screen.blit(text1, (ext * dif +k + 12, j * dif - 5)) 
                k += dif 

        for i in range(len(CountCol)):
            List1 = CountCol[i]
            k = 0
            for j in range(len(List1)):   
                text1 = font1.render(List1[j], 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 4, ext * dif + k - 4)) 
                k += dif

        # Draw lines horizontally and verticallyto form grid          
        for i in range(51):
            if i % (ext//4) == 0 :
                thick = 3
            else:
                thick = 1
            pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (400, i * dif), thick)
            pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 400), thick) 
    
    # Highlight the cell selected
    def draw_box():
        for i in range(2):
            
            global x 
            global y 

            pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
            pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)
            return [x, y]   
    
    # Raise error when wrong value entered
    def raise_error1():
        text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
        screen.blit(text1, (20, 570)) 
    def raise_error2():
        text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
        screen.blit(text1, (20, 570)) 
    
    # Check if the value entered in board is valid
    def valid(m, i, j):
        if m[i][j] == 1:
            return True
        return False 
    def correct(fakegrid, i,j):
        fakegrid[i][j] = 1
        print("it drew a rect")

    def incorrect(fakegrid, i, j): 
        fakegrid[i][j] = 2
        print("this is incorrect")
    
    def instruction():
        text1 = font2.render("PRESS ENTER TO PLAY", 1, (0, 0, 0))
        text2 = font2.render("YOU EARN 50 points TO YOUR HEALTH BAR EVERY 3 CORRECT ATTEMPTS", 1, (0, 0, 0))
        text3 = font2.render("AND LOSE 20 points FOR EVERY MISTAKE", 1, (0, 0, 0))
        screen.blit(text1, (20, 520))       
        screen.blit(text2, (20, 540))
        screen.blit(text3, (20, 560)) 
    
    # Display options when solved
    def result():
        text1 = font2.render("GAME OVER", 1, (0, 0, 0))
        screen.blit(text1, (20, 570))   
        pygame.draw.rect(screen, (255,255,255), (400, 250, 200, 100))
        text1 = font2.render("GAME OVER!!!", 1, (255, 0, 0))
        screen.blit(text1, (450,275))  
        print("result")



    run = True
    flag1 = 0
    flag2 = 0
    rs = 0
    error = 0
    numberOfCorrect = 0 
    healthLeft = player.sprite.health_bar_length
    gameOver = 0
    win = 0
    # The loop thats keep the window running
    while run:
        
        # White color background
        screen.fill((255, 255, 255))
        # Loop through the events stored in event.get()
        for event in pygame.event.get():
            # Quit the game window
            if event.type == pygame.QUIT:
                run = False 
            # Get the mouse position to insert number   
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag1 = 1
                pos = pygame.mouse.get_pos()
                XY  = get_cord(pos)
                x = XY[0]
                y = XY[1]
            # Get the number to be inserted if key pressed   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x-= 1
                    flag1 = 1
                if event.key == pygame.K_RIGHT:
                    x+= 1
                    flag1 = 1
                if event.key == pygame.K_UP:
                    y-= 1
                    flag1 = 1
                if event.key == pygame.K_DOWN:
                    y+= 1
                    flag1 = 1   
                if event.key == pygame.K_RETURN:
                    flag2 = 1  
                if event.key == pygame.K_k:
                    Challenge()
                if event.key == pygame.K_KP_ENTER:
                    print("you entered")
                    print(x,y)
                    if valid(grid, int(x), int(y)) == True:
                        numberOfCorrect += 1
                        correct(fakegrid, int(x), int(y)) 
                        print(grid, fakegrid)
                        if numberOfCorrect % 3 == 0:
                            player.sprite.get_health(50)
                            healthLeft += 50 
                        if grid == fakegrid:
                            win = 1
                            print("WINNNNNNNN")
                    else: 
                        incorrect(fakegrid, int(x), int(y)) 
                        player.sprite.get_damage(20)
                        healthLeft -= 20 
                        if healthLeft <= 0:
                            print("Game Over")
                            gameOver = 1
        if win == 1:
            pygame.draw.rect(screen, (255,255,255), (0, 0, 600, 600))
            text1 = font2.render("Congratulations!!!", 3, (255, 0, 0))
            screen.blit(text1, (350,300)) 
            img = cv2.imread('Batch/GUIpanda2.jpg')  
            cv2.imshow("Panda", img) 


        if gameOver == 1:  
            pygame.draw.rect(screen, (255,255,255), (0, 0, 700, 600))
            text1 = font2.render("GAME OVER!!!", 3, (255, 0, 0))
            screen.blit(text1, (500,200))  
            text1 = font2.render("Press K to try again", 3, (255, 0, 0))
            screen.blit(text1, (500,300)) 
                            
                            
        draw()    
        if flag1 == 1:
            XY = draw_box() 
            x = XY[0]
            y = XY[1]
        instruction()   
    
        # Update window
    
        player.draw(screen)
        player.update()
        pygame.display.update()
        #clock.tick(60)
    
    # Quit pygame window   
pygame.quit()
if __name__ == "__main__":
    Challenge() 