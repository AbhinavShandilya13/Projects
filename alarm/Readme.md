# Alarm App

This is a simple alarm application built using Python and Tkinter, which allows you to set an alarm and be reminded at the specified time with a sound. The application provides a graphical user interface (GUI) where you can select the hour, minute, second, and period (AM/PM) to set the alarm. It also gives you the option to activate and deactivate the alarm as needed.

## Prerequisites

Before running the application, you need to make sure you have the following installed on your system:

- Python 3.x
- Tkinter (usually comes with Python by default)
- pygame library: You can install it using `pip install pygame`.
- PIL (Python Imaging Library) library: You can install it using `pip install pillow`.

## How to Run

1. Clone or download the project files from the repository.
2. Ensure you have all the prerequisites installed on your system.
3. Place the `icon.png` file in the same directory as the Python script. This image will be used as the application icon.
4. Place the `song.mp3` file in the same directory as the Python script. This audio file will be played when the alarm is triggered.
5. Open a terminal or command prompt and navigate to the directory containing the script and the required files.
6. Run the Python script using the command: `python alarm_app.py`.

## Using the Alarm App

1. When you run the application, a graphical window will open, displaying the alarm setting options.
2. Set the alarm time by selecting the hour, minute, second, and period (AM/PM) using the drop-down menus.
3. Click the "Activate" radio button to activate the alarm. The alarm will be triggered when the current time matches the set alarm time.
4. Once the alarm is activated, you can click the "Deactivate" radio button to stop the alarm sound.
5. When the alarm is triggered, a sound will be played using the `song.mp3` file, alerting you that it's time to take a break or perform the designated task.

## Note

- Make sure to have the `song.mp3` file present in the same directory as the script, containing the audio you want to play as the alarm sound.
- The alarm will keep checking the current time every second to see if it matches the set alarm time. If they match, the alarm sound will be played.

**Enjoy your alarm app! Feel free to modify, enhance, or customize it as per your requirements.**
