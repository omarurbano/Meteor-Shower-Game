# Meteor Shower Game
# This program allows the user to create and then store a nested list creating a meteor shower game. this game drops meteors and detects for collisions 
# Within this program meteors have been drawn of a size and color, they also have a set speed which progresses during the duration of the game.
# The meteors are placed at the top of the game screen and fall at random times. Each meteor that hits the bottom is removed from the nested list.
# The user must dodge the meteors as they come down and continue if they don't get hit. Once a hit is detected,
# the game ends.


# Import modules
import pygame as pyg
from random import *
import math as m

# Define functions
def set_speed(score):
    '''
    Takes integer 'score' from main() function and runs a conditional check. If
    score is less than for (initial state) then speed is default of 2. Else score 
    is greater than 4 speed is calculated based off a logrithmic function to gradually
    increase speed based on the score. Returns integer 'speed' to main() function.
    '''
    if score < 4:                           # Determines base speed for initial game start
        speed = 2
    else:
        speed = m.log(score ** 5, 10)       # Increments speed consistantly as game progresses based on score
    return speed                            # returns speed to main()


def draw_meteors(met_list, met_dim, screen, color):
    '''
    Takes met_list, met_dim, screen, and color as parameters from main() function. Runs an itterating
    for loop with all meteors in met_list creating them on the screen using the pygame.draw.rectangle
    process.
    '''
    for i in met_list:                      # Each meteor instance on the met_list
        pyg.draw.rect(screen, color ,pyg.Rect(i[0], i[1], met_dim, met_dim))       # Actual meteor displayed
    return
    

def drop_meteors(met_list, met_dim, width, score):
    '''
    Takes parameters list (met_list), integer (met_dim), and integer (screen width) to generate initial
    placement of meteors on screen. While the game is active generates a random number between 1 and 24 and
    places a meteor when a 1 is generated. It then runs a nested conditional where, if a 1 is generated, the
    function will determine a random x value for the meteor to be generated on the screen so the dimension
    does not extend beond the screen width. If x is even then it is used to generate a new meteor in the list
    met_list. If not even then function continues and returns to main(). If drop did not equal 1 then it also
    returns to main(). Additionally pulled score from main() so it could be used to influence drop rate at 
    higher scores.
    '''

    while True:
        drop_rate = ((score // 10) * 2)     # establishes rate at which meteors drop is adjusted
        if drop_rate >= 24:                 # conditional to determine if drop_rate exceeds 24
            drop_rate = 24                  # limits how high drop_rate can increase
        drop = randint(1, (25 - drop_rate)) # Generates random number to determine if meteor is dropped, decrease by drop_rate, min value 1
        if drop == 1:                       # only drops meteor when drop value == 1
            x = randrange(0, width, met_dim)        # sets random x value on screen for initial drop
            if x % 2 == 0:                  # checks to see if number is even
                met_list.append([x,0])      # Adds meteor position to met_list
            else:
                continue                    # continues program if number was odd
            return
        else:                               # returns to program if drop != 1
            return


def update_meteor_positions(met_list, height, score, speed):
    '''
    This function increases the y coordinate of the meteor by speed. If the meteor
    passes height, then score is increased by 1 and gets appended to list1. Met_list
    is then updated by assigning it to list1, therefore, removing the meteor. Returns
    the updated meteor list and score.
    '''

    list1 = []                      # initalizes empty list as temp list for use in update met_list
    for i in range(len(met_list)):  # begins counting for-loop based on number of meteors in met_list
        met_list[i][1] += speed     # adds speed to y value thus increasing speed of meteors in met_list
        if met_list[i][1] >= height:    # checks to see if y value of meteor is at or exceeds height limit, aka 'hit ground'
            score +=1               # adds one point to score if meteor 'hit ground'
        else:
            list1.append(met_list[i])   # if meteor hasn't 'hit ground' then adds to temp list

    met_list = list1                # sets temp list to met_list so only 'active' meteors remain in met_list

    return score, met_list          # returns score and updated met_list to main()


def detect_collision(player_pos, met_list, player_dim, met_dim):
    '''
    This function detects if there has been a collision with the player. It checks every 
    meteor in met_list to see if it did not collide horizontally or vertically. When a collision is
    detected, it returns True. If no collision is detected, it will return False and the game
    continues. 
    '''

    for i in range(len(met_list)):
        meteor = met_list[i][0]                 # Assigns meteor with coordinate points in met_list
        meteor_right = met_list[i][0] + met_dim #This takes into account the dimension of the meteor horizontally
        player = player_pos[0]                  #Assigns player with  player coordinate points
        player_right = player_pos[0] + player_dim #This takes into account the dimension of the player horizontally
        meteor_top = met_list[i][1]             #Assigns meteor_top with the top of the meteor
        meteor_bottom = met_list[i][1] + met_dim #This takes into account the dimension of the metoer to determine the bottom
        player_top = player_pos[1]              #Assigns players_top to the players top
        player_bottom = player_pos[1] + player_dim #This takes into account the dimension of the player to determine players bottom
        
        if (meteor <= player_right and meteor >= player) or (meteor_right <= player_right and meteor_right >= player):#horizontal collision

            if (meteor_top <= player_bottom and meteor_top >= player_top) or (meteor_bottom <= player_bottom and meteor_bottom >= player_top):#vertical collision 
                return True
    return False


def collision_check(met_list, player_pos, player_dim, met_dim):
    '''
    This function calls the detect_collision function and checks to see if it returns
    True. If it does, then it also returns True and the game ends. If True is not detected,
    then False is returned.
    '''
    if detect_collision(player_pos, met_list, player_dim, met_dim) == True:
        return True
    else:
        return False

    
def main():
    '''
    Initialize pygame and pygame parameters.  Note that both player and meteors
    are square.  Thus, player_dim and met_dim are the height and width of the
    player and meteors, respectively.  Each line of code is commented.
    '''
    pyg.init()                # initialize pygame

    width = 800               # set width of game screen in pixels
    height = 600              # set height of game screen in pixels

    red = (255,0,0)           # rgb color of player
    yellow = (244,208,63)     # rgb color of meteors
    background = (0,0,156)    # rgb color of sky (midnight blue)

    player_dim = 50           # player size in pixels
    player_pos = [int(width/2), int(height-2*player_dim)]  # initial location of player
                                                 # at bottom middle; height
                                                 # never changes

    met_dim = 20              # meteor size in pixels
    met_list = []             # initialize list of two-element lists
                              # giving x and y meteor positions

    screen = pyg.display.set_mode((width, height)) # initialize game screen

    game_over = False         # initialize game_over; game played until
                              # game_over is True, i.e., when collision
                              # is detected

    score = 0                 # initialize score

    clock = pyg.time.Clock()  # initialize clock to track time

    my_font = pyg.font.SysFont("monospace", 35) # initialize system font

    while not game_over:                       # play until game_over == True
        for event in pyg.event.get():          # loop through events in queue
            if event.type == pyg.KEYDOWN:      # checks for key press
                x = player_pos[0]              # assign current x position
                y = player_pos[1]              # assign current y position
                if event.key == pyg.K_LEFT:    # checks if left arrow;
                    x -= player_dim            # if true, moves player left
                elif event.key == pyg.K_RIGHT: # checks if right arrow;
                    x += player_dim            # else moves player right
                player_pos = [x, y]            # reset player position
            
        screen.fill(background)                # refresh screen bg color
        drop_meteors(met_list, met_dim, width, score) # call drop_meteors function to drop meteors 
        # added speed to drop_meteor() argument so that drop_rate increases based on score 
        speed = set_speed(score)               # call set_speed function to increase speed of meteors as score increases
        score, met_list = update_meteor_positions(met_list, height, score, speed)
                                               # call the update_meteor_position function and returns score and updated list
        text = "Score: " + str(score)              # create score text
        label = my_font.render(text, 1, yellow)    # render text into label
        screen.blit(label, (width-250, height-40)) # blit label to screen at
                                                   # given position; for our 
                                                   # purposes, just think of
                                                   # blit to mean draw
        draw_meteors(met_list, met_dim, screen, yellow) # self-explanatory;
                                                        # call the draw_meteor function

        pyg.draw.rect(screen, red, (player_pos[0], player_pos[1], player_dim, player_dim))  # draw player

        if collision_check(met_list, player_pos, player_dim, met_dim):
            game_over = True                       # ends the game
    
        clock.tick(30)                             # set frame rate to control
                                                   # frames per second (~30); 
                                                   # slows down game

        pyg.display.update()                       # update screen characters
    # Outside while-loop now.
    print('Final score:', score)                   # final score
    pyg.quit()                                     # leave pygame

main()
