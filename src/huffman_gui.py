import tkinter as tk
import huffman_algo
import sys

codes = {} 
buttonOneFlag = False

def on_close():
    root.destroy()
    sys.exit()

def start_move(event):
    root.x = event.x
    root.y = event.y

def on_move(event):
    root.geometry(f"500x600+{event.x_root - root.x}+{event.y_root - root.y}")



# Fuction for button 1 pressing
def button_one_pressed(textbox1, text_label):
    print("Button 1 pressed!")
    buttonOneFlag = True
    global text, encoded_text, decoded_result, file_path
    trigger = "encode"
    codes, text, encoded_text, file_path, originalSize, compressedSize = huffman_algo.encodeAndDecode(trigger, None)
    print("Original Text: ", text)
    print("Huffman Codes: ", codes)
    print("Encoded Text: ", encoded_text)
    print(f"Original file size: {originalSize} bytes")
    print(f"Compressed file size: {compressedSize} bytes")

    print("File Path Test 1 ", file_path)

    # Calculate the compression ratio
    ratio = (compressedSize / originalSize) * 100 
    compressionDetailSTR = f"Original: {originalSize} bytes | Compressed: {compressedSize} bytes | Ratio: {ratio:.2f}%"
    
    # Update the label with the compression details
    text_label.config(text=compressionDetailSTR)

    # Creating the string for the textbox
    codes_str = "\n".join(f"'{char}': {code}" for char, code in codes.items())

    # Enable the textbox for editing
    textbox1.config(state=tk.NORMAL)

    # Clear any existing content
    textbox1.delete(1.0, tk.END)

    # Insert the Huffman codes into the textbox
    textbox1.insert(tk.END, "Huffman Codes:\n")
    textbox1.insert(tk.END, codes_str)

    # Set the textbox back to read-only
    textbox1.config(state=tk.DISABLED)

# Function for button 2 pressing
def button_two_pressed(textbox2):
    if buttonOneFlag:
        print("Encode First!")
        return
    print("Button 2 pressed!")
    trigger = "decode"
    print("File path from button two pressed func ", file_path)
    decoded_result = huffman_algo.encodeAndDecode(trigger, file_path)
    print("Decoded Result 101: ", decoded_result)


    textbox2.config(state=tk.NORMAL)

    # Clear any existing content
    textbox2.delete(1.0, tk.END)

    # Insert the decoded text into the textbox
    textbox2.insert(tk.END, "Decoded Result:\n")
    textbox2.insert(tk.END, decoded_result)

    # Set the textbox back to read-only
    textbox2.config(state=tk.DISABLED)
        

def main():
    global root
    root = tk.Tk()
    # For the boarderless windows
    root.overrideredirect(True)  
    # Window Size
    root.geometry("500x600") 
    root.configure(bg="#2C3E50")

    # Custom Title Bar
    title_bar = tk.Frame(root, bg="#1F2A38", relief="raised", bd=0, height=30)
    title_bar.pack(fill=tk.X)
    title_bar.bind("<Button-1>", start_move)
    title_bar.bind("<B1-Motion>", on_move)
    
    close_button = tk.Button(title_bar, text="✖", bg="#E74C3C", fg="white", bd=0, command=on_close)
    close_button.pack(side=tk.RIGHT, padx=5, pady=2)
    
    title_label = tk.Label(title_bar, text="Huffman Compression Tool", bg="#1F2A38", fg="#ECF0F1", font=("Courier New", 12, "bold"))
    title_label.pack(side=tk.LEFT, padx=10)

    # Common Style Dictionary
    label_style = {"bg": "#2C3E50", "fg": "#ECF0F1", "font": ("Courier New", 16, "bold")}
    label_style2 = {"bg": "#2C3E50", "fg": "#ECF0F1", "font": ("Courier New", 10, "bold")}
    button_style = {"bg": "#536872", "fg": "white", "font": ("Courier New", 8), "relief": "flat", "bd": 0, "highlightthickness": 0, "padx": 10, "pady": 5}
    textbox_style = {"bg": "#34495E", "fg": "#ECF0F1", "font": ("Courier New", 10)}

    # Title Label
    title1 = tk.Label(root, text="📦 Huffman Coding Compression Tool", **label_style)
    title1.pack(pady=8)

    defaultText = "Compression details will appear here."
    text_label = tk.Label(root, text=defaultText, **label_style2)
    text_label.pack(pady=8)

    # Button 1
    button1 = tk.Button(root, text="Select Text File", command=lambda: button_one_pressed(textbox1, text_label), **button_style)
    button1.pack(pady=8)

    # Textbox Label
    textbox_label1 = tk.Label(root, text="Huffman Codes:", **label_style2)
    textbox_label1.pack(pady=8)
    
    '''
    Textbox for Huffman Codes
    '''
    # Create a frame to hold the Text widget and Scrollbar
    textbox_frame = tk.Frame(root)
    textbox_frame.pack(pady=8)

    # Create Text widget (for displaying Huffman codes)
    textbox1 = tk.Text(textbox_frame, height=4, width=40, **textbox_style)
    textbox1.pack(side=tk.LEFT)

    # Create a Scrollbar and attach it to the Text widget
    scrollbar = tk.Scrollbar(textbox_frame, command=textbox1.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Link the scrollbar to the Text widget
    textbox1.config(yscrollcommand=scrollbar.set)

    # Set the Text widget to be read-only (optional)
    textbox1.config(state=tk.DISABLED)

    textbox1.insert(tk.END, "Huffman Codes will appear here...")


    # Button 2
    button2 = tk.Button(root, text="Decompress File", command=lambda: button_two_pressed(textbox2), **button_style)
    button2.pack(pady=8)

    # Textbox Label
    textbox_label2 = tk.Label(root, text="Decoded Text:", **label_style2)
    textbox_label2.pack(pady=5)
    
    '''
    Textbox for Decoding
    '''
    textbox2_frame = tk.Frame(root)
    textbox2_frame.pack(pady=8)

    # Create Text widget (for displaying Decoded Text)
    textbox2 = tk.Text(textbox2_frame, height=4, width=40, **textbox_style)
    textbox2.pack(side=tk.LEFT)

    # Create a Scrollbar and attach it to the Text widget
    scrollbar2 = tk.Scrollbar(textbox2_frame, command=textbox2.yview)
    scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)

    # Link the scrollbar to the Text widget
    textbox2.config(yscrollcommand=scrollbar2.set)

    # Set the Text widget to be read-only (optional)
    textbox2.config(state=tk.DISABLED)

    # Insert some default text (for display purposes)
    textbox2.insert(tk.END, "Decoded Text will appear here...")


    root.mainloop()

if __name__ == "__main__":
    main()
