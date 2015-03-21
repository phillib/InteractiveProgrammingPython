# multiply and subtract on keydown / keyup
# utilizes codeskulptor.org

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
number = 5
count = 0


# define event handlers
def draw(canvas):
    canvas.draw_text(str(number), (WIDTH / 8, HEIGHT / 1.5), 200, 'Red')

def keydown(key):
    global number

    if key == simplegui.KEY_MAP["up"]:
        number = number * 2 # multiply number by 2 when up key is pressed
#        print number

        
def keyup(key):
    global number
    global count
    if key == simplegui.KEY_MAP["up"]:
        number = number -3 # subtract 3 from number when up key is released
        count = count + 1
        print "Press count is:", count
        print "Your result is:", number
        print
 
    
# create frame 
frame = simplegui.create_frame("Multiply and Subtract", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
frame.start()
