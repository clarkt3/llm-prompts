# Using an LLM (GPT4) to generate and modify  a Snake Game 

## Prompt 1 - Priming the LLM

    # fed the following prompt to GPT4o in a new chat window to get it 'warmed up'
    # changing to new chat ensure that previous information doesn't influence new prompt output

    Input: Prompt 1: I want to creat a a Snake Game using Python. What steps would I need to do that?

    Output: GPT4o

    Creating a Snake Game using Python is a fun project that will help you learn more about programming concepts, game development, and Python libraries. Here's a step-by-step guide to help you get started:

### Step 1: Set Up Your Environment
1. **Install Python**: Make sure you have Python installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Install Pygame**: Pygame is a popular library for making games in Python. You can install it using pip:
   ```bash
   pip install pygame
   ```

### Step 2: Plan Your Game
1. **Game Logic**: Plan out the basic logic of your game:
   - The snake moves continuously in a specific direction.
   - The player can control the direction of the snake using the arrow keys.
   - The snake grows when it eats food.
   - The game ends when the snake collides with itself or the walls.

2. **Game Elements**:
   - **Snake**: A list of segments (each segment can be represented as a block).
   - **Food**: A single block that appears randomly on the screen.
   - **Score**: Tracks the number of food items eaten by the snake.

### Step 3: Create the Game Window
1. **Initialize Pygame**: Set up your game window and initialize Pygame.
   ```python
   import pygame

   # Initialize Pygame
   pygame.init()

   # Set the dimensions of the window
   window_width = 800
   window_height = 600

   # Create the game window
   window = pygame.display.set_mode((window_width, window_height))
   ```

2. **Set Up the Game Loop**: Create a loop that will run the game continuously until the player quits.
   ```python
   running = True
   while running:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
   ```

### Step 4: Create the Snake and Food
1. **Create the Snake**: Represent the snake as a list of coordinates.
   ```python
   snake_pos = [100, 50]
   snake_body = [[100, 50], [90, 50], [80, 50]]
   snake_direction = 'RIGHT'
   change_to = snake_direction
   ```

2. **Create the Food**: Randomly place food on the screen.
   ```python
   import random

   food_pos = [random.randrange(1, (window_width // 10)) * 10,
               random.randrange(1, (window_height // 10)) * 10]
   food_spawn = True
   ```

### Step 5: Implement Game Logic
1. **Control the Snake**: Allow the player to control the snake’s direction using the arrow keys.
   ```python
   for event in pygame.event.get():
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_UP:
               change_to = 'UP'
           elif event.key == pygame.K_DOWN:
               change_to = 'DOWN'
           elif event.key == pygame.K_LEFT:
               change_to = 'LEFT'
           elif event.key == pygame.K_RIGHT:
               change_to = 'RIGHT'

   # Make sure the snake cannot move in the opposite direction
   if change_to == 'UP' and not snake_direction == 'DOWN':
       snake_direction = 'UP'
   if change_to == 'DOWN' and not snake_direction == 'UP':
       snake_direction = 'DOWN'
   if change_to == 'LEFT' and not snake_direction == 'RIGHT':
       snake_direction = 'LEFT'
   if change_to == 'RIGHT' and not snake_direction == 'LEFT':
       snake_direction = 'RIGHT'
   ```

2. **Move the Snake**: Update the position of the snake based on the direction.
   ```python
   if snake_direction == 'UP':
       snake_pos[1] -= 10
   if snake_direction == 'DOWN':
       snake_pos[1] += 10
   if snake_direction == 'LEFT':
       snake_pos[0] -= 10
   if snake_direction == 'RIGHT':
       snake_pos[0] += 10

   # Snake body growing mechanism
   snake_body.insert(0, list(snake_pos))
   if snake_pos == food_pos:
       score += 10
       food_spawn = False
   else:
       snake_body.pop()

   if not food_spawn:
       food_pos = [random.randrange(1, (window_width // 10)) * 10,
                   random.randrange(1, (window_height // 10)) * 10]

   food_spawn = True
   ```

3. **Check for Collisions**: Determine when the game should end.
   ```python
   # Game Over conditions
   if snake_pos[0] < 0 or snake_pos[0] > window_width-10:
       running = False
   if snake_pos[1] < 0 or snake_pos[1] > window_height-10:
       running = False

   # Check if the snake hits itself
   for block in snake_body[1:]:
       if snake_pos == block:
           running = False
   ```

### Step 6: Display the Game
1. **Render the Game Elements**: Draw the snake and food on the screen.
   ```python
   window.fill(pygame.Color('black'))

   for pos in snake_body:
       pygame.draw.rect(window, pygame.Color('green'), pygame.Rect(pos[0], pos[1], 10, 10))

   pygame.draw.rect(window, pygame.Color('red'), pygame.Rect(food_pos[0], food_pos[1], 10, 10))

   # Refresh the game screen
   pygame.display.update()

   # Frame Per Second /Refresh Rate
   fps = pygame.time.Clock()
   fps.tick(25)
   ```

### Step 7: Add Scoring and Game Over Screen
1. **Display Score**: Keep track of and display the player’s score.
   ```python
   def show_score(choice=1):
       score_font = pygame.font.SysFont('times new roman', 20)
       score_surface = score_font.render('Score : ' + str(score), True, pygame.Color('white'))
       score_rect = score_surface.get_rect()
       if choice == 1:
           score_rect.midtop = (window_width / 10, 15)
       else:
           score_rect.midtop = (window_width / 2, window_height / 1.25)
       window.blit(score_surface, score_rect)

   # Call this function in the game loop
   show_score()
   ```

2. **Game Over Function**: Display a message when the game ends.
   ```python
   def game_over():
       my_font = pygame.font.SysFont('times new roman', 50)
       game_over_surface = my_font.render('Your Score is : ' + str(score), True, pygame.Color('red'))
       game_over_rect = game_over_surface.get_rect()
       game_over_rect.midtop = (window_width / 2, window_height / 4)
       window.blit(game_over_surface, game_over_rect)
       pygame.display.flip()
       pygame.time.wait(3000)
       pygame.quit()
       quit()

   # Call this function when the game is over
   if not running:
       game_over()
   ```

### Step 8: Finalize and Run Your Game
- Put all the pieces together, make sure your code is organized, and test the game.
- Add comments and improve the code as needed.
- Run your game using the terminal:
  ```bash
  python snake_game.py
  ```

This is a basic structure to get you started. You can expand upon this by adding more features like levels, sound effects, and different difficulty settings.

## Input - Prompt 2: Provide the code for a Snake Game in Python. The code should include all the details and feature described above.

## GPT4o Output:

Below is the complete code for a simple Snake Game in Python using the Pygame library. It includes all the basic features described earlier, such as controlling the snake, growing the snake when it eats food, collision detection, and displaying the score.

```python
import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 800
window_height = 600

# Create the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Snake settings
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction
speed = 15

# Food settings
food_pos = [random.randrange(1, (window_width // 10)) * 10,
            random.randrange(1, (window_height // 10)) * 10]
food_spawn = True

# Game variables
score = 0
clock = pygame.time.Clock()

# Font
font_style = pygame.font.SysFont('times new roman', 50)
score_font = pygame.font.SysFont('times new roman', 35)

# Function to display score
def show_score():
    score_surface = score_font.render('Score: ' + str(score), True, white)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (window_width / 10, 15)
    window.blit(score_surface, score_rect)

# Function to display game over
def game_over():
    game_over_surface = font_style.render('Your Score is: ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_width / 2, window_height / 4)
    window.fill(black)
    window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

# Main function
def gameLoop():
    global change_to, snake_direction, snake_pos, snake_body, food_pos, food_spawn, score

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # Validate direction change
        if change_to == 'UP' and not snake_direction == 'DOWN':
            snake_direction = 'UP'
        if change_to == 'DOWN' and not snake_direction == 'UP':
            snake_direction = 'DOWN'
        if change_to == 'LEFT' and not snake_direction == 'RIGHT':
            snake_direction = 'LEFT'
        if change_to == 'RIGHT' and not snake_direction == 'LEFT':
            snake_direction = 'RIGHT'

        # Move the snake
        if snake_direction == 'UP':
            snake_pos[1] -= 10
        if snake_direction == 'DOWN':
            snake_pos[1] += 10
        if snake_direction == 'LEFT':
            snake_pos[0] -= 10
        if snake_direction == 'RIGHT':
            snake_pos[0] += 10

        # Snake body growing mechanism
        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            score += 10
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, (window_width // 10)) * 10,
                        random.randrange(1, (window_height // 10)) * 10]

        food_spawn = True
        window.fill(black)

        # Draw snake
        for pos in snake_body:
            pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        # Draw food
        pygame.draw.rect(window, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        # Check for collisions
        if snake_pos[0] < 0 or snake_pos[0] > window_width - 10:
            game_over()
        if snake_pos[1] < 0 or snake_pos[1] > window_height - 10:
            game_over()

        # Check if the snake hits itself
        for block in snake_body[1:]:
            if snake_pos == block:
                game_over()

        show_score()
        pygame.display.update()

        # Control the game speed
        clock.tick(speed)

# Run the game
gameLoop()
```

### How the Code Works

- **Initialization**: Pygame is initialized, and a game window is created with specific dimensions.

- **Game Loop**: The main game loop listens for keyboard events to change the direction of the snake. It updates the snake's position, checks for collisions, and refreshes the screen.

- **Snake Movement**: The snake moves in the direction set by the arrow keys. The position of the snake is updated based on its direction.

- **Food Consumption**: When the snake's head collides with the food, the snake grows, and a new food item is spawned randomly.

- **Collision Detection**: The game checks for collisions with the walls and with the snake's own body to determine when the game is over.

- **Display**: The score is displayed on the screen, and the game over screen is shown when the snake collides with the walls or itself.

You can run this code in your Python environment to see the Snake Game in action. Feel free to modify the game, add features, or customize it further!

## Prompt 3: 
