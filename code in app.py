import tkinter as tk
from tkinter import scrolledtext, messagebox

class MessageEncoderDecoderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secret Message App")
        
        # Set the background color for the main window
        self.root.configure(bg="#f0f8ff")  # Light blue background

        # Create the UI components
        self.create_widgets()

        # Initialize history list
        self.history = []

    def create_widgets(self):
        # Label for encoding
        self.encode_label = tk.Label(self.root, text="Enter a message to encode:", bg="#f0f8ff", fg="#000080")  # Dark blue text
        self.encode_label.pack(pady=10)

        # Text entry for the input message to encode (reduced width)
        self.encode_input = tk.Entry(self.root, width=46, bg="#ffffff", fg="#000000")  # White background and black text
        self.encode_input.pack(pady=10)

        # Button for encoding
        self.encode_button = tk.Button(self.root, text="Encode Message", command=self.encode_message, bg="#4CAF50", fg="#ffffff")  # Green button
        self.encode_button.pack(pady=5)

        # Output box for encoded message (matching width)
        self.encode_output = scrolledtext.ScrolledText(self.root, width=46, height=5, wrap=tk.WORD, bg="#e6f7ff", fg="#000000")  # Light blue background for output
        self.encode_output.pack(pady=10)

        # Label for decoding
        self.decode_label = tk.Label(self.root, text="Enter a binary message to decode:", bg="#f0f8ff", fg="#000080")  # Dark blue text
        self.decode_label.pack(pady=10)

        # Text entry for the input binary message to decode (reduced width)
        self.decode_input = tk.Entry(self.root, width=46, bg="#ffffff", fg="#000000")  # White background and black text
        self.decode_input.pack(pady=10)

        # Button for decoding
        self.decode_button = tk.Button(self.root, text="Decode Binary Message", command=self.decode_message, bg="#4CAF50", fg="#ffffff")  # Green button
        self.decode_button.pack(pady=5)

        # Output box for decoded message (matching width)
        self.decode_output = scrolledtext.ScrolledText(self.root, width=46, height=5, wrap=tk.WORD, bg="#e6f7ff", fg="#000000")  # Light blue background for output
        self.decode_output.pack(pady=10)

        # Button to clear all fields
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_fields, bg="#ff9800", fg="#ffffff")  # Orange button
        self.clear_button.pack(pady=5)

        # Button to show history
        self.history_button = tk.Button(self.root, text="History", command=self.show_history, bg="#2196F3", fg="#ffffff")  # Blue button
        self.history_button.pack(pady=5)

        # Button to exit the application
        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_application, bg="#f44336", fg="#ffffff")  # Red button
        self.exit_button.pack(pady=20)

    def string_to_binary(self, message):
        """Convert a string message to binary."""
        binary_message = ''.join(format(ord(char), '08b') for char in message)
        return binary_message

    def binary_to_string(self, binary_message):
        """Convert a binary message back to a string."""
        # Split the binary message into chunks of 8 bits
        chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
        # Convert each chunk from binary to the corresponding character
        decoded_message = ''.join(chr(int(char, 2)) for char in chars)
        return decoded_message

    def encode_message(self):
        original_message = self.encode_input.get()
        if original_message:
            encoded_message = self.string_to_binary(original_message)
            self.encode_output.delete(1.0, tk.END)  # Clear previous output
            self.encode_output.insert(tk.END, f"Original Message: {original_message}\nEncoded Binary Message: { encoded_message}")
            # Store the history
            self.history.append(f"Encoded: {original_message} -> {encoded_message}")
        else:
            self.encode_output.delete(1.0, tk.END)
            self.encode_output.insert(tk.END, "Please enter a message to encode.")

    def decode_message(self):
        binary_message = self.decode_input.get()
        if binary_message:
            try:
                decoded_message = self.binary_to_string(binary_message)
                self.decode_output.delete(1.0, tk.END)  # Clear previous output
                self.decode_output.insert(tk.END, f"Decoded Message: {decoded_message}")
                # Store the history
                self.history.append(f"Decoded: {binary_message} -> {decoded_message}")
            except ValueError:
                self.decode_output.delete(1.0, tk.END)
                self.decode_output.insert(tk.END, "Invalid binary message. Please ensure it contains only 0s and 1s and is a multiple of 8 bits.")
        else:
            self.decode_output.delete(1.0, tk.END)
            self.decode_output.insert(tk.END, "Please enter a binary message to decode.")

    def clear_fields(self):
        """Clear all input and output fields."""
        self.encode_input.delete(0, tk.END)
        self.encode_output.delete(1.0, tk.END)
        self.decode_input.delete(0, tk.END)
        self.decode_output.delete(1.0, tk.END)

    def show_history(self):
        """Show the history of messages in a new window."""
        history_window = tk.Toplevel(self.root)
        history_window.title("Message History")
        history_window.configure(bg="#f0f8ff")

        history_text = scrolledtext.ScrolledText(history_window, width=60, height=20, bg="#e6f7ff", fg="#000000")
        history_text.pack(pady=10)

        if self.history:
            history_text.insert(tk.END, "\n".join(self.history))
        else:
            history_text.insert(tk.END, "No history available.")

        close_button = tk.Button(history_window, text="Close", command=history_window.destroy, bg="#f44336", fg="#ffffff")
        close_button.pack(pady=5)

    def exit_application(self):
        """Exit the application smoothly."""
        self.root.destroy()  # Destroy the main window and exit the application

if __name__ == "__main__":
    root = tk.Tk()
    app = MessageEncoderDecoderApp(root)
    root.mainloop()
