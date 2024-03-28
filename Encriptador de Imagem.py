from cryptography.fernet import Fernet
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def encrypt_image(input_image_path, output_image_path, key):
    # Abrir a imagem
    img = Image.open(input_image_path)

    # Converter a imagem para o modo RGB (sem canal alfa)
    img = img.convert("RGB")

    # Converter a imagem para bytes
    img_bytes = img.tobytes()

    # Inicializar o objeto Fernet com a chave fornecida
    fernet = Fernet(key)

    # Encriptar os bytes da imagem
    encrypted_bytes = fernet.encrypt(img_bytes)

    # Criar uma nova imagem com os bytes encriptados
    encrypted_img = Image.frombytes(img.mode, img.size, encrypted_bytes)

    # Salvar a imagem encriptada
    encrypted_img.save(output_image_path)

    messagebox.showinfo("Success", "Imagem encriptada e salva com sucesso!")

def browse_image():
    filename = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    entry_path.delete(0, tk.END)
    entry_path.insert(0, filename)

def encrypt():
    input_image_path = entry_path.get()
    if not os.path.exists(input_image_path):
        messagebox.showerror("Error", "Caminho da imagem inválido.")
        return
    
    output_image_path = "encrypted_image.jpg"

    key = Fernet.generate_key()

    encrypt_image(input_image_path, output_image_path, key)

    with open("key.key", "wb") as key_file:
        key_file.write(key)

    messagebox.showinfo("Success", "Chave de encriptação salva como 'key.key'.")

# Criar a interface gráfica
root = tk.Tk()
root.title("Encriptador de Imagens")

label_path = tk.Label(root, text="Caminho da imagem:")
label_path.grid(row=0, column=0, padx=5, pady=5)

entry_path = tk.Entry(root, width=40)
entry_path.grid(row=0, column=1, padx=5, pady=5)

button_browse = tk.Button(root, text="Procurar", command=browse_image)
button_browse.grid(row=0, column=2, padx=5, pady=5)

button_encrypt = tk.Button(root, text="Encriptar", command=encrypt)
button_encrypt.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
