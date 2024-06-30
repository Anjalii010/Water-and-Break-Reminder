import time
import threading
from plyer import notification
import tkinter as tk
from tkinter import messagebox
# from playsound import playsound

# Water reminder functions
def notify_water():
    notification.notify(
        title="Please Drink Water!!",
        message="Adequate hydration supports overall health and enhances physical and cognitive performance",
        timeout=10
    )

def ask_water():
    root = tk.Tk()
    root.withdraw()
    answer = messagebox.askyesno("Water reminder", "Did you drink a Glass of Water?")
    root.destroy()
    return answer

def drink_water():
    total_intake_in_ml = 4000
    current_intake_in_ml = 0
    glass_size_in_ml = 300
    while current_intake_in_ml < total_intake_in_ml:
        notify_water()
        if ask_water():
            current_intake_in_ml += glass_size_in_ml
        remaining_water_in_ml = total_intake_in_ml - current_intake_in_ml
        if remaining_water_in_ml > 0:
            print(f"Great! You have {remaining_water_in_ml} ml more to go.")
        else:
            print("Congratulations! You've reached your daily water intake goal.")
            break
        time.sleep(60 * 2)  # Sleep for 2 hours

# Break reminder functions
def notify_break():
    notification.notify(
        title="TIME TO TAKE A BREAK!!",
        message="It's been half an hour, take a 10-minute break!",
        timeout=5,
    )

def start_break_timer():
    while True:
        # Work for 30 minutes
        time.sleep(2* 60)
        notify_break()
        
        # Take a 10-minute break
        root = tk.Tk()
        root.title("Break Timer")
        
        label = tk.Label(root, text="10:00", font=('calibri', 40, 'bold'), fg='red')
        label.pack(pady=20)
        
        countdown_time = 30  # 10 minutes in seconds
        
        def countdown(time_left):
            if time_left > 0:
                mins, secs = divmod(time_left, 60)
                time_format = '{:02d}:{:02d}'.format(mins, secs)
                label.config(text=time_format)
                root.after(1000, countdown, time_left - 1)
            else:
                print("TIMES UP!!")
                #messagebox.showinfo("Break Timer", "Time's up!")  # Show the pop-up message
                # playsound('audio.mp3')  # Play the alarm sound
                root.destroy()
        
        countdown(countdown_time)
        root.mainloop()

if __name__ == "__main__":
    # Run the break timer in a separate thread
    break_thread = threading.Thread(target=start_break_timer)
    break_thread.start()

    # Run the water reminder in the main thread
    drink_water()
