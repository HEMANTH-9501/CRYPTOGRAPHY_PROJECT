import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox


# Encryption function
def encrypt_image(path, key):
    try:
        with open(path, 'rb') as fin:
            image = bytearray(fin.read())

        for index, values in enumerate(image):
            image[index] = values ^ key

        with open(path, 'wb') as fout:
            fout.write(image)
        messagebox.showinfo("Success", "Encryption Done!")
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {e}")


# Decryption function
def decrypt_image(path, key):
    try:
        with open(path, 'rb') as fin:
            image = bytearray(fin.read())

        for index, values in enumerate(image):
            image[index] = values ^ key

        with open(path, 'wb') as fout:
            fout.write(image)
        messagebox.showinfo("Success", "Decryption Done!")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")


# GUI Application
class ImageCryptoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption/Decryption")

        # File path label and entry
        self.file_path_label = Label(root, text="File Path:")
        self.file_path_label.grid(row=0, column=0, padx=10, pady=10)
        self.file_path_entry = Entry(root, width=40)
        self.file_path_entry.grid(row=0, column=1, padx=10, pady=10)

        # Browse button
        self.browse_button = Button(root, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)

        # Key label and entry
        self.key_label = Label(root, text="Key:")
        self.key_label.grid(row=1, column=0, padx=10, pady=10)
        self.key_entry = Entry(root, width=20)
        self.key_entry.grid(row=1, column=1, padx=10, pady=10)

        # Encrypt and Decrypt buttons
        self.encrypt_button = Button(root, text="Encrypt", command=self.encrypt_action)
        self.encrypt_button.grid(row=2, column=0, padx=10, pady=10)

        self.decrypt_button = Button(root, text="Decrypt", command=self.decrypt_action)
        self.decrypt_button.grid(row=2, column=1, padx=10, pady=10)

        # Exit button
        self.exit_button = Button(root, text="Exit", command=root.quit)
        self.exit_button.grid(row=2, column=2, padx=10, pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff"), ("All Files", "*.*")]
        )
        self.file_path_entry.delete(0, 'end')
        self.file_path_entry.insert(0, file_path)

    def encrypt_action(self):
        path = self.file_path_entry.get()
        key = self.key_entry.get()

        if not os.path.exists(path):
            messagebox.showerror("Error", "File does not exist!")
            return
        if not key.isdigit():
            messagebox.showerror("Error", "Key must be a numeric value!")
            return

        encrypt_image(path, int(key))

    def decrypt_action(self):
        path = self.file_path_entry.get()
        key = self.key_entry.get()

        if not os.path.exists(path):
            messagebox.showerror("Error", "File does not exist!")
            return
        if not key.isdigit():
            messagebox.showerror("Error", "Key must be a numeric value!")
            return

        decrypt_image(path, int(key))


# Run the application
if __name__ == "__main__":
    root = Tk()
    app = ImageCryptoApp(root)
    root.mainloop()
