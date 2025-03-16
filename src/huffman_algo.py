import heapq # Heap Queue for priority queue operations
import tkinter as tk
from tkinter import filedialog
from bitarray import bitarray

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
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

def save_to_bitarray_binary(encoded_text, file_path):
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
    if trigger == "encode":
        file_path = open_file_dialog()
    elif trigger == "decode":
        file_path = filePath2

    text = read_file_as_ascii(file_path)

    freq_map = {char: text.count(char) for char in set(text)}

    root = build_huffman_tree(freq_map)
    codes = build_codes(root)

    encoded_text = "".join(codes[char] for char in text)

    # print("Original Text: ", text)
    # print("Huffman Codes: ", codes)
    # print("Encoded Text: ", encoded_text)

    save_location = "compressed.bin"
    save_to_bitarray_binary(encoded_text, save_location)

    file_path = "compressed.bin"  # Specify the binary file path

    decoded_result = huffman_decode_from_binary_file(file_path, codes)

    # if decoded_result is not None:
    #     print("Decoded Text: ", decoded_result)
    print("File Path Test 3 ", file_path)
    if trigger == "encode":
        return codes, text, encoded_text, file_path
    elif trigger == "decode":
        return decoded_result
    else:
        print("Error")


