from stego import encode_image, decode_image

input_img = "../assets/input_image.png"
output_img = "../assets/encoded_image.png"
secret = "This is a secret!"

print("[*] Encoding message...")
success = encode_image(input_img, output_img, secret)
if success:
    print("Message encoded.")

print("[*] Decoding message...")
decoded = decode_image(output_img)
print("Decoded message:", decoded)
