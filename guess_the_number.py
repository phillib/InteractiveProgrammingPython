# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random


num_range = 100
count = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global num_range
    global count
    
    if num_range == 100:
        count = 7
    else:
        count = 10
        
    secret_number = random.randrange(0, num_range)
    
    #print secret_number
    print "New game.  Range is from 0 to", num_range
    print "You have", count, "guesses"
    print
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()
  
   

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
   
    
    
def input_guess(guess):
    # main game logic goes here	
    global num_range
    global count
    guess = int(guess)
    
    count = count - 1
       
    print "Guess was", guess
    
    if count > 0:
        if guess > secret_number:
            print "Lower"
            print "You have", count, "guesses remaining"
            #print
        elif guess < secret_number:
            print "Higher"
            print "You have", count, "guesses remaining"
            #print
        else:
            print "Correct!  You Win!"
            print
            new_game()
    else:
        if guess == secret_number:
            print "Correct!  You Win!"
            print
            new_game()
        else:
            print "You have", count, "guesses remaining"
            print "You ran out of guesses, the number was", secret_number
            print
            new_game()
        
    print
        
    
  
# create frame
frame = simplegui.create_frame("Guess the Number", 300, 300)
input = frame.add_input("My Guess", input_guess, 100)
frame.add_button("Range: 0 - 100", range100, 200)
frame.add_button("Range: 0 - 1000", range1000, 200)
# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric

