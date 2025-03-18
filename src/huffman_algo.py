import heapq # Heap Queue for priority queue operations
import tkinter as tk
from tkinter import filedialog
from bitarray import bitarray
import os


def show_popup():
    popup = tk.Toplevel()
    popup.title("")
    popup.geometry("300x150")
    popup.configure(bg="#4c789e") 

    # Message Label
    if encodeTrigger == True:
        label = tk.Label(popup, text="✅ Compressed file saved as 'compressed.bin'.", bg="#4c789e", fg="#ECF0F1",  font=("Courier New", 10, "bold"), wraplength=280)
    elif decodeTrigger == True:
        label = tk.Label(popup, text="Decoding successful! Original text matches.", bg="#4c789e", fg="#ECF0F1",  font=("Courier New", 10, "bold"), wraplength=280)
    label.pack(pady=15, padx=15)

    # Okay Button
    okay_button = tk.Button(popup, text="OK", command=popup.destroy, bg="#27AE60", fg="white", font=("Courier New", 10, "bold"),relief="flat",padx=10, pady=5)
    okay_button.pack(pady=10)

    popup.after(10, lambda: None)

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    print("Filepath from open file dialog func", file_path)
    return file_path

def read_file_as_ascii(file_path):
    try:
        with open(file_path, 'r', encoding='ascii', errors='ignore') as file:
            content = file.read()
        return content
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Huffman Start
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Step 2: Build Huffman Tree
def build_huffman_tree(freq_map):
    heap = [HuffmanNode(char,freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = HuffmanNode(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        heapq.heappush(heap, new_node)
    return heap[0]

# Step 3: Generate / Assign Huffman Codes
def build_codes(node, prefix = "", code_map = {}):
    if node is None:
        return
    if node.char is not None:
        code_map[node.char] = prefix
    build_codes(node.left, prefix + "0", code_map) # left child (0)
    build_codes(node.right, prefix + "1", code_map) # right child (1)

    return code_map

# # Step 4: Get user input and compute Huffman Encoding
# file_path = open_file_dialog()
# text = read_file_as_ascii(file_path)

# freq_map = {char: text.count(char) for char in set(text)}

# root = build_huffman_tree(freq_map)
# codes = build_codes(root)

# encoded_text = "".join(codes[char] for char in text)

# print("Original Text: ", text)
# print("Huffman Codes: ", codes)
# print("Encoded Text: ", encoded_text)

def save_to_bitarray_binary(encoded_text, file_path, file_path_og):
    """Convert binary-encoded text to a bitarray and save it to a binary file."""
    try:
        # Convert binary-encoded text to a bitarray
        bit_array = bitarray(encoded_text)  # Directly creates a bitarray from the binary string

        # Save the bitarray to a binary file
        with open(file_path, 'wb') as binary_file:
            bit_array.tofile(binary_file)

        print(f"Bitarray successfully saved to binary file: {file_path}")
    except Exception as e:
        print(f"Error converting to bitarray or saving: {e}")

# save_location = "compressed.bin"
# save_to_bitarray_binary(encoded_text, save_location)

def read_binary_file(file_path):
    try:
        bit_array = bitarray()
        with open(file_path, 'rb') as binary_file:
            bit_array.fromfile(binary_file)
        return bit_array
    except Exception as e:
        print(f"Error reading binary file: {e}")
        return None

def huffman_decode_from_binary_file(file_path, huffman_codes):
    # Read the binary file into a bitarray
    bit_array = read_binary_file(file_path)
    if bit_array is None:
        return None

    # Convert bitarray to a string of 0s and 1s
    encoded_text = bit_array.to01()  # Convert the bitarray to a binary string

    # Decode using the existing decoding logic
    reverse_codes = {code: char for char, code in huffman_codes.items()}
    decoded_text = ""
    temp_code = ""

    for bit in encoded_text:
        temp_code += bit
        if temp_code in reverse_codes:
            decoded_text += reverse_codes[temp_code]
            temp_code = ""
    
    return decoded_text

# # Example usage
# file_path = "compressed.bin"  # Specify the binary file path

# decoded_result = huffman_decode_from_binary_file(file_path, codes)

# if decoded_result is not None:
#     print("Decoded Text: ", decoded_result)


def encodeAndDecode(trigger, filePath2):
    # Step 4: Get user input and compute Huffman Encoding
    global encodeTrigger, decodeTrigger
    if trigger == "encode":
        file_path = open_file_dialog()
        encodeTrigger = True
        decodeTrigger = False
    elif trigger == "decode":
        file_path = filePath2
        decodeTrigger = True
        encodeTrigger = False

    text = read_file_as_ascii(file_path)

    freq_map = {char: text.count(char) for char in set(text)}

    root = build_huffman_tree(freq_map)
    codes = build_codes(root)

    encoded_text = "".join(codes[char] for char in text)

    # print("Original Text: ", text)
    # print("Huffman Codes: ", codes)
    # print("Encoded Text: ", encoded_text)

    save_location = "compressed.bin"
    save_to_bitarray_binary(encoded_text, save_location, file_path)
    file_path_og = file_path
    file_path = "compressed.bin"  # Specify the binary file path

    # Get byte sizes of original and compressed files
    #global original_file_size, compressed_file_size
    original_file_size = os.path.getsize(file_path_og)  # Assuming file_path_og is the path to the original file
    compressed_file_size = os.path.getsize(file_path)   # Path to the compressed file
        
    print(f"Original file size: {original_file_size} bytes")
    print(f"Compressed file size: {compressed_file_size} bytes")

    decoded_result = huffman_decode_from_binary_file(file_path, codes)

    if text == decoded_result:
        show_popup()

    # if decoded_result is not None:
    #     print("Decoded Text: ", decoded_result)
    print("File Path Test 3 ", file_path)
    if trigger == "encode":
        return codes, text, encoded_text, file_path_og, original_file_size, compressed_file_size
    elif trigger == "decode":
        return decoded_result
    else:
        print("Error")

# def get_byte_sizes():
#     return original_file_size, compressed_file_size

