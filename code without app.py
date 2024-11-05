class MessageEncoderDecoder:
    def __init__(self):
        pass

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

    def run(self):
        """Run the application."""
        while True:
            print("\nMenu:")
            print("1. Encode a message")
            print("2. Decode a binary message")
            print("3. Exit")

            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                original_message = input("Enter a message to encode: ")
                encoded_message = self.string_to_binary(original_message)
                print(f"Original Message: {original_message}")
                print(f"Encoded Binary Message: {encoded_message}")

            elif choice == '2':
                binary_message = input("Enter a binary message to decode: ")
                try:
                    decoded_message = self.binary_to_string(binary_message)
                    print(f"Decoded Message: {decoded_message}")
                except ValueError:
                    print("Invalid binary message. Please ensure it contains only 0s and 1s and is a multiple of 8 bits.")

            elif choice == '3':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    app = MessageEncoderDecoder()
    app.run()
