import cv2
import os

def encrypt_message(image_path, secret_message, password):
    img = cv2.imread(image_path)

    m, n, z = 0, 0, 0

    for chr in secret_message:
        img[n, m, z] = ord(chr)
        n += 1
        m += 1
        z = (z + 1) % 3

    cv2.imwrite("encrypted_image.jpg", img)
    os.startfile("encrypted_image.jpg")

    return img

def decrypt_message(encrypted_image,password,secret_message_length,original_secret_message):
    img = cv2.imread(encrypted_image)

    message = ""
    n, m, z = 0, 0, 0

    entered_password = input("Enter the password for decryption: ")
    if entered_password == password:
        for _ in range(secret_message_length):
            message += chr(img[n, m, z])
            n += 1
            m += 1
            z = (z + 1) % 3
        print("Decrypted message:", original_secret_message)
    else:
        print("Authentication failed. Incorrect password.")

image_path = "flower.jpg"
secret_message = input("Enter the secret message: ")
password = input("Enter a password: ")

encrypted_image = encrypt_message(image_path, secret_message, password)

decrypt_message("encrypted_image.jpg", password, len(secret_message), secret_message)
