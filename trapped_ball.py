# Trapped bouncy ball
# utilizes codeskulptor.org
# The ball goes at a set speed and continually bounces around the container.
# reflecting off of any wall it hits.
import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-40.0 / 60.0,  5.0 / 60.0]

# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS: # Left wall
        vel[0] = - vel[0] 
    if ball_pos[0] >= WIDTH - BALL_RADIUS: # Right wall
        vel[0] = - vel[0] 
    if ball_pos[1] >= HEIGHT - BALL_RADIUS: # Bottom wall
        vel[1] = - vel[1] 
    if ball_pos[1] <= BALL_RADIUS: # Top wall
        vel[1] = - vel[1] 

    
    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Ball physics", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()
