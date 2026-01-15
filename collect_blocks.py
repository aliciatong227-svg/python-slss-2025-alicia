# Collect Blocks
# Author:
# Date:

import random
import time
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
        """The player"""
        super().__init__()

        # Right version of Mario and Left version
        self.image_right =  pygame.image.load("assets/mario-snes.png")
        self.image_right = pygame.transform.scale_by(self.image_right, 0.5)
        self.image_left = pygame.transform.flip(self.image_right, True, False)

        self.image = self.image_right
        self.rect = self.image.get_rect()

        self.previous_x = 0               # help with direction
        self.health = 100
        self.points = 0

    def calc_damage(self, amt: int) -> int:
        """Decrease player health by amt
        Returns:
            Remaining health"""
        self.health -= amt
        return self.health

    def incr_score(self, amt: int) -> int:
        """Increases player score by amt
        Returns:
            Score"""
        self.points += amt
        return self.points

    def get_damage_percentage(self) -> float:
        return self.health / 100

    def update(self):
        """Update Mario's location based on the mouse pos
        Update Mario's image based on where he's going"""
        self.rect.center = pygame.mouse.get_pos()

        # If Mario's previous x less than current x
        #   Then Mario is facing Right
        # If Mario's previous x is greater than current x
        #   Then Mario is facing Left
        if self.previous_x < self.rect.x:
            self.image = self.image_right
        elif self.previous_x > self.rect.x:
            self.image = self.image_left

        self.previous_x = self.rect.x


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/goomba-nes.png")
        self.rect = self.image.get_rect()

        self.vel_x = 0
        self.vel_y = 0

        self.damage = 1

    def update(self):
        # movement in the x- and y-axis
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def level_up(self):
        # increase damage
        self.damage *= 2

class Safe_Pack(pygame.sprite.Sprite):
    def __init__(self):
         super().__init__()
         self.image_right = pygame.image.load("assets/vector-illustration-first-aid-kit-260nw-2499481599.webp")
         self.image_right = pygame.transform.scale_by(self.image_right, 0.1)
         self.image = self.image_right
         self.rect = self.image.get_rect()
         self.health = 10

class HealthBar(pygame.Surface):
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        super().__init__((width, height))

        self.fill(RED)

    def update_info(self, percentage: float):
        """Updates the healthbar with the given percentage"""
        self.fill(RED)
        pygame.draw.rect(self, GREEN, (0, 0, percentage * self._width, self._height))

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
    health_bar = HealthBar(200, 10)
    num_enemies = 7
    num_blocks = 100
    num_safe = 5

    # Create a sprite group
    all_sprites_group = pygame.sprite.Group()
    block_sprites_group = pygame.sprite.Group()
    enemy_sprites_group = pygame.sprite.Group()
    safe_sprite_group = pygame.sprite.Group()

    # Create player sprite
    player = Mario()
    # Place Mario in the middle of the screen
    player.rect.centerx = WIDTH / 2
    player.rect.centery = HEIGHT / 2
    all_sprites_group.add(player)

    # TODO: Check collision with Enemies
    # Create 3 enemies to start
    for _ in range(num_enemies):
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

    for _ in range(num_blocks):
        block = Block()
        # randomize their location
        block.rect.centerx = random.randrange(0, WIDTH-10)
        block.rect.centery = random.randrange(0, HEIGHT-10)
        # add them to the sprite group
        all_sprites_group.add(block)
        block_sprites_group.add(block)

    for _ in range(num_safe):
         safe = Safe_Pack()
         # randomize their location
         safe.rect.centerx = random.randrange(0, WIDTH-10)
         safe.rect.centery = random.randrange(0, HEIGHT-10)
         # add them to the sprite group
         all_sprites_group.add(safe)
         safe_sprite_group.add(safe)


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
           num_blocks -= 1
           print(num_blocks)

        safe_collided = pygame.sprite.spritecollide(player, safe_sprite_group, False)
        if safe_collided and player.health < 80:
            pygame.sprite.spritecollide(player, safe_sprite_group, True)
            player.calc_damage(-20)
            print("----")
            print("Mario regaining health!")
            print(player.health)
            num_safe -= 1
            if num_safe <=0:
                print("NO MORE SAFE PACKS LEFTTT!!!!!!")

        # TODO: Mario collides with enemy
        enemies_collided = pygame.sprite.spritecollide(player, enemy_sprites_group, False)
        for enemy in enemies_collided:
            # Decrease Mario's life by some number
            player.calc_damage(enemy.damage)
        if player.health < 0:
            done = True

        if num_blocks <= 20:
           print("You pass")
           time.sleep(5)
           done = True


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
