import pygame
import random

# initialize Pygame
pygame.init()

# create the window
window = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Avoid the Obstacles")

# create the player character and set its starting position
player_image = pygame.Surface((50, 50))
player_image.fill((255, 0, 0))
player_rect = player_image.get_rect()
player_rect.center = (200, 250)

# create a list to store the obstacles
obstacles = []

# game loop
running = True
clock = pygame.time.Clock()
spawn_timer = 0
spawn_interval = 1000  # time in milliseconds between spawning obstacles
num_obstacles = 1  # added number of obstacles
max_obstacles = 10  # added maximum number of obstacles
increase_timer = 0  # added timer for increasing number of obstacles
game_timer = 0  # added timer for measuring the duration of the game
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # move the player based on user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
    
    # update player position to keep it within the window
    player_rect.clamp_ip(window.get_rect())
    
    # check for collisions between the player and the obstacles
    for obstacle_rect in obstacles:
        if player_rect.colliderect(obstacle_rect):
            running = False
    
    # update the obstacle positions
    for obstacle_rect in obstacles:
        obstacle_rect.top += 5
    
    # spawn a new obstacle every spawn_interval milliseconds
    spawn_timer += clock.get_time()
    if spawn_timer >= spawn_interval:
        spawn_timer = 0
        obstacle_image = pygame.Surface((25, 25))
        obstacle_image.fill((0, 255, 0))
        obstacle_rect = obstacle_image.get_rect(top=0, left=random.randint(0, 375))
        obstacles.append(obstacle_rect)
    
    # increase the number of obstacles every 10 seconds
    increase_timer += clock.get_time()
    if increase_timer >= 10000:
        increase_timer = 0
        if num_obstacles < max_obstacles:
            num_obstacles += 1
            spawn_interval /= 2  # reduce the spawn interval
    
    # update the game timer
    game_timer += clock.get_time()
    
    # redraw the window
    window.fill((255, 255, 255))
    window.blit(player_image, player_rect)
    for obstacle_rect in obstacles:
        window.blit(obstacle_image, obstacle_rect)
    
    pygame.display.update()
    clock.tick(60)

# quit Pygame
