import pygame
import os
import time
import random
# Initialising the for for the score and level etc
pygame.font.init()

# Creating the window
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter Tutorial")  # Windows title

# Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Player player
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
# pygame.transform.scale to make the background the same size as the window
# We will set it to the window later
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


# Creating the laser class so each laser is independent to our ship
# So when we move our ship, the lasers don't move with them
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        # Creates the mask around the ship
        # So we know where its pixels are, so we can detect if something hits it
        self.mask = pygame.mask.from_surface(self.img)

    # Drawing the laser
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    # Moving the laser
    def move(self, vel):
        self.y += vel

    # Checking if the laser has moved off the screen
    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    # Checking if it has collided with another object
    def collision(self, obj):
        return collide(self, obj)


# Creating an abstract class which we will inherit from later
# The Enemy and player ship will inherit it
class Ship:
    COOLDOWN = 30  # How long until the ship can shoot a laser again

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        # We will set the images later in the individual classes
        self.ship_img = None
        self.laser_img = None
        self.lasers = []  # for storing the lasers
        # For measuring the time between how long until the ship can shoot a laser again
        self.cool_down_counter = 0

    def draw(self, window):
        # Draw the ship at the value of x and y
        window.blit(self.ship_img, (self.x, self.y))
        # Drawing all the lasers
        for laser in self.lasers:
            laser.draw(window)

    # For moving the laser
    def move_lasers(self, vel, obj):
        self.cooldown()  # Everytime, we move the laser call the countdown method
        for laser in self.lasers:
            # Move the laser by its vel
            laser.move(vel)
            # If it goes over the screen, remove it from the list
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            # if it has collided with another object, decrement the objects health, and remove the laser
            # Calls the collisions method we have created in the laser class
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    # For handling counting the cooldown counter
    def cooldown(self):
        # If the counter is equal to our limit, set it to 0
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            # Otherwise, increment the counter
            self.cool_down_counter += 1

    # For creating the laser when the ship shoots
    def shoot(self):
        if self.cool_down_counter == 0:  # If we're not in the process of counting down
            # How long until the ship can shoot again
            # Create the laser, add it to our list
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            # So we can't shoot again for a while
            self.cool_down_counter = 1

    # Methods for the ships width and height
    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


# Inherits from the Ship class
class Player(Ship):
    def __init__(self, x, y, health=100):
        # Calls the parent init method
        super().__init__(x, y, health)
        # Set the images
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        # Creates the mask around the ship
        # So we know where its pixels are, so we can detect if something hits it
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    # Overrides the move_laser method in the parent class
    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    # If the players laser has ht an enemy ship
                    if laser.collision(obj):
                        # Then remove the enemy
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    # Override the parent draw method
    def draw(self, window):
        # Call the parent draw method
        super().draw(window)
        # Drawing the health bar
        self.healthbar(window)

    # Creating the healthbar
    def healthbar(self, window):
        # Drawing the red bar
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        # Draw the green bar, which should be the same the max_health
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))


# Inherits from the Ship class
class Enemy(Ship):
    # A dictionary for the enemies color of ship and laser
    COLOR_MAP = {
                "red": (RED_SPACE_SHIP, RED_LASER),
                "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
                }

    def __init__(self, x, y, color, health=100):
        # Calls the parent init method
        super().__init__(x, y, health)
        # Set the images to the color passed in as parameter
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        # Creates the mask around the ship
        # So we know where its pixels are, so we can detect if something hits it
        self.mask = pygame.mask.from_surface(self.ship_img)

    # For moving the ship down, we'll pass in a parameter
    def move(self, vel):
        self.y += vel

    # Overrides it from our ship class
    # For shooting the laser
    def shoot(self):
        if self.cool_down_counter == 0:
            # self.x-20 So they shoot from the middle of the ship
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


# For checking if the two objects have collided
def collide(obj1, obj2):
    # Get the distance between the X and Y coordinates for object 1 and 2
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    # mask.overlap Tell you if the two objects masks overlap (collided)
    # Returns true if they do overlap, otherwise false
    # The offset is the difference of their X and Y coordinates
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


# main() handles all of our events
# Collisions, drawing things on the screen, moving character... etc
def main():
    run = True
    FPS = 60  # Frames per second, the speed of the game
    clock = pygame.time.Clock()  # For controlling the speed of the game

    level = 0
    lives = 5
    # Creating the fonts
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []  # It will store all the enemies
    wave_length = 5  # The number of enemies per wave
    enemy_vel = 1  # The speed at which the enemies move down

    # For how many pixels we want the players ship and the laser to move
    player_vel = 5
    laser_vel = 5

    player = Player(300, 630)

    # For checking if the user has lost the game
    lost = False
    lost_count = 0

    # Function for drawing the stufff on the screen
    # Its inside the main function, so it can only be called inside the main function
    def redraw_window():
        # Win is our variable for the window at the top
        # It draws the background we created at the top at position 0, 0
        WIN.blit(BG, (0, 0))

        # draw text
        # We pass in the text, 1 and the RGB color
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        # We draw the lives text at top left
        WIN.blit(lives_label, (10, 10))
        # We draw the level label at top right
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        # For drawing all the enemies
        # Ship class has a draw method and our enemy class inherits from it
        for enemy in enemies:
            enemy.draw(WIN)

        # Drawing the player
        player.draw(WIN)

        # If the user has lost the game
        if lost:
            # Create a lost label and show it in the window
            lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        # Refreshes the display
        pygame.display.update()

    while run:
        # Use our FPS variables as the speed of the game
        clock.tick(FPS)
        # Call the func to draw the window
        redraw_window()

        if lives <= 0 or player.health <= 0:
            # If the user has no lives or health left, set lost to true
            lost = True
            lost_count += 1  # Increment this

        # If the user has lost the game, show the lost_label for 3 seconds
        if lost:
            # if we have gone past our 3 sec timer
            if lost_count > FPS * 3:
                run = False  # Then stop the game
            else:
                continue  # Otherwise don't do anything

        # When there are no enemies left, increment the level
        # And create more enemies (5)
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            # Creating the enemies in random positions
            for i in range(wave_length):
                # We pass in X value, Y value and a random color from R, G or B
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                # Add the enemy to our list
                enemies.append(enemy)

        # Checking if an event has occurred
        # Event can be anything i.e. pressing a key / mouse button
        for event in pygame.event.get():
            # If the event is QUIT, then quit
            if event.type == pygame.QUIT:
                quit()

        # Gets all the keys and tells you if they're pressed or not
        keys = pygame.key.get_pressed()
        # and player.x - player_vel > 0 making sure they can't move off the screen
        if keys[pygame.K_a] and player.x - player_vel > 0:  # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:  # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:  # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT:  # down, + 15 to make # space for the healthbar
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            # If they press space, shoot the laser
            player.shoot()

        for enemy in enemies[:]:
            # For moving the enemy, we move it by enemy_vel
            enemy.move(enemy_vel)
            # And we move its laser by laser_vel
            # And we pass the player object to check if its hit the player
            enemy.move_lasers(laser_vel, player)

            # Making the enemies shoot within 2 seconds at random
            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            # If the player and the enemy collide, remove the enemy, and decrement the players health
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                # If the enemies gone over the screen, decrement a life
                # And remove it from the list
                lives -= 1
                enemies.remove(enemy)

        # Move the players laser by -laser_vel and check if has collided with the enemy ship
        player.move_lasers(-laser_vel, enemies)


# Creating the main menu screen
def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        WIN.blit(BG, (0,0))
        # Creating the text for the main menu text
        title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))  # Show it on the window
        pygame.display.update()
        for event in pygame.event.get():
            # If they press quit, stop the game
            if event.type == pygame.QUIT:
                run = False
            # If they press the mouse, call the main method (start the game)
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


main_menu()

