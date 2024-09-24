import turtle, random, time

"""
Snake Game using the Turtle Graphics library.

This game simulates the classic Snake game. The player controls the snake using
the arrow keys to move it up, down, left, or right. The goal is to eat the food
that appears randomly on the screen, causing the snake to grow in length and 
increase the score. The game ends if the snake collides with the screen border 
or its own body. The player's highest score is tracked and displayed throughout 
the game.

Features:
- Snake controlled by arrow keys.
- Snake grows in size as it eats food.
- Speed increases with each piece of food consumed.
- Game resets when the snake collides with walls or its own body.
- Current and high scores displayed on the screen.
"""

# Game settings
width = 800  # Screen width
height = 700  # Screen height
current_score = 0  # Score of the current game session
high_score = 0  # Highest score achieved
speed = 0.1  # Initial movement speed of the snake

# Set up the screen
screen = turtle.Screen()  # Initialize the screen object
screen.setup(width, height)  # Set screen dimensions
screen.title('Snake Game')  # Set game title
screen.bgcolor('black')  # Set background color to black
screen.tracer(0)  # Disable auto updates, we will update manually

# Create the snake's head
head = turtle.Turtle()  # Initialize turtle object for the head
head.speed(0)  # Set drawing speed of head object to maximum
head.color('red')  # Set head color to red
head.shape('square')  # Set the shape of the head to a square
head.penup()  # Disable drawing a line when moving
head.goto(-width // 3, 0)  # Start the head at a specific location
head.direction = 'right'  # Initial movement direction

# Create food for the snake
food = turtle.Turtle()  # Initialize turtle object for the food
food.speed(0)  # Set food object's drawing speed to maximum (stationary object)
food.color('yellow')  # Set food color to yellow
food.shape('circle')  # Set the shape of the food to a circle
food.penup()  # Disable drawing a line when moving
food.goto(0, 0)  # Start food at the center of the screen

# Score display
score = turtle.Turtle()  # Initialize turtle object for the score display
score.speed(0)  # Set movement speed to maximum (not affecting game speed)
score.color('white')  # Set text color to white
score.penup()  # Disable drawing a line when moving
score.hideturtle()  # Hide the turtle shape (only show the text)
score.goto(0, 300)  # Position the score at the top of the screen
score.write(f'Score: {current_score}\t\tHigh Score: {high_score}', align='center', font=('Arial', 24, 'normal'))  # Display initial scores

# Move the snake's head based on direction
def move():
    if head.direction == 'up':  # Move up
        head.sety(head.ycor() + 20)  # Increase y-coordinate
    elif head.direction == 'down':  # Move down
        head.sety(head.ycor() - 20)  # Decrease y-coordinate
    elif head.direction == 'right':  # Move right
        head.setx(head.xcor() + 20)  # Increase x-coordinate
    elif head.direction == 'left':  # Move left
        head.setx(head.xcor() - 20)  # Decrease x-coordinate

# Direction control functions
def move_up():
    if head.direction != 'down':  # Prevent moving directly opposite
        head.direction = 'up'
def move_down():
    if head.direction != 'up':
        head.direction = 'down'
def move_right():
    if head.direction != 'left':
        head.direction = 'right'
def move_left():
    if head.direction != 'right':
        head.direction = 'left'

# Set up key bindings to control the snake
screen.listen()  # Listen for keyboard input
screen.onkeypress(move_up, 'Up')  # Bind the Up arrow to move up
screen.onkeypress(move_down, 'Down')  # Bind the Down arrow to move down
screen.onkeypress(move_right, 'Right')  # Bind the Right arrow to move right
screen.onkeypress(move_left, 'Left')  # Bind the Left arrow to move left

# List to store snake's body parts
snake_body = []

# Main game loop
while True:
    screen.update()  # Update the screen after every frame

    # Check for collision with the screen border
    if head.xcor() > ((width // 2) - 10) or head.xcor() < (-(width // 2) + 10) or head.ycor() > ((height // 2) - 10) or head.ycor() < (-(height // 2) + 10):
        time.sleep(1)  # Pause for a moment after the collision
        current_score = 0  # Reset current score
        speed = 0.1  # Reset speed
        score.penup()  # Prepare score display for update
        score.clear()  # Clear the previous score
        head.goto(-width // 3, 0)  # Reset the snake's head position
        head.direction = 'right'  # Reset direction to right
        # Move all body parts off screen
        for part in snake_body: 
            part.goto(1000, 1000)
        snake_body.clear()  # Clear the snake's body
        score.write(f'Score: {current_score}\t\tHigh Score: {high_score}', align='center', font=('Arial', 24, 'normal'))  # Update score

    # Check if the snake eats the food
    if head.distance(food) < 20:
        food.goto(random.randint(-((width//2)-20), (width//2)-20), random.randint(-((height//2)-20), (height//2)-20))  # Move food to a new random position
        # Add a new part to the snake's body
        new_part = turtle.Turtle()  # Initialize a new body part
        new_part.speed(0)  # Set speed to maximum
        new_part.color('green')  # Set body color to green
        new_part.shape('square')  # Set body shape to square
        new_part.penup()  # Disable drawing when moving
        snake_body.append(new_part)  # Append the new part to the snake body
        current_score += 10  # Increase score
        high_score = current_score if high_score < current_score else high_score  # Update high score if needed
        score.penup()  # Prepare for score update
        score.clear()  # Clear previous score
        score.write(f'Score: {current_score}\t\tHigh Score: {high_score}', align='center', font=('Arial', 24, 'normal'))  # Display updated score
        speed -= 0.001  # Increase the snake's speed

    # Move the snake body to follow the head
    for i in range(len(snake_body)-1, 0, -1):
        snake_body[i].goto(snake_body[i-1].xcor(), snake_body[i-1].ycor())  # Move each part to the position of the previous part
            
    # If there is a body, the first part follows the head
    if len(snake_body) > 0:
        snake_body[0].goto(head.xcor(), head.ycor())
            
    move()  # Move the head based on its direction

    # Check for collision with the snake's own body
    for part in snake_body:
        if part.distance(head) < 20:
            time.sleep(1)  # Pause after collision
            current_score = 0  # Reset score
            speed = 0.1  # Reset speed
            score.penup()  # Prepare for score update
            score.clear()  # Clear previous score
            head.goto(-width // 3, 0)  # Reset head position
            head.direction = 'right'  # Reset direction to right
            # Move all body parts off screen
            for part in snake_body:
                part.goto(1000, 1000)
            snake_body.clear()  # Clear the snake's body
            score.write(f'Score: {current_score}\t\tHigh Score: {high_score}', align='center', font=('Arial', 24, 'normal'))  # Update score
    
    time.sleep(speed)  # Control the speed of the game
