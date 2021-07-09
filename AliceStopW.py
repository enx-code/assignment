"""
App name "Stopwatch"
Author: Enkhbat B.
©2021 Enkhbat and ©2021 Alice
Version 1.1
"""
import tkinter as tk

# variables
# boolean variable to control state of time
running = False
# time variables initially set to 0
hours, minutes, seconds, milliseconds = 0,0,0,0

# global
# global will be used to modify variables putside functions

# functions
# start, pause, reset function will be called when button activated

#start function
def start():
    global running
    if not running:
        update()
        running = True
 #pause function
def pause():
    global running
    if running:
        # cancel update of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False
# reset function
def reset():
    global running
    if running:
        #cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = false
    # set variable back to zero
    global hours, minutes, seconds, milliseconds
    hours,minutes, seconds, milliseconds = 0, 0, 0, 0 
    #set label back to zero
    stopwatch_label.config(text="00:00:00:00")
# update stopwatch function
def update():
    #update seconds with (addition) compound assignment operator
    global hours, minutes, seconds, milliseconds
    milliseconds +=1
    if milliseconds == 10:
        seconds +=1
        milliseconds = 0
    if seconds == 60:
        minutes +=1
        seconds = 0
    if minutes == 60:
        hours +=1
        minutes = 0
    # format time to include leading zeros
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    milliseconds_string = f'{milliseconds}' if milliseconds > 9 else f'{milliseconds}'
    #update timer label after 100 ms (1 second)
    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string + ':' + milliseconds_string)
    #after each second(1000 milliseconds), call update fanction
    #use update_time variable to cancel or pause the time using after_cancel
    global update_time
    update_time = stopwatch_label.after(100, update)
#create main window
gui = tk.Tk()
gui.geometry('550x230')
gui.title("Alice's Stopwatch")
#label to display time
stopwatch_label = tk.Label(text='00:00:00:00', font=("Comic Sans MS", 80))
stopwatch_label.pack()


#start, pause, reset quit buttons
start_button = tk.Button(text='start',
                         height=5,
                         width=7,
                         font=('Comic Sans MS',30),
                         command=start)
start_button.pack(side=tk.LEFT)
pause_button = tk.Button(text='pause',
                         height=5,
                         width=7,
                         font=('Comic Sans MS',30),
                         command=pause)
pause_button.pack(side=tk.LEFT)
reset_button = tk.Button(text='reset',
                         height=5,
                         width=7,
                         font=('Comic Sans MS',30),
                         command=reset)
reset_button.pack(side=tk.LEFT)
quit_button = tk.Button(text='quit',
                        height=5,
                        width=7,
                        font=('Comic Sans MS',30),
                        command=gui.destroy)
quit_button.pack(side=tk.LEFT)
#run program
gui.mainloop()
