import pygame
background_colour = (0,179,30)
button_color = (179,0,179)
button_win = (179,0,0)
(width, height) = (750,650)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic-Tac-Toe Game')
screen.fill(background_colour)
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 120)
winner = False
font = pygame.font.SysFont('Arial', 48)
font1 = pygame.font.SysFont('Arial', 25)
player_turn = 1
game_grid = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

p1_score = 0
p2_score = 0

score_title = font1.render('Player Scores', True, (255, 255, 255))
p1 = font1.render('  Player 1: ' + str(p1_score), True, (255, 255, 255))
p2 = font1.render('  Player 2: ' + str(p2_score), True, (255, 255, 255))
screen.blit(score_title, (5, 5))
screen.blit(p1, (5, 35))
screen.blit(p2, (5, 62))

button1 = pygame.draw.rect(screen,button_color,(125,100,125,125))
button2 = pygame.draw.rect(screen,button_color,(300,100,125,125))
button3 = pygame.draw.rect(screen,button_color,(475,100,125,125))

button4 = pygame.draw.rect(screen,button_color,(125,275,125,125))
button5 = pygame.draw.rect(screen,button_color,(300,275,125,125))
button6 = pygame.draw.rect(screen,button_color,(475,275,125,125))

button7 = pygame.draw.rect(screen,button_color,(125,450,125,125))
button8 = pygame.draw.rect(screen,button_color,(300,450,125,125))
button9 = pygame.draw.rect(screen,button_color,(475,450,125,125))

button10 = pygame.draw.rect(screen,background_colour,(125,585,475,55))

text = font.render('Player: ' + str(player_turn) + "'s turn", True, (0, 0, 0))
screen.blit(text, (200, 25))
pygame.display.flip()
running = True
print(player_turn)

def game_update(clicked_button, player):
    global game_grid
    global player_turn
    screen.fill(pygame.Color(background_colour), (150, 25, 400, 70))
    if player_turn == 1:
        game_grid[clicked_button] = "X"
        player_turn = 2
        text = font.render("Player: 2's turn", True, (0, 0, 0))
        screen.blit(text, (200, 25))
        pygame.display.flip()

    elif player_turn == 2:
        game_grid[clicked_button] = "O"
        player_turn = 1
        text = font.render("Player: 1's turn", True, (0, 0, 0))
        screen.blit(text, (200, 25))
        
    
    pygame.display.flip()
    reload_buttons()
    winner_check()
    print(player_turn)

def reload_buttons():
    
    button1text = myfont.render(game_grid[0], True, (45, 45, 45))
    button2text = myfont.render(game_grid[1], True, (45, 45, 45))
    button3text = myfont.render(game_grid[2], True, (45, 45, 45))

    button4text = myfont.render(game_grid[3], True, (45, 45, 45))
    button5text = myfont.render(game_grid[4], True, (45, 45, 45))
    button6text = myfont.render(game_grid[5], True, (45, 45, 45))

    button7text = myfont.render(game_grid[6], True, (45, 45, 45))
    button8text = myfont.render(game_grid[7], True, (45, 45, 45))
    button9text = myfont.render(game_grid[8], True, (45, 45, 45))

    if game_grid[0] == "X" or game_grid[0] == "O":
        screen.blit(button1text,(140,75))
    
    if game_grid[1] == "X" or game_grid[1] == "O":
        screen.blit(button2text,(315,75))

    if game_grid[2] == "X" or game_grid[2] == "O":
        screen.blit(button3text,(495,75))

    if game_grid[3] == "X" or game_grid[3] == "O":
        screen.blit(button4text,(140,250))
    
    if game_grid[4] == "X" or game_grid[4] == "O":
        screen.blit(button5text,(315,250))
    
    if game_grid[5] == "X" or game_grid[5] == "O":
        screen.blit(button6text,(495,250))

    if game_grid[6] == "X" or game_grid[6] == "O":
        screen.blit(button7text,(140,425))
    
    if game_grid[7] == "X" or game_grid[7] == "O":
        screen.blit(button8text,(315,425))
    
    if game_grid[8] == "X" or game_grid[8] == "O":
        screen.blit(button9text,(495,425))
    pygame.display.update()
    
def new_game():
    global game_grid
    global winner
    global player_turn 
    winner = False
    player_turn = 1
    game_grid = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    screen.fill(background_colour)
    pygame.draw.rect(screen,button_color,(125,100,125,125))
    pygame.draw.rect(screen,button_color,(300,100,125,125))
    pygame.draw.rect(screen,button_color,(475,100,125,125))

    pygame.draw.rect(screen,button_color,(125,275,125,125))
    pygame.draw.rect(screen,button_color,(300,275,125,125))
    pygame.draw.rect(screen,button_color,(475,275,125,125))

    pygame.draw.rect(screen,button_color,(125,450,125,125))
    pygame.draw.rect(screen,button_color,(300,450,125,125))
    pygame.draw.rect(screen,button_color,(475,450,125,125))

    pygame.draw.rect(screen,background_colour,(125,585,475,55))
    
    text = font.render('Player: ' + str(player_turn) + "'s turn", True, (0, 0, 0))
    p1 = font1.render('  Player 1: ' + str(p1_score), True, (255, 255, 255))
    p2 = font1.render('  Player 2: ' + str(p2_score), True, (255, 255, 255))
    screen.blit(p1, (5, 35))
    screen.blit(p2, (5, 62))
    screen.blit(score_title, (5, 5))
    
    screen.blit(text, (200, 25))
    
    pygame.display.flip()

    print("P1: " + str(p1_score))
    print("P2: " + str(p2_score))

def winner_check():
    global p1_score
    global p2_score
    global winner
    screen.fill(pygame.Color(background_colour), (150, 25, 400, 70))
    font = pygame.font.SysFont('Arial', 48)
    player_winner = ""
    restart_text = font.render("Do you want to try again?", True, (0, 0, 0))
    if game_grid[1] == game_grid[0] and game_grid[2] == game_grid[0]:
        # 0 - 1 - 2
        pygame.draw.rect(screen,button_win,(125,100,125,125))
        pygame.draw.rect(screen,button_win,(300,100,125,125))
        pygame.draw.rect(screen,button_win,(475,100,125,125))
        
        if game_grid[1] == "X":
            player_winner = "1"
            p1_score += 1
           
        else:
            player_winner = "2"
            p2_score += 1
            

        screen.blit(score_title, (5, 5))
        
        font = pygame.font.SysFont('Arial', 48)
        text1 = font.render(f"Player {player_winner} Wins!", True, (0, 0, 0))
        screen.blit(text1, (200, 25))
        reload_buttons()
        pygame.draw.rect(screen,button_color,(125,585,475,55))
        
        screen.blit(restart_text, (140, 580))
        pygame.display.flip()
        winner = True

    elif game_grid[3] == game_grid[0] and game_grid[6] == game_grid[0]:
        # 0 - 3 - 6
        pygame.draw.rect(screen,button_win,(125,100,125,125))
        pygame.draw.rect(screen,button_win,(125,275,125,125))
        pygame.draw.rect(screen,button_win,(125,450,125,125))
        if game_grid[3] == "X":
            player_winner = "1"
            p1_score += 1
           
        else:
            player_winner = "2"
            p2_score += 1
        
        font = pygame.font.SysFont('Arial', 48)
        text1 = font.render(f"Player {player_winner} Wins!", True, (0, 0, 0))
        screen.blit(text1, (200, 25))
        reload_buttons()
        pygame.draw.rect(screen,button_color,(125,585,475,55))
        screen.blit(restart_text, (140, 580))
        pygame.display.flip()
        winner = True
    elif game_grid[4] == game_grid[0] and game_grid[8] == game_grid[0]:
        # 0 - 4 - 8
        pygame.draw.rect(screen,button_win,(125,100,125,125))
        pygame.draw.rect(screen,button_win,(300,275,125,125))
        pygame.draw.rect(screen,button_win,(475,450,125,125))
        if game_grid[4] == "X":
            player_winner = "1"
            p1_score += 1
           
        else:
            player_winner = "2"
            p2_score += 1
        
        font = pygame.font.SysFont('Arial', 48)
        text1 = font.render(f"Player {player_winner} Wins!", True, (0, 0, 0))
        screen.blit(text1, (200, 25))
        reload_buttons()
        pygame.draw.rect(screen,button_color,(125,585,475,55))
        screen.blit(restart_text, (140, 580))
        pygame.display.flip()


        winner = True
    elif game_grid[4] == game_grid[3] and game_grid[5] == game_grid[3]:
        # 3 - 4 - 5
        pygame.draw.rect(screen,button_win,(125,275,125,125))
        pygame.draw.rect(screen,button_win,(300,275,125,125))
        pygame.draw.rect(screen,button_win,(475,275,125,125))
        if game_grid[4] == "X":
            player_winner = "1"
            p1_score += 1
           
        else:
            player_winner = "2"
            p2_score += 1
        
        font = pygame.font.SysFont('Arial', 48)
        text1 = font.render(f"Player {player_winner} Wins!", True, (0, 0, 0))
        screen.blit(text1, (200, 25))
        reload_buttons()
        pygame.draw.rect(screen,button_color,(125,585,475,55))
        screen.blit(restart_text, (140, 580))
        pygame.display.flip()
        winner = True
    elif game_grid[7] == game_grid[6] and game_grid[8] == game_grid[6]:
        # 6 - 7 - 8
        pygame.draw.rect(screen,button_win,(125,450,125,125))
        pygame.draw.rect(screen,button_win,(300,450,125,125))
        pygame.draw.rect(screen,button_win,(475,450,125,125))
        if game_grid[7] == "X":
            player_winner = "1"
            p1_score += 1
           
        else:
            player_winner = "2"
            p2_score += 1
        
        font = pygame.font.SysFont('Arial', 48)
        text1 = font.render(f"Player {player_winner} Wins!", True, (0, 0, 0))
        screen.blit(text1, (200, 25))
        reload_buttons()
        pygame.draw.rect(screen,button_color,(125,585,475,55))
        screen.blit(restart_text, (140, 580))
        pygame.display.flip()

        
        winner = True
    elif game_grid[7] == game_grid[1] and game_grid[4] == game_grid[1]:
        # 1 - 4 - 7
        pygame.draw.rect(screen,button_win,(300,100,125,125))
        pygame.draw.rect(screen,button_win,(300,275,125,125))
        pygame.draw.rect(screen,button_win,(300,450,125,125))
        if game_grid[4] == "X":
            player_winner = "1"
            p1_score += 1
           
        else:
            player_winner = "2"
            p2_score += 1
        
        font = pygame.font.SysFont('Arial', 48)
        text1 = font.render(f"Player {player_winner} Wins!", True, (0, 0, 0))
        screen.blit(text1, (200, 25))
        reload_buttons()
        pygame.draw.rect(screen,button_color,(125,585,475,55))
        screen.blit(restart_text, (140, 580))
        pygame.display.flip()

        winner = True
    elif game_grid[8] == game_grid[2] and game_grid[5] == game_grid[2]:
        # 2 - 5 - 8
        pygame.draw.rect(screen,button_win,(475,100,125,125))
        pygame.draw.rect(screen,button_win,(475,275,125,125))
        pygame.draw.rect(screen,button_win,(475,450,125,125))
        if game_grid[5] == "X":
            player_winner = "1"
            p1_score += 1
           
        else:
            player_winner = "2"
            p2_score += 1
        
        font = pygame.font.SysFont('Arial', 48)
        text1 = font.render(f"Player {player_winner} Wins!", True, (0, 0, 0))
        screen.blit(text1, (200, 25))
        reload_buttons()
        pygame.draw.rect(screen,button_color,(125,585,475,55))
        screen.blit(restart_text, (140, 580))
        pygame.display.flip()
        winner = True
    elif game_grid[6] == game_grid[2] and game_grid[4] == game_grid[2]:
        # 6 - 4 - 2
        pygame.draw.rect(screen,button_win,(125,450,125,125))
        pygame.draw.rect(screen,button_win,(300,275,125,125))
        pygame.draw.rect(screen,button_win,(475,100,125,125))
        if game_grid[4] == "X":
            player_winner = "1"
            p1_score += 1
           
        else:
            player_winner = "2"
            p2_score += 1
        
        font = pygame.font.SysFont('Arial', 48)
        text1 = font.render(f"Player {player_winner} Wins!", True, (0, 0, 0))
        screen.blit(text1, (200, 25))
        reload_buttons()
        pygame.draw.rect(screen,button_color,(125,585,475,55))
        screen.blit(restart_text, (140, 580))
        pygame.display.flip()
        winner = True
    elif game_grid[0] != "0" and game_grid[1] != "1" and game_grid[2] != "2" and game_grid[3] != "3" and game_grid[4] != "4" and game_grid[5] != "5" and game_grid[6] != "6" and game_grid[7] != "7" and game_grid[8] != "8":
        text = font.render("No winner!!", True, (0, 0, 0))
        screen.blit(text, (200, 25))
        pygame.draw.rect(screen,button_color,(125,585,475,55))
        screen.blit(restart_text, (140, 580))
        pygame.display.flip()
        winner = True
    else:
        pass

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        if winner == False:
            if button1.collidepoint(pos):
                if game_grid[0] == "0":
                    
                    game_update(0, player_turn)
                            
            if button2.collidepoint(pos):
                if game_grid[1] == "1":
                    game_update(1, player_turn)
                    
            if button3.collidepoint(pos):
                if game_grid[2] == "2":
                    game_update(2, player_turn)
                
            if button4.collidepoint(pos):
                if game_grid[3] == "3":
                    game_update(3, player_turn)
                    
            if button5.collidepoint(pos):
                if game_grid[4] == "4":
                    game_update(4, player_turn)
                
            if button6.collidepoint(pos):
                if game_grid[5] == "5":
                    game_update(5, player_turn)
                
            if button7.collidepoint(pos):
                if game_grid[6] == "6":
                    game_update(6, player_turn)
            
            if button8.collidepoint(pos):
                if game_grid[7] == "7":
                        game_update(7, player_turn)

            if button9.collidepoint(pos):
                if game_grid[8] == "8":
                    game_update(8, player_turn)

        if button10.collidepoint(pos):
            if winner == True:
                new_game()
                print("Restart Button")
                