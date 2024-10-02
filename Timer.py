import customtkinter as ctk
import keyboard  # Module for capturing global key presses
from PIL import Image  # To handle images with customtkinter

# Class to handle each individual timer
class Timer:
    def __init__(self, image, name, duration, label):
        self.image = image
        self.name = name
        self.duration = duration
        self.remaining_time = duration
        self.label = label
        self.running = False
        self.paused = False  # State to check if the timer is paused
        self.timer_id = None  # To store the after() callback ID

    # Start the timer using the `after()` method
    def start(self):
        self.running = True
        self._countdown()

    # Countdown function that uses the `after()` method
    def _countdown(self):
        if self.running and not self.paused and self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_label(f"{self.name} Time Left: {self.remaining_time} sec", "#eeeeee")
            # Schedule the _countdown method to be called after 1 second (1000 ms)
            self.timer_id = self.label.after(1000, self._countdown)
        elif self.remaining_time <= 0:
            self.update_label(f"{self.name} Time's up!", "#5fce4e")
            self.running = False  # Stop the timer when time's up

    # Update the label text and color
    def update_label(self, text, color):
        self.label.configure(text=text, text_color=color)

    # Reset the timer to its initial state
    def reset(self):
        if self.name != "Freed Shadow" or "AOSM" or "Night Parade" or "GROTTO" or self.remaining_time <= 0:
            if self.timer_id:
                self.label.after_cancel(self.timer_id)
            self.remaining_time = self.duration
            self.update_label(f"{self.name} Time Left: {self.duration} sec", "#eeeeee")
            self.running = True
            self._countdown()  # Restart the countdown when reset

    # Stop the timer
    def stop(self):
        if self.timer_id:
            self.label.after_cancel(self.timer_id)
        self.running = False

    # Pause the timer
    def pause(self):
        self.paused = True
        if self.timer_id:
            self.label.after_cancel(self.timer_id)  # Cancel the ongoing countdown

    # Resume the timer from where it was paused
    def resume(self):
        self.paused = False
        if self.running:  # Only resume if the timer was running before
            self._countdown()

# Function to handle key presses, including combinations
def handle_keypress(key, timers, status_label):
    key = key.lower()  # Convert the key press to lowercase
    if key == 'f2':  # Change 'F2' to what you want for pause/resume
        global all_paused  # Use global state to track if timers are paused or running
        if all_paused:
            for timer in timers.values():
                timer.resume()
            update_status_label(status_label, "Running", "#5fce4e")  # Green color for "Running"
            all_paused = False
        else:
            for timer in timers.values():
                timer.pause()
            update_status_label(status_label, "Paused", "#ff9933")  # Orange color for "Paused"
            all_paused = True
    elif key == 'f3':  # Change 'F2' to what you want to reset timers 
        for name, timer in timers.items():
            timer.remaining_time = 0
    else:  # Handle other keys for resetting individual timers
        for name, timer in timers.items():
            # Check if the key combination is pressed
            if '+' in timer.key:
                # Split the combination and check if both keys are pressed
                keys = timer.key.split('+')
                if all(keyboard.is_pressed(k) for k in keys):
                    timer.reset()
            elif key == timer.key:
                timer.reset()

# Update the status label text and color
def update_status_label(label, text, color):
    label.configure(text=f"Timer: {text}", text_color=color)

# Main application setup
def main():
    global all_paused
    all_paused = False  # Initial state of timers (not paused)
    
    # Configuration of initial timer values and key bindings
    timer_settings = {
    "Example Name": {"duration": 15, "key": "r"},  # New timer added   
    }

    # Create the main application window
    app = ctk.CTk()
    app.resizable(True, True)
    app.title("Timer")
    app.geometry("300x100")  # Adjusted size for better UI layout
    app.attributes('-topmost', True)  # Always on top
    app.attributes('-alpha', 0.8)  # Slight transparency
    app.configure(fg_color="#000000")   

    # Configure customtkinter appearance
    ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Light", "Dark"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue")

    # Dictionary to hold timer objects
    timers = {}

    # Create labels and initialize Timer objects for each timer setting
    for idx, (name, config) in enumerate(timer_settings.items()):
        # Create a label for each timer
        
        # Check if 'image' key exists and load image accordingly
        if 'image' in config:
            if name in ["Freed Shadow", "AOSM", "Night Parade", "GROTTO"]:
                ctkImage = ctk.CTkImage(light_image=Image.open(config['image']), dark_image=Image.open(config['image']), size=(65, 50))
            else:
                ctkImage = ctk.CTkImage(light_image=Image.open(config['image']), dark_image=Image.open(config['image']), size=(50, 50))
        else:
            ctkImage = None  # No image specified

        label = ctk.CTkLabel(app, image=ctkImage,compound="left", padx=10, text=f"{name} Time Left: 0 sec", font=("Helvetica", 18))
        label.pack(pady=10)

        # Create and store Timer object
        timer = Timer(config.get("image"), name, config["duration"], label)
        timer.key = config["key"]  # Store key in timer object for reference
        timers[name] = timer

        # Immediately set remaining time to 0 and display "Time's up!" initially
        timer.remaining_time = 0  # Set remaining time to 0
        timer.update_label(f"{timer.name} Time's up!", "#5fce4e")  # Show time's up message

    # Create a status label to show if the timers are running or paused
    status_label = ctk.CTkLabel(app, text="Timer: Running", font=("Helvetica", 16), text_color="#5fce4e")
    status_label.pack(pady=10)

    # Register a listener for key presses, passing the status label as well
    keyboard.on_press(lambda e: handle_keypress(e.name, timers, status_label))

    # Run the main loop of the application
    app.mainloop()

    # Stop all timers when the application closes
    for timer in timers.values():
        timer.stop()

if __name__ == "__main__":
    main()
