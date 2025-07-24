import tkinter as tk
from tkinter import filedialog, messagebox
from stego import encode_image, decode_image

def create_gui():
    def select_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            file_label.config(text=file_path)

    def encode():
        image_path = file_label.cget("text")
        secret_message = message_entry.get()
        if not secret_message:
            messagebox.showwarning("Warning", "Please enter a secret message.")
            return
        if image_path == "No file selected":
            messagebox.showwarning("Warning", "Please select an image.")
            return

        output_path = image_path.rsplit(".", 1)[0] + "_encoded.png"
        try:
            encode_image(image_path, output_path, secret_message)
            messagebox.showinfo("Success", f"Image saved as {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to encode image.\n{e}")

    def decode():
        image_path = file_label.cget("text")
        if image_path == "No file selected":
            messagebox.showwarning("Warning", "Please select an image first.")
            return

        try:
            decoded_msg = decode_image(image_path)
            if decoded_msg:
                decoded_label.config(text=f"Decoded Message: {decoded_msg}")
            else:
                decoded_label.config(text="No hidden message found.")
        except Exception as e:
            decoded_label.config(text="Error decoding image.")
            print(e)

    def reset():
        file_label.config(text="No file selected")
        message_entry.delete(0, tk.END)
        decoded_label.config(text="Decoded Message will appear here.")

    root = tk.Tk()
    root.title("Image Steganography Tool")
    root.geometry("500x400")

    tk.Label(root, text="Image Steganography", font=("Cochin", 18, "bold")).pack(pady=10)

    tk.Button(root, text="Select Image", command=select_file).pack()
    file_label = tk.Label(root, text="No file selected", wraplength=400)
    file_label.pack(pady=5)

    tk.Label(root, text="Secret Message:").pack()
    message_entry = tk.Entry(root, width=50)
    message_entry.pack(pady=5)

    tk.Button(root, text="Encode", command=encode).pack(pady=5)
    tk.Button(root, text="Decode", command=decode).pack(pady=5)
    tk.Button(root, text="Reset", command=reset).pack(pady=5)

    decoded_label = tk.Label(root, text="Decoded Message will appear here.", wraplength=400)
    decoded_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
