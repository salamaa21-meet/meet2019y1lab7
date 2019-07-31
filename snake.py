
import turtle
import random #We'll need this later in the lab
turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size.    
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 9
TIME_STEP = 100

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("circle")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Function to draw a part of the snake on the screen

def new_stamp():
    snake_pos = snake.pos() #Get snake’s position
    #Append the position tuple to pos_list
    pos_list.append(snake_pos) 
    #snake.stamp() returns a stamp ID. Save it in some variable         
    stamp= snake.stamp()
    #append that stamp ID to stamp_list.     
    stamp_list.append(stamp)

    #Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for position in range(9) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1] 

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+= SQUARE_SIZE

    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Now draw the new snake part on the screen (hint, you have a 
    #function to do this
    new_stamp()

def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp) # erase last piece of tail
    pos_list.pop(0) # remove last piece of tail's position


snake.direction = "Up"
snake.direction = "Down"
snake.direction = "Left"
snake.direction = "Right"

def up():
    snake.direction="Up" #Change direction to up
    print("You pressed the up key!")

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400


#2. Make functions down(), left(), and right() that change snake.direction
def down():
    snake.direction="Down"
    print("You pressed the up key!")

def left():
    snake.direction="Left"
    print("You pressed the left key!")

def right():
    snake.direction="Right"
    print("You pressed the left key!")
    

turtle.onkeypress(up, "Up") # Create listener for up key
turtle.listen()

turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script

food = turtle.clone()
food.shape("trash.gif") 

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don't forget to hide the food turtle!
for this_food_pos in food_pos :
    food.goto(this_food_pos)
    v=food.stamp()
    food_stamps.append(v)
    food.hideturtle()

#3. Do the same for the other arrow keys
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")

turtle.listen()

def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

    food.goto(food_x,food_y)
    v=food.pos()
    food_pos.append(v)
    f=food.stamp()
    food_stamps.append(f)
        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position 
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
    
colors = ['Blue','Green','Red','Yellow','Orange','purple']

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    
    #Add new lines to the end of the function
    #Grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    # The next three lines check if the snake is hitting the 
    # right edge.
    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()

     # You should write code to check for the left, top, and bottom edges.
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the right edge! Game over!")
        quit()

    elif new_y_pos >= UP_EDGE:
        print("You hit the top edge! Game over!")
        quit()

    elif new_y_pos <= DOWN_EDGE:
        print("You hit the bottum edge! Game over!")
        quit()

    if(new_x_pos, new_y_pos) in pos_list[:-1]:
        print("you hit the snake! Game over!")
        quit()
    
    #If snake.direction is up, then we want the snake to change
    #it’s y position by SQUARE_SIZE
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction == "Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")
    #4. Write the conditions for RIGHT and LEFT on your own
    elif snake.direction == "Left":
        snake.goto(x_pos - SQUARE_SIZE , y_pos)
        print("You moved left")
        
    elif snake.direction == "Right":
        snake.goto(x_pos + SQUARE_SIZE , y_pos)
        print("You moved right!")


    #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this
    new_stamp()

     #If snake is on top of food item
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_pos.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp
        print("You have eaten the food!")
        snake.color(random.choice(colors))
    else:
        remove_tail()
        
    #HINT: This if statement may be useful for Part 8


    #Don't change the rest of the code in move_snake() function:
    #If you have included the timer so the snake moves 
    #automatically, the function should finish as before with a 
    #call to ontimer()
    turtle.ontimer(move_snake,TIME_STEP) #<--Last line of function

    #remove the last piece of the snake (Hint Functions are FUN!)

    if len(food_stamps) <= 4 :
    			make_food()
    #remove_tail()

    			
move_snake()
