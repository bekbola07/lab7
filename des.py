
from Crypto.Cipher import AES
from Crypto.Util. Padding import unpad
with open("shifrlangan.bin", "rb") as f:
    iv = f.read(16)
    ciphertext = f.read()
cipher = AES.new(key, AES. MODE_CBC, iv)
plaintext = unpad (cipher.decrypt (ciphertext), AES.block_size)
with open("yechilgan.txt", "wb") as f:
    f.write(plaintext)
print("Fayl muvaffaqiyatli shifrdan yechildi.")