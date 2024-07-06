# Water and Break Reminder App
This Python script provides a simple yet effective way to remind you to drink water and take breaks regularly throughout your day. It uses desktop notifications and pop-up dialogs to ensure you stay hydrated and take necessary breaks to maintain your productivity and health.

# Features

Water Reminder:

Sends desktop notifications reminding you to drink water.

Asks for confirmation if you have drunk water through a pop-up dialog.

Tracks your daily water intake and updates you on how much more you need to drink.

Break Reminder:

Sends desktop notifications reminding you to take breaks every 30 minutes.

Starts a countdown timer for a 10-minute break using a Tkinter GUI pop-up.

# Technique Used

Desktop Notifications: Implemented using the plyer library to provide system notifications.

Tkinter GUI: Utilized for creating pop-up dialogs and countdown timers.

Threading: Used to run the break reminder and water reminder concurrently without blocking each other.

Time Management: Incorporated sleep intervals to manage the timing of reminders and breaks.

User Interaction: Leveraged Tkinter's messagebox for user confirmation.
