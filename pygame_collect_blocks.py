# Your Title Here
# Author:
# Date:

import random
import sys
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
        # Change the colour of the image to blue
        self.image.fill(BLUE)

        # rect represents the hitbox of our sprite
        # the hit box gives info about:
            # the location of the sprite - x,y
            # the size of the sprite - width,height
        self.rect = self.image.get_rect()
        # change the location of the hitbox
        self.rect.centerx = 100
        self.rect_centery = 100

        self.point_value = 1

    def level_up(self,val:int):
        """increase point value"""
        self.point_value *= val


class MoveBlock(pygame.sprite.Sprite):
    """Moving block"""
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((20,15))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        # movement in the x-axis
        self.rect.x += self.vel_x
        # movement in the y-axis
        self.rect.y += self.vel_y
        # randomize movement
        # self.last_x = self.rect.x




class Coin(pygame.sprite.Sprite):
    """Coin dropper"""

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/coins.png")
        self.image = pygame.transform.scale_by(self.image, 0.1)
        self.rect = self.image.get_rect()

        self.vel_x = 0
        self.vel_y = 0


        # def collect_moving(self, amt: int):
        #     self.moving_collected += amt

    def update(self):
          # movement in the x-axis
          self.rect.x += self.vel_x
          # movement in the y-axis
          self.rect.y += self.vel_y
          # randomize movement




class Mario(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/mario-snes.png")
        self.image = pygame.transform.scale_by(self.image, 0.5)
        # make two copies of the
        self.image_right = pygame.image.load("assets/mario-snes.png")
        self.image_right = pygame.transform.scale_by(self.image_right, 0.5)
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image = self.image_right

        self.rect = self.image.get_rect()
        # keep track of last x coord
        self.last_x = 0
        # Mario's life
        self.health = 100
        self.points = 0
        self.coins_collected = 0

    def decrease_health(self, mag: int) -> float:
        self.health -= mag
        return self.health

    def increase_score(self, amt: int):
        self += amt

    def collect_coins(self, amt: int):
        self.coins_collected += amt

    # def collect_moving(self, amt: int):
    #     self.moving_collected += amt

    def show_health_percentage(self) -> float:
        return self.health / 100

    def move_block(self, amt:int):
        self.collected_blocks += amt


    def update(self):
        """Have Mario follow the mouse"""
        """Set the 'right' Mario image based on where he's facing."""
        self.rect.center = pygame.mouse.get_pos()
        if self.last_x < self.rect.x:
            self.image = self.image_right
        elif self.last_x > self.rect.x:
            self.image = self.image_left

        # update the last_x
        self.last_x = self.rect.x


class Enemy(pygame.sprite.Sprite):
    # Enemy class
    def __init__(self):
        """Goomba"""
        super().__init__()

        self.image = pygame.image.load("assets/goomba-nes.png")
        self.rect = self.image.get_rect()
        # no initial location -> 0,0

        # velocity of enemy
        self.vel_x = 0
        self.vel_y = 0

        self.damage = 1
    def level_up(self):
        # increase damage
        self.damage *= 2

    def update(self):
          # movement in the x-axis
          self.rect.x += self.vel_x
          # movement in the y-axis
          self.rect.y += self.vel_y
          # randomize movement

class HealthBar(pygame.Surface):
    def __init__(self):
        super().__init__((300,10))
        self.fill(RED)

    def set_health(self, percentage: float):
        self.fill(RED)
        pygame.draw.rect(self, GREEN, (0,0, (300 * percentage), 10))

def game():
    pygame.init()

    # CONSTANTS
    WIDTH = 1920
    HEIGHT = 1080
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Collect Blocks")
    pygame.mouse.set_visible(False)

    # Variables
    done = False
    clock = pygame.time.Clock()
    num_enemies = 3
    num_blocks = 50
    num_blocks_2 = 2
    healthbar = HealthBar()
    level = 1
    coins = 5
    move_block = 3
    font = pygame.font.SysFont("Arial", 30)

    block_one = Block()
    block_one.rect.centerx = WIDTH / 2

    # create a sprite group
    all_sprites_group = pygame.sprite.Group()
    # add block_one to the all_sprites_group
    block_sprite_group = pygame.sprite.Group()
    enemy_sprites_group = pygame.sprite.Group()
    move_sprite_group = pygame.sprite.Group()
    coin_sprites_group = pygame.sprite.Group()
    # create a player sprite
    player = Mario()
    # place Mario in the middle of the screen
    player.rect.centerx = WIDTH / 2
    player.rect.centery = HEIGHT / 2
    # add Mario to the all_sprites)group
    all_sprites_group.add(player)

    # create enemy sprite
    for _ in range(num_enemies):
        enemy_one = Enemy()
        # randomize the position at bottom left
        random_x = random.randrange(20, 100)
        random_y = random.randrange(HEIGHT - 120, HEIGHT - 20)
        enemy_one.rect.center = random_x, random_y
        # move the enemy
        enemy_one.vel_x = random.choice([-3, -2, -1, 1, 2, 3])
        enemy_one.vel_y = random.choice([-3, -2, -1, 1, 2, 3])
        all_sprites_group.add(enemy_one)
        enemy_sprites_group.add(enemy_one)


    # create 100 blocks
    # randomize their location
    # add them to the sprite group
    for _ in range(num_blocks):
        block = Block()
        # randomize their location
        block.rect.centerx = random.randrange(0,WIDTH)
        block.rect.centery = random.randrange(0, HEIGHT)
        # add them to the sprites group
        all_sprites_group.add(block)
        block_sprite_group.add(block)


    for _ in range(num_blocks_2):
        move_block = MoveBlock()
        # randomize the position at bottom left
        move_block.rect.centerx = random.randrange(0,WIDTH)
        move_block.rect.centery = random.randrange(500, HEIGHT)
        # move the block
        move_block.vel_x = random.choice([-3, -2, -1, 1, 2, 3])
        move_block.vel_y = random.choice([-3, -2, -1, 1, 2, 3])
        # add to group
        all_sprites_group.add(move_block)
        move_sprite_group.add(move_block)

    # todo: wait 3 seconds before spawning again

    for _ in range(coins):
        coin_one = Coin()
        # wait 3 seconds before spawning again
        # initial position
        random_x = random.choice([100,200,300,400,500])
        random_y = HEIGHT
        # make coins drop

        coin_one.vel_y = random.choice([1, 2, 2, 3, 3, 3])
        all_sprites_group.add(coin_one)
        coin_sprites_group.add(coin_one)

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC
        all_sprites_group.update()
        healthbar.set_health(player.show_health_percentage())

        # keep enemies inside the screen
        # iterate through all the enemies in enemy group
        for enemy in enemy_sprites_group:
        # x-axis bounce
            if enemy.rect.left < 0 or enemy.rect.right > WIDTH:
                enemy.vel_x = -enemy.vel_x   # set the velocity to negative
        # y axis bounce
        for enemy in enemy_sprites_group:
            if enemy.rect.top < 0 or enemy.rect.bottom > HEIGHT:
                enemy.vel_y = -enemy.vel_y

        for move_block in move_sprite_group:
            if move_block.rect.left < 0 or move_block.rect.right > WIDTH:
                move_block.vel_x = -move_block.vel_x
        for move_block in move_sprite_group:
            if move_block.rect.top < 0 or move_block.rect.bottom > HEIGHT:
                move_block.vel_y = -move_block.vel_y


        # If Mario collides with a block, print out "Mario has collided with a block"
        blocks_collided = pygame.sprite.spritecollide(player, block_sprite_group, True)
        if blocks_collided:
            print("------")
            print("Mario has collided with a block")
            print(blocks_collided)

        blocks_collided = pygame.sprite.spritecollide(player, move_sprite_group, True)
        if blocks_collided:
            print("------")
            print("Moving Block Collected!")
            print(blocks_collided)


        # If Mario collides with a coin, increase the coins_collected property
        coins_collided = pygame.sprite.spritecollide(player, coin_sprites_group, True)
        for coin in coins_collided:
            player.collect_coins(1)
            print(player.coins_collected)

        # Mario collides with enemy
        enemies_collided = pygame.sprite.spritecollide(player, enemy_sprites_group, False)
        for enemy in enemies_collided:
            # decrease Mario's life by a number
            player.decrease_health(enemy.damage)

            if not block_sprite_group:
                level += 1

                for _ in range(num_blocks):
                    block = Block()
                    block.rect.center = random.randrange(0,WIDTH), random.randrange(0,HEIGHT)

                    block.level_up(level)
                    all_sprites_group.add(block)
                    block_sprite_group.add(block)

                enemy = Enemy()
                enemy.vel_x, enemy.vel_y = random.choice ([-5, -3, -1, 1, 3, 5]), random.choice([-5, -3, -1, 1, 3, 5])
                enemy.rect.center = (WIDTH/2, HEIGHT/2)
                all_sprites_group.add(enemy)
                enemy_sprites_group.add(enemy)



                for enemy in enemy_sprites_group:
                    enemy.level_up()

        if player.health <= 0:
            done = True


        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)

        # draw all the sprites
        all_sprites_group.draw(screen)
        screen.blit(healthbar, (5,5))
        coins_text = font.render(f"Coins: {player.coins_collected}", True, BLACK)
        screen.blit(coins_text, (WIDTH - 200, 5))
        blocks_text = font.render(f"Blocks: {blocks_collided}", True, BLACK)
        screen.blit(blocks_text, (WIDTH - 200, 38))

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60) # 60 fps
        if block_sprite_group == 0:
            sys.exit

    pygame.quit()

if __name__ == "__main__":
    game()
