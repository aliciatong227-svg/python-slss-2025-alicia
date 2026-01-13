# Collect Blocks
# Author:
# Date:

import random

import pygame

# COLOURS - (R, G, B)
# CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
GREY  = (128, 128, 128)

class Block(pygame.sprite.Sprite):
    def __init__(self):
        """A blue block"""
        super().__init__()

        self.image = pygame.Surface((20, 15))
        # change the colour of our image to blue
        self.image.fill(BLUE)

        # rect represents the hitbox of our sprite
        # the hitbox gives information about:
        #    - location of the sprite x, y
        #    - the size of the sprite width, height
        self.rect = self.image.get_rect()
        # change the location of our hitbox
        self.rect.centerx = 100
        self.rect.centery = 100

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        """Player sprite"""
        super().__init__()

        # Two copies of image: right-facing and left-facing
        self.image_right = pygame.image.load("assets/mario-snes.png")
        self.image_right = pygame.transform.scale_by(self.image_right, 0.5)
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image = self.image_right

        self.rect = self.image.get_rect()

        # Keep track of last x-coord
        self.last_x = 0

        # Mario's "Life"
        self.health = 100

    def decrease_health(self, mag: int) -> int:
        """Decrease player's health by magnitude.
        Returns:
            current health that Mario has after the change
        """
        self.health -= mag
        return self.health


    def update(self):
        """Have Mario follow the mouse.
        Set the "right" Mario image based on where he's facing."""
        self.rect.center = pygame.mouse.get_pos()

        # Mario faces right if and only if the previous x
        # is less than the current x
        if self.last_x < self.rect.x:
            self.image = self.image_right
        elif self.last_x > self.rect.x:
            self.image = self.image_left

        # Update the last_x
        self.last_x = self.rect.x

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        """Goomba"""
        super().__init__()

        self.image = pygame.image.load("assets/goomba-nes.png")
        self.rect = self.image.get_rect()
        # No initial location -> (0, 0)

        # Velocity of the Enemy
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        # movement in the x- and y-axis
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        # TODO: randomize movement

def game():
    pygame.init()

    # CONSTANTS
    WIDTH = 800
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Collect Blocks")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # Create a sprite group
    all_sprites_group = pygame.sprite.Group()
    block_sprites_group = pygame.sprite.Group()
    enemy_sprites_group = pygame.sprite.Group()

    # Create player sprite
    player = Mario()
    # Place Mario in the middle of the screen
    player.rect.centerx = WIDTH / 2
    player.rect.centery = HEIGHT / 2
    all_sprites_group.add(player)

    # TODO: Check collision with Enemies
    # Create 3 enemies to start
    for _ in range(3):
        enemy_one = Enemy()
        # Randomize position at bottom-left
        random_x = random.randrange(20, 100)
        random_y = random.randrange(HEIGHT-100, HEIGHT-20)
        enemy_one.rect.center = random_x, random_y
        # Randomize velocity
        enemy_one.vel_x = random.choice([-3, -2, -1, 1, 2, 3])
        enemy_one.vel_y = random.choice([-3, -2, -1, 1, 2, 3])

        all_sprites_group.add(enemy_one)
        enemy_sprites_group.add(enemy_one)

    # Create 100 blocks
    blocks = 0
    for _ in range(100):
        block = Block()
        # randomize their location
        block.rect.centerx = random.randrange(10, WIDTH-10)
        block.rect.centery = random.randrange(10, HEIGHT-10)
        # add them to the sprite group
        all_sprites_group.add(block)
        block_sprites_group.add(block)
        blocks += 1


    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC
        all_sprites_group.update()

        # Keep the enemies inside the screen
        for enemy in enemy_sprites_group:
            # x-axis and y-axis bounce
            if enemy.rect.left < 0 or enemy.rect.right > WIDTH:
                enemy.vel_x = -enemy.vel_x
            if enemy.rect.top < 0 or enemy.rect.bottom > HEIGHT:
                enemy.vel_y = -enemy.vel_y

        # Check if Mario collides with a block
        blocks_collided = pygame.sprite.spritecollide(player, block_sprites_group, True)
        if blocks_collided:
           print("----")
           print("Mario has collided with a block!")
           print(blocks_collided)
           blocks -= 1
           print(blocks)

        # TODO: Mario collides with enemy
        enemies_collided = pygame.sprite.spritecollide(player, enemy_sprites_group, False)
        for enemy in enemies_collided:
            # Decrease Mario's life by some number
            print(player.decrease_health(1))
            if player.health < 0:
                all_sprites_group.remove(player)

        if blocks == 0:
           print("gameover")


        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)

        # Draw all the sprites
        all_sprites_group.draw(screen)

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60) # 60 fps

    pygame.quit()

if __name__ == "__main__":
    game()
