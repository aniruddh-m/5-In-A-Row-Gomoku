import pygame

w = 550 # Total width of the window
h = 550 # Total height of the window
x = 30 # Width of the box
y = 30 # Height of the box

grid = []                       # Create a grid filled with zeros
for i in range(15):
    row = []
    for j in range(15):
        row.append(0)
    grid.append(row)

pygame.init() # Initialize the pygame window
screen = pygame.display.set_mode((w,h)) # Create the screen
pygame.draw.line(screen, (0, 200, 200), (x, y), (480, x), (1)) # Form lines on the top and the left
pygame.draw.line(screen, (0, 200, 200), (x, y), (x, 480), (1))

Arial_font = pygame.font.SysFont("Arial", 20) # Initialize font

clock = pygame.time.Clock()

i = 0

# Form the grid
while i < 15: 
    clock.tick(60)
    pygame.display.update()    
    x += 30
    y += 30
    pygame.draw.line(screen, (0, 200, 200), (30, y), (480, x), (1))
    pygame.draw.line(screen, (0, 200, 200), (x, 30), (x, 480), (1))
    i = i + 1

end = False # Flag to check when to stop the game
player = 0 # Decide who has to play
player_sprite = [(255, 0, 0), (0, 0, 255)] # Two different colors for the players
while(not end):
    player = player%2 # Choose next player
    pygame.draw.rect(screen, player_sprite[player], [530, 10, 10, 10]) # Indicate players' turns
    
    for event in pygame.event.get():
        flag = True # Flag to check if the screen is closed
        
        if(event.type == pygame.MOUSEBUTTONDOWN): # Check if a MB is pressed
            x, y = pygame.mouse.get_pos() # Get the position
            
            # Check if the mouse is clicked outside the grid or on an already occupied box
            while(((x not in range(30, 480)) or (y not in range(30, 480))) or (grid[(y-30)//30][(x-30)//30] != 0)):
                pygame.event.get()
                mouse_status = (pygame.mouse.get_pressed()) # Get the new set of locations of the mouse
                # Get the new coordinates of the RMB click
                if(mouse_status[0] == 1):
                    for event_2 in pygame.event.get():
                        if(event.type == pygame.MOUSEBUTTONDOWN):
                            x, y = pygame.mouse.get_pos()
            
            grid[(y-30)//30][(x-30)//30] = player + 1 # Mark the grid
            pygame.draw.rect(screen, player_sprite[player], [((x)//30)*30 + 10, ((y)//30)*30 + 10, 10, 10]) # Mark the box pressed
            player = player + 1
            pygame.display.update() # Make changes to the screen
        
        # Check if the screen is being closed
        if event.type == pygame.QUIT:
            flag = False
            break
    pygame.display.update() # Make changes to the screen
    
    # Go through each row and column and the diagonals for both the players and check if there are 5 consecutive similar sprites
    # Since we're appending 1 for the first person, we check if there are 5 consecutive elements that add up to 5 and whose product is 1
    # Since we're appending 1 for the first person, we check if there are 5 consecutive elements that add up to 10 and whose product is 32
    # If a person wins, indicate the same
    for i in range(15):
        for j in range(11):
            if(grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i][j+3]+grid[i][j+4] == 5 and grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]*grid[i][j+4] == 1):
                end = True
                label = Arial_font.render("PLAYER 1 ROW " + str((x-30)//30 + 1)+ ',' + str((y-30)//30 + 1), 1, (255, 255, 255))
                screen.blit(label, (10, 10))
                pygame.display.update()

    for i in range(11):
        for j in range(15): 
            if(grid[i][j]+grid[i+1][j]+grid[i+2][j]+grid[i+3][j]+grid[i+4][j] == 5 and grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]*grid[i+4][j] == 1):
                end = True
                label = Arial_font.render("PLAYER 1 COLUMN " + str((x-30)//30 + 1)+ ',' + str((y-30)//30 + 1), 1, (255, 255, 255))
                screen.blit(label, (10, 10))
                pygame.display.update()

    for i in range(4, 15):
        for j in range(11):
            if(grid[i][j]+grid[i-1][j+1]+grid[i-2][j+2]+grid[i-3][j+3]+grid[i-4][j+4] == 5 and grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3]*grid[i-4][j+4] == 1):
                end = True
                label = Arial_font.render("PLAYER 1 DIAGONAL 1 " + str((x-30)//30 + 1)+ ',' + str((y-30)//30 + 1), 1, (255, 255, 255))
                screen.blit(label, (10, 10))
                pygame.display.update()

    for i in range(11):
        for j in range(11):
              if(grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]+grid[i+3][j+3]+grid[i+4][j+4] == 5 and grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]*grid[i+4][j+4] == 1):
                  end = True
                  label = Arial_font.render("PLAYER 1 DIAGONAL 2 " + str((x-30)//30 + 1)+ ',' + str((y-30)//30 + 1), 1, (255, 255, 255))
                  screen.blit(label, (10, 10))
                  pygame.display.update()
                  
    for i in range(15):
            for j in range(11):
                if(grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i][j+3]+grid[i][j+4] == 10 and grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]*grid[i][j+4] == 32):
                    end = True
                    label = Arial_font.render("PLAYER 2 ROW " + str((x-30)//30 + 1)+ ',' + str((y-30)//30 + 1), 1, (255, 255, 255))
                    screen.blit(label, (10, 10))
                    pygame.display.update()

    for i in range(11):
            for j in range(15):
                if(grid[i][j]+grid[i+1][j]+grid[i+2][j]+grid[i+3][j]+grid[i+4][j] == 10 and grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]*grid[i+4][j] == 32):
                    end = True
                    label = Arial_font.render("PLAYER 2 COLUMN " + str((x-30)//30 + 1)+ ',' + str((y-30)//30 + 1), 1, (255, 255, 255))
                    screen.blit(label, (10, 10))
                    pygame.display.update()

    for i in range(4, 15):
            for j in range(11):
                if(grid[i][j]+grid[i-1][j+1]+grid[i-2][j+2]+grid[i-3][j+3]+grid[i-4][j+4] == 10 and grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3]*grid[i-4][j+4] == 32):
                    end = True
                    label = Arial_font.render("PLAYER 2 DIAGONAL 1 " + str((x-30)//30 + 1)+ ',' + str((y-30)//30 + 1), 1, (255, 255, 255))
                    screen.blit(label, (10, 10))
                    pygame.display.update()

    for i in range(11):
            for j in range(11):
                  if(grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]+grid[i+3][j+3]+grid[i+4][j+4] == 10 and grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]*grid[i+4][j+4] == 32):
                      end = True
                      label = Arial_font.render("PLAYER 2 DIAGONAL 2 " + str((x-30)//30 + 1)+ ',' + str((y-30)//30 + 1), 1, (255, 255, 255))
                      screen.blit(label, (10, 10))
                      pygame.display.update()
    if(flag == False):
        break

# Wait for the window to get closed
while(1):
    flag = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flag = False
        if(flag == False):
            break
    if(flag == False):
        break