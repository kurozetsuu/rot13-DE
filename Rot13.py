import os
import time
os.system("clear")
print"""
		---------------------------------------------
		-         ROT13 Encryption/Decryption       -
		-              By : Ayoub Ourass            -
		-  https://www.facebook.com/ayoub.flack.90  -
		---------------------------------------------                                                        
		"""
from string import maketrans
print("[1] Coder")
print("[2] Decoder")
print("[3] Exit")
choice = input("Enter Your Choice :  ")
if choice == 1:
    def rot13_cipher(text):
        rot13_cipher = maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
        return text.translate(rot13_cipher)
    plaintext = raw_input("Enter Your Text Here : ")
    ciphertext = rot13_cipher(plaintext)
    print "Encrypting ...."
    time.sleep(1)
    print"Encryption :", ciphertext

if choice == 2:
	def rot13_cipher(text):
		rot13_cipher = maketrans("NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
		return text.translate(rot13_cipher)
	plaintext = raw_input("Enter Your Text Here : ")
	ciphertext = rot13_cipher(plaintext)
	print("Decrypting ....")
	time.sleep(1)
	print"Decryption :",ciphertext
if choice == 3:
	os.system("exit")

    
