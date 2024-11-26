import tkinter as tk
from datetime import datetime, timezone

# Function to update the time displayed
def update_time():
    # GMT time
    current_gmt_time = datetime.now(timezone.utc).strftime('%H:%M:%S GMT')
    gmt_clock_label.config(text=current_gmt_time)

    # Local time
    local_time = datetime.now().strftime('%H:%M:%S Local')
    local_clock_label.config(text=local_time)

    root.after(1000, update_time)  # Update every second

# Functions to handle window dragging
def start_move(event):
    root.x_offset = event.x_root - root.winfo_x()
    root.y_offset = event.y_root - root.winfo_y()

def on_motion(event):
    x = event.x_root - root.x_offset
    y = event.y_root - root.y_offset
    root.geometry(f"+{x}+{y}")

# Initialize the main window
root = tk.Tk()
root.title("GMT and Local Time Clocks")

# Remove the title bar
root.overrideredirect(True)

# Set the background color of the window to black
root.configure(bg='black')

# Add a label to display the GMT time with a digital clock style
gmt_clock_label = tk.Label(
    root,
    font=('Digital-7 Mono', 50, 'italic'),  # Use Digital-7 Mono Italic
    fg='#39FF14',                           # Neon green color
    bg='black',                             # Black background for digital look
    anchor='center'                         # Center-align the text
)
gmt_clock_label.pack(fill="both", expand=True, padx=10, pady=5)

# Add a label to display the local time with a digital clock style
local_clock_label = tk.Label(
    root,
    font=('Digital-7 Mono', 50, 'italic'),  # Use Digital-7 Mono Italic
    fg='#39FF14',                           # Neon green color
    bg='black',                             # Black background for digital look
    anchor='center'                         # Center-align the text
)
local_clock_label.pack(fill="both", expand=True, padx=10, pady=5)

# Add a label for your name and callsign, positioned just under the clocks
callsign_label = tk.Label(
    root,
    text="Jason Howell - N9NDF / TC225",    # Your name and callsigns
    font=('Courier', 20),                   # Smaller font size for the callsign
    fg='#39FF14',                           # Neon green color
    bg='black'                              # Match background with the clock
)
callsign_label.pack(pady=5)

# Set a fixed window size
root.geometry('600x400')

# Bind mouse events to make the window draggable
gmt_clock_label.bind("<Button-1>", start_move)
gmt_clock_label.bind("<B1-Motion>", on_motion)

local_clock_label.bind("<Button-1>", start_move)
local_clock_label.bind("<B1-Motion>", on_motion)

# Start updating the time
update_time()

# Start the GUI event loop
root.mainloop()