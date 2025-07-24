from PIL import Image

def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    message = ''
    for char in chars:
        if char == '11111111':
            break
        message += chr(int(char, 2))
    return message

def encode_image(input_path, output_path, secret_message):
    image = Image.open(input_path)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    binary_message = text_to_binary(secret_message) + '1111111111111110'  # end marker
    binary_index = 0

    pixels = list(image.getdata())
    new_pixels = []

    for pixel in pixels:
        r, g, b = pixel
        if binary_index < len(binary_message):
            r = (r & ~1) | int(binary_message[binary_index])
            binary_index += 1
        if binary_index < len(binary_message):
            g = (g & ~1) | int(binary_message[binary_index])
            binary_index += 1
        if binary_index < len(binary_message):
            b = (b & ~1) | int(binary_message[binary_index])
            binary_index += 1
        new_pixels.append((r, g, b))

    image.putdata(new_pixels)
    image.save(output_path)
    return True

def decode_image(image_path):
    image = Image.open(image_path)
    if image.mode != 'RGB':
        image = image.convert('RGB')

    pixels = list(image.getdata())
    binary_data = ''

    for pixel in pixels:
        for color in pixel[:3]:  # r, g, b
            binary_data += str(color & 1)

    end_marker = '1111111111111110'
    end_index = binary_data.find(end_marker)
    if end_index != -1:
        binary_data = binary_data[:end_index]
    return binary_to_text(binary_data)
