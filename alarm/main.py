from threading import Thread
from tkinter.ttk import *
from tkinter import *
from datetime import datetime
from pygame import mixer
from time import sleep

from PIL import ImageTk, Image

# Colors
bg_color = '#464667'  # Background color for the window
co1 = "#566FC6"  # Blue color for labels and buttons
co2 = "#000000"  # Black color for text

# Create the main window
window = Tk()
window.title("")

window.geometry('350x150')
window.configure(bg=bg_color)

# Create frames to organize the layout
frame_line = Frame(window, width=400, height=5, bg=co1)  # Frame for the top blue line
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=400, height=290, bg=bg_color)  # Frame for the main content
frame_body.grid(row=1, column=0)

# Add application image to the frame
img = Image.open('icon.png')  # Load the application icon image
img.resize((100, 100))  # Resize the image (not in place, just for displaying purposes)
img = ImageTk.PhotoImage(img)  # Convert image to Tkinter PhotoImage

app_image = Label(frame_body, height=100, image=img, bg=bg_color)  # Create a label to display the image
app_image.place(x=10, y=10)  # Place the image label on the frame

# Add application title to the frame
name = Label(frame_body, text="Alarm", height=1, font=("Ivy 18 bold"), bg=bg_color)
name.place(x=125, y=10)

# Create drop-down menus for setting the alarm time (hour, minute, second, period)
hour = Label(frame_body, text="Hour", height=1, font=("Ivy 10 bold"), bg=bg_color, fg=co1)
hour.place(x=127, y=40)
c_hour = Combobox(frame_body, width=2, font=('arial 15 '))
c_hour['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
c_hour.current(0)
c_hour.place(x=130, y=58)

min = Label(frame_body, text="Min", height=1, font=("Ivy 10 bold"), bg=bg_color, fg=co1)
min.place(x=177, y=40)
c_min = Combobox(frame_body, width=2, font=('arial 15 '))
c_min['values'] = tuple(str(i).zfill(2) for i in range(60))  # Use zfill to pad single-digit numbers with a leading 0
c_min.current(0)
c_min.place(x=180, y=58)

sec = Label(frame_body, text="Sec", height=1, font=("Ivy 10 bold"), bg=bg_color, fg=co1)
sec.place(x=227, y=40)
c_sec = Combobox(frame_body, width=2, font=('arial 15 '))
c_sec['values'] = tuple(str(i).zfill(2) for i in range(60))
c_sec.current(0)
c_sec.place(x=230, y=58)

period = Label(frame_body, text="Period", height=1, font=("Ivy 10 bold"), bg=bg_color, fg=co1)
period.place(x=277, y=40)
c_period = Combobox(frame_body, width=3, font=('arial 15 '))
c_period['values'] = ('AM', 'PM')
c_period.current(0)
c_period.place(x=280, y=58)

# Function to activate the alarm
def activate_alarm():
    t = Thread(target=alarm)  # Start a new thread to run the alarm function in the background
    t.start()

# Function to deactivate the alarm
def deactivate_alarm():
    print("deactivate: ", selected.get())  # Print a message for debugging purposes
    mixer.music.stop()  # Stop the alarm sound

# Variable to store the state of the radio buttons (1 for activated, 0 for deactivated)
selected = IntVar()

# Create the "Activate" radio button and set its properties
rad1 = Radiobutton(frame_body, font=("arial 10 bold"), value=1, text='Activate', bg=bg_color, 
                   command=activate_alarm, variable=selected)
rad1.place(x=125, y=95)

# Function to play the alarm sound
def sound_alarm():
    mixer.music.load('song.mp3')  # Load the specified mp3 file for the alarm sound
    mixer.music.play()  # Play the music
    selected.set(0)  # Reset the radio button to "Deactivate" after playing the alarm sound
    # Create the "Deactivate" radio button to stop the alarm
    rad2 = Radiobutton(frame_body, font=("arial 10 bold"), value=2, text='Deactivate', bg=bg_color,
                       command=deactivate_alarm, variable=selected)
    rad2.place(x=200, y=95)

# Function to check the alarm time and play the alarm sound if necessary
def alarm():
    while True:  # Run the loop indefinitely
        control = selected.get()  # Get the state of the radio buttons
        print(control)  # Print the state for debugging purposes

        # Get the current time
        now = datetime.now()
        hour = now.strftime('%I')  # Hour in 12-hour format with leading zero removed
        minute = now.strftime('%M')  # Minute with leading zero
        second = now.strftime('%S')  # Second with leading zero
        period = now.strftime('%p')  # AM or PM

        # Get the alarm time from the drop-down menus
        alarm_hour = c_hour.get()
        alarm_min = c_min.get()
        alarm_sec = c_sec.get()
        alarm_period = c_period.get()
        alarm_period = str(alarm_period.upper())

        # Check if the alarm is activated and if the current time matches the set alarm time
        if control == 1:
            if alarm_hour == hour and alarm_min == minute and alarm_sec == second and alarm_period == period:
                print("Time To Take a Break")  # Print a message for debugging purposes
                sound_alarm()  # Play the alarm sound

        sleep(1)  # Wait for 1 second before checking the alarm time again

# Initialize the mixer for playing the sound
mixer.init()

# Start the Tkinter main loop
window.mainloop()
