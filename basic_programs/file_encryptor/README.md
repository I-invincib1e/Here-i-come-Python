# File Encryptor/Decryptor (XOR Cipher)

Encrypt and decrypt files using a simple XOR cipher for learning cryptography concepts.

## How It Works

- Reads the input file as raw bytes
- Creates a repeating key stream from the password
- XORs each byte with corresponding key byte
- Writes encrypted/decrypted result to output file
- Same function works for both encrypt/decrypt (XOR symmetry)

## Example

```text
Enter input file path: secret.txt
Enter output file path: secret.enc
Enter encryption key: pass123
File processed successfully: secret.enc
```

## Industry Applications

**Where encryption patterns are used in the real world:**

- **File Security**: Commercial encryption tools like VeraCrypt, BitLocker
- **Network Security**: TLS/SSL protocols for secure web communication
- **Database Security**: Transparent Data Encryption (TDE) in SQL Server, Oracle
- **Cloud Storage**: S3 server-side encryption, Azure Storage encryption

**Learning Connection:** This demonstrates the foundation of symmetric encryption used in VPNs, encrypted databases, and secure file transfer protocols.

## Internals

- `xor_encrypt_decrypt()`: Core function performing byte-by-byte XOR with repeating key
- XOR is symmetric: encrypt(decrypt(data)) = decrypt(encrypt(data)) = original data
- Key repetition: Short passwords create cycling key patterns
