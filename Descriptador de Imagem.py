import os
from cryptography.fernet import Fernet
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def decrypt_image(encrypted_image_path, output_image_path, key):
    # Abrir a imagem encriptada
    encrypted_img = Image.open(encrypted_image_path)

    # Converter a imagem para bytes
    img_bytes = encrypted_img.tobytes()

    # Inicializar o objeto Fernet com a chave fornecida
    fernet = Fernet(key)

    # Desencriptar os bytes da imagem
    decrypted_bytes = fernet.decrypt(img_bytes)

    # Criar uma nova imagem com os bytes desencriptados
    decrypted_img = Image.frombytes(encrypted_img.mode, encrypted_img.size, decrypted_bytes)

    # Salvar a imagem desencriptada
    decrypted_img.save(output_image_path)

    messagebox.showinfo("Success", "Imagem desencriptada e salva com sucesso!")

def browse_image():
    filename = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    entry_path.delete(0, tk.END)
    entry_path.insert(0, filename)

def decrypt():
    input_image_path = entry_path.get()
    if not os.path.exists(input_image_path):
        messagebox.showerror("Error", "Caminho da imagem inválido.")
        return
    
    output_image_path = "decrypted_image.jpg"

    # Carregar a chave salva
    with open("key.key", "rb") as key_file:
        key = key_file.read()

    decrypt_image(input_image_path, output_image_path, key)

# Criar a interface gráfica
root = tk.Tk()
root.title("Desencriptador de Imagens")

label_path = tk.Label(root, text="Caminho da imagem encriptada:")
label_path.grid(row=0, column=0, padx=5, pady=5)

entry_path = tk.Entry(root, width=40)
entry_path.grid(row=0, column=1, padx=5, pady=5)

button_browse = tk.Button(root, text="Procurar", command=browse_image)
button_browse.grid(row=0, column=2, padx=5, pady=5)

button_decrypt = tk.Button(root, text="Desencriptar", command=decrypt)
button_decrypt.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
