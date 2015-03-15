# template for "Stopwatch: The Game"
import simplegui
 
# define global variables


time = 0
count = 0
success = 0
message= ''
startTimer = False
 
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global message
    minute = t // 600
    tensecond = (t - minute * 600) // 100
    second = (t - minute * 600 - tensecond * 100) // 10
    decisecond = t % 10
 
    message = str(minute)+":"+str(tensecond)+str(second)+":"+str(decisecond)
    return message
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global startTimer 
    startTimer = True
    timer.start()
 
def stop():
    timer.stop()
    global startTimer, count, success
    if startTimer == True:
        startTimer = False
        count += 1
        if time % 10 == 0:
            success +=1   
        
def reset():
    global time, count, success, startTimer
    timer.stop()
    time = 0
    count = 0
    success = 0
    startTimer = False
    
# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time = time +1
 
# define draw handler
def draw(c):
    global message
    c.draw_text(format(time), (100, 125), 36, "white")  
    score = str(success)+"/"+str(count)
    c.draw_text(score, (240, 40), 24, "Green")
    
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
timer = simplegui.create_timer(100, tick)
 
# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
 
# start frame
frame.start()
 
# Please remember to review the grading rubric
