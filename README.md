
# Timer Application

This is a simple Timer Application built using Python and `customtkinter` with hotkey bindings. 
The application allows users to create multiple timers that can be reset using specific key bindings. 
**Need to run as admin** to works while using Elsword somehow.

## Features

- **Multiple Timers**: Each timer is associated with a different key.
- **Custom Key Bindings**: Supports single keys and combinations (e.g., `ctrl+right`).
- **Real-Time Countdown**: Timers are displayed and updated in real-time.
- **Adjustable UI**: Users can modify window size and timer labels easily.

## Installation

1. Clone the repository then go in the folder (or just download Timer.py): 

   ```bash
   git clone https://github.com/Nyno3333/Timer.git
   cd Timer
   ```

2. Install the required packages (cmd):

   ```bash
   pip install customtkinter
   pip install keyboard
   pip install pillow

   ```

3. Run the application (cmd):

   ```bash
   python Timer.py
   ```

## Before  Using

### Example Modifications
If you want to add a new timer named **"Example Name"** with a duration of 15 seconds and bound to the **"r"** key combination, go to **Line 108**  your timer settings should look like this:

```python
timer_settings = {
    ...
    "Example Name": {"duration": 15, "key": "r"},  # New timer added   
    "Example Name": {"duration": 15, "key": "r", "image": "xxx.png"},  # New timer with image added
}
```

- To add a new timer, copy an existing line and paste it below. Make sure to update the **name**, **duration**, and **key binding** as needed.
- Don't forget to add a comma `,` at the end of each line to avoid syntax errors.
- Use **"Freed Shadow"**, **"AOSM"**, **"Night Parade"**, **"GROTTO"** instead of **"Example Name"** to have the correct title image ratio.



### Modifying the Window Size & Title
To change the size of the application window, go to **Line 111** in the script:

```python
   app.geometry("340x130")  # Adjusted size for better UI layout
   app.attributes('-topmost', True)  # Always on top
   app.attributes('-alpha', 0.8)  # Slight transparency
```
- The **first value** is the width of the window, and the **second value** is the height.
- Optionally, you can change the **title of the window** just above.
- And the lasts ones are the background **opacity and color**.

### Pause/Resume and Reset Timers
Default binds are F2 to pause/resume and F3 to reset timers:
```python
   if key == 'f2':  # Change 'F2' to what you want for pause/resume (Line 68)
   ```
```python
   elif key == 'f3':  # Change 'F2' to what you want to reset timers (Line 80)
```
