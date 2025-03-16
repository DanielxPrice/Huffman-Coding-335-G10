import tkinter as tk
from tkinter import filedialog
from bitarray import bitarray

def open_read_file():
    # Open file dialog to select a file
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not file_path:
        print("No file selected.")
        return None

    # Read the contents of the file and store in a bitarray
    bit_array = bitarray()
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            bit_array.frombytes(content.encode('utf-8'))
        print(f"File contents successfully stored in a bitarray: {file_path}")
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

    return bit_array
