# File Encryptor/Decryptor

Encrypt and decrypt files using a simple XOR cipher (for learning only).

## How It Works

- Reads the input file as bytes
- Builds a repeating key stream from the password
- XORs each byte with the key stream to produce output bytes
- Writes the result to the output file

## Example

```text
Enter input file path: secret.txt
Enter output file path: secret.enc
Enter encryption key: pass123
File processed successfully: secret.enc
```

## Internals

- `xor_encrypt_decrypt(data, key)` does byte-by-byte XOR with repeating key
- Same function decrypts encrypted data (XOR is symmetric)

## Notes

- Not secure for real data; use proper crypto libraries in practice
