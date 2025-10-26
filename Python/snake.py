import pygame
import random

pygame.init()

#display
s_width = 800
s_height = 600

gameWindow = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Snake Game With Rohan")



def gameloop():

  greenl = (30,60,15)
  red = (255,0,0) 
  green = (0,255,0)
  black = (0, 0, 0)
  white = (255,255,255, 0.7)
  blue = (0, 0, 200)


  #snake  position
  snake_x = 45
  snake_y = 55
  size = 10
  tail = 10

  #clock fps
  clock = pygame.time.Clock()
  fps = 60
  #velocity of snake
  velocity_x = 0
  velocity_y = 0
  velocity = 4

  #food
  food_x = random.randint(0, 780)
  food_y = random.randint(0, 380)
  snk_list = []
  snk_length = 1
  food_size = 10

  

  score = 0
  exit_game = False
  game_over = False


  font = pygame.font.SysFont(None, 25)
  def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

  def ploat_snake(gameWindow, color, snk_list, size):
    for x,y in snk_list:
      pygame.draw.rect(gameWindow, color, [x, y, size, size])



  while not exit_game:
    
    if game_over:
      gameWindow.fill(white)
      text_screen("Game over! Enter to continue:", blue, 280, 150)
      text_screen("Press Backspace for Exit.", red, 280, 190)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          exit_game = True
          

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
            gameloop()
          
          if event.key == pygame.K_BACKSPACE:
            exit_game= True

    else:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          exit_game = True
          

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            velocity_x = velocity
            velocity_y = 0

          if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            velocity_x = -velocity
            velocity_y = 0

          if event.key == pygame.K_UP or event.key == pygame.K_w:
            velocity_y = -velocity
            velocity_x = 0

          if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            velocity_y = velocity
            velocity_x = 0

          if event.key == pygame.K_1:
            velocity = 1
          if event.key == pygame.K_2:
            velocity = 2
          if event.key == pygame.K_3:
            velocity = 3
          if event.key == pygame.K_4:
            velocity = 4
          if event.key == pygame.K_5:
            velocity = 5
          if event.key == pygame.K_6:
            velocity = 6
          if event.key == pygame.K_7:
            velocity = 7
          if event.key == pygame.K_8:
            velocity = 8
          if event.key == pygame.K_9:
            velocity = 9
          if event.key == pygame.K_0:
            velocity = 10
          

      snake_x += velocity_x
      snake_y += velocity_y

      if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
        score += 1
        food_x = random.randint(20, 780)
        food_y = random.randint(20, 380)
        snk_length += 5
     
      
        

    #coliding the snake
      if snake_x > s_width:
        snake_x = 1
        # exit_game = True
        # game_over = True
      if snake_x < 1:
        snake_x = s_width
      if snake_y > s_height:
        snake_y = 1
      if snake_y < 1:
        snake_y = s_height
      

      head = []
      head.append(snake_x)
      head.append(snake_y)
      snk_list.append(head)

      if len(snk_list)> snk_length:
        del snk_list[0]

      if head in snk_list[:-1]:
        game_over = True
      gameWindow.fill(white)
      text_screen("Score: "+ str(score * 10), greenl, 5, 5)
      # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, tail, size])
      ploat_snake(gameWindow, black, snk_list, size)
      pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])

    
    pygame.display.update()
    clock.tick(fps)

  pygame.quit()
  quit()
gameloop()