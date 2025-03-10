# Meteor Shower Game

## Overview

Meteor Shower Game is a simple yet engaging game where the player must dodge falling meteors. The meteors drop from the top of the screen at random times and increase in speed as the player's score increases. The game ends when a meteor collides with the player.

## Features

- Meteors of varying speed and positions fall from the top of the screen.
- The player can move left and right to avoid collisions.
- The speed of meteors increases as the game progresses.
- The game detects collisions and ends when the player is hit.
- The score increases with every meteor successfully dodged.

## Installation

1. Ensure you have Python installed on your system.
2. Install the required dependencies by running:
   ```bash
   pip install pygame
3. Download or clone this repository to your local machine.

## How to Play

1. Run the game using the following command:
   ```bash
   python meteor_shower.py
2. Use the left arrow key to move left and the right arrow key to move right.
3. Avoid the meteors as they fall.
4. Keep dodging to increase your score.
5. The game ends when a meteor collides with the player.

## Game Mechanics
- The meteors fall at a base speed of 2 initially.
- As the player's score increases, the meteor speed is adjusted logarithmically.
- Meteors are randomly placed and drop at varying intervals.
- The player's movement is restricted to the horizontal axis.

## Code Structure

- set_speed(score): Adjusts meteor speed based on the score.
- draw_meteors(met_list, met_dim, screen, color): Draws the meteors on the screen.
- drop_meteors(met_list, met_dim, width, score): Determines when and where meteors appear.
- update_meteor_positions(met_list, height, score, speed): Updates meteor positions and removes those that reach the bottom.
- detect_collision(player_pos, met_list, player_dim, met_dim): Detects if a collision occurs.
- collision_check(met_list, player_pos, player_dim, met_dim): Calls the collision detection function to determine if the game should end.
- main(): Runs the game loop, handles player input, updates meteors, and checks for collisions.

## Dependencies
- Python 3.x
- pygame



