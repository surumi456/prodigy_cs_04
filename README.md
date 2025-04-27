# Simple Keylogger

This repository contains a Python script that implements a basic keylogger using the `pynput` library. The keylogger records keystrokes and logs them into a file named `key_log.txt`.

## Features

- **Keystroke Logging**: Captures and logs every key pressed on the keyboard.
- **Special Key Handling**: Differentiates between regular character keys and special keys (e.g., `Shift`, `Enter`, `Ctrl`).
- **Esc Key to Stop**: Stops the keylogger when the `Esc` key is pressed.

## Installation

To run this script, you need to have Python installed along with the following package:

- [pynput](https://pypi.org/project/pynput/) (A library for controlling and monitoring input devices)

You can install `pynput` using pip:

```bash
pip install pynput
```

> **Note:** Running a keylogger requires administrative privileges on most systems. Please ensure you have the appropriate permissions before running this script.

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ayisharizwi/prodigy_cs_04.git
   cd prodigy_cs_04
   ```

2. **Run the Script:**

   ```bash
   python keylogger.py
   ```

3. **Logging:**

   - All keypresses will be recorded in a file named `key_log.txt` located in the same directory as the script.
   - Regular keys (e.g., `a`, `1`, `x`) will be logged as they are.
   - Special keys (e.g., `Shift`, `Enter`, `Backspace`) will be logged with their respective names.

4. **Stopping the Keylogger:**

   - Press the `Esc` key to stop the keylogger and terminate the script.

## Example Log Output

Here is an example of what the `key_log.txt` file might look like:

```
hello world 
 Key.space  Key.shift  H Key.shift  W orld 
```

## How It Works

1. **Key Press Detection:**
   - The script uses `pynput`'s `Listener` to monitor keyboard events.
   - When a key is pressed, the `on_press` function logs the key to `key_log.txt`.

2. **Handling Special Keys:**
   - Special keys like `Shift`, `Ctrl`, `Enter`, and `Backspace` are handled by checking if the pressed key has an associated character (`key.char`). If not, the key is treated as a special key and logged with its name.

3. **Stopping the Logger:**
   - The keylogger will run indefinitely until the `Esc` key is pressed, which triggers the `on_release` function to stop the listener.

