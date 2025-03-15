import tkinter as tk

uncompressedFile = ""
compressedFile = ""

def on_close():
    root.destroy()

def start_move(event):
    root.x = event.x
    root.y = event.y

def on_move(event):
    root.geometry(f"500x600+{event.x_root - root.x}+{event.y_root - root.y}")



# Fuction for button 1 pressing
def button_one_pressed():
    print("Button 1 pressed!")



# Function for button 2 pressing
def button_two_pressed():
    print("Button 2 pressed!")







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

    # Button 1
    button1 = tk.Button(root, text="Select Text File", command=button_one_pressed, **button_style)
    button1.pack(pady=8)

    # Text Label for compression details
    defaultText = "Compression details will appear here."
    text_label = tk.Label(root, text=defaultText, **label_style2)
    text_label.pack(pady=8)

    # Textbox Label
    textbox_label1 = tk.Label(root, text="Huffman Codes:", **label_style2)
    textbox_label1.pack(pady=8)
    
    # Textbox 1 (Read-only)
    textbox1 = tk.Text(root, height=4, width=40, **textbox_style)
    textbox1.pack(pady=8)
    textbox1.insert(tk.END, "Huffman Codes...")
    textbox1.config(state=tk.DISABLED)

    # Button 2
    button2 = tk.Button(root, text="Decompress File", command=button_two_pressed, **button_style)
    button2.pack(pady=8)

    # Textbox Label
    textbox_label2 = tk.Label(root, text="Decoded Text:", **label_style2)
    textbox_label2.pack(pady=5)
    
    # Textbox 2 (Read-only)
    textbox2 = tk.Text(root, height=4, width=40, **textbox_style)
    textbox2.pack(pady=8)
    textbox2.insert(tk.END, "Decoded Text...")
    textbox2.config(state=tk.DISABLED)


    root.mainloop()

if __name__ == "__main__":
    main()
