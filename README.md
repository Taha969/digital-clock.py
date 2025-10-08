Dual Time Digital Clock 🕰️

A simple digital clock application built with Python and the Tkinter library for a lightweight graphical interface. This application simultaneously displays the current time in two modes: Local Time and Greenwich Mean Time (GMT), with real-time updates.

Features ✨

    Dual Time Display: Shows both Local Time (LOC) and Greenwich Mean Time (GMT) in the same window.

    Real-Time Updates: The time is updated every second, ensuring constant accuracy.

    12-Hour Format: Time is displayed using the 12-hour clock system, including the AM/PM indicator.

    Simple GUI: A fixed-size window with distinct background colors to visually separate the two time zones.

Prerequisites 🛠️

To run this application, you will need:

    Python 3.x

    Tkinter Library: This library is typically included by default with standard Python installations on most operating systems.

Installation and Setup 🚀

    Save the Code: Save the provided Python code into a file named digital_clock.py.

    Open Terminal: Navigate to the directory where you saved the file using your terminal or command prompt.

    Run the Application: Execute the script using the Python interpreter:
    Bash

    python digital_clock.py

    A graphical window displaying the two times will open immediately.

How It Works 🧑‍💻

The application logic is centered around a few key components:

1. GUI Setup

    window = Tk(): Creates the main application window.

    window.geometry("510x250") and window.resizable(False, False): Sets a fixed size for the window and prevents the user from resizing it.

    Two Label widgets (clock_l and clock_g) are created to display the Local and GMT times, using distinct background colors (lavender and pink) for visual separation.

2. The get_time() Function

This is the core function responsible for refreshing the clock:

    It uses the strftime and gmtime() functions to fetch the current GMT time in the 12-hour format ("%I:%M:%S %p").

    It uses strftime and localtime() to fetch the current Local Time (LOC) in the same format.

    It updates the text of the two Label widgets using the .config() method.

    Crucially, it uses window.after(1000, get_time) to schedule the function to call itself again after 1000 milliseconds (1 second), creating the continuous, real-time update loop.

Code Notes 💡

    The time formatting string "%I:%M:%S %p" controls the output:

        %I: Hour as a 12-hour number.

        %M: Minute.

        %S: Second.

        %p: Displays AM or PM.

    To change the clock to a 24-hour format, you would simply change the format string inside the get_time function to "%H:%M:%S".
