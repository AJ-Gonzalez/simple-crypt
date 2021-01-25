from simplecrypt import encrypt, decrypt
password='password1'
ciphertext = encrypt(password, 'my secret message')
print(type(ciphertext),str(ciphertext))
plaintext = decrypt(password, ciphertext)
print(plaintext.decode('utf-8'))
