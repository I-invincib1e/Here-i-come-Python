#!/usr/bin/env python3
"""
File Encryptor/Decryptor - CLI
Simple XOR-based file encryption/decryption.
"""

import os

def xor_encrypt_decrypt(data, key):
    """Encrypt or decrypt data using XOR with a key."""
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def process_file(input_file, output_file, key):
    """Process a file with encryption/decryption."""
    try:
        with open(input_file, 'rb') as f:
            data = f.read()

        processed_data = xor_encrypt_decrypt(data, key.encode())

        with open(output_file, 'wb') as f:
            f.write(processed_data)

        print(f"File processed successfully: {output_file}")
        return True

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return False
    except Exception as e:
        print(f"Error processing file: {e}")
        return False

def main():
    print("File Encryptor/Decryptor")
    print("-" * 30)

    input_file = input("Enter input file path: ").strip()
    output_file = input("Enter output file path: ").strip()
    key = input("Enter encryption key: ").strip()

    if not input_file or not output_file or not key:
        print("Error: All fields are required.")
        return

    if process_file(input_file, output_file, key):
        print("\nNote: Use the same key to decrypt the file.")
        print("This is a simple XOR encryption - not suitable for sensitive data!")

if __name__ == "__main__":
    main()
