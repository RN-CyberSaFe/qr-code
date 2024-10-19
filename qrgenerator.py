import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk

def generate_qr_code():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        tk_img = ImageTk.PhotoImage(img)
        qr_label.config(image=tk_img)
        qr_label.image = tk_img
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    root.title("QR Code Generator")
    root.geometry("300x200")
    root.configure(bg="#f0f0f0")

    url_label = tk.Label(root, text="Enter URL:", bg="#f0f0f0")
    url_label.pack(pady=10)

    global url_entry
    url_entry = tk.Entry(root)
    url_entry.pack()

    generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code, bg="#007bff", fg="white")
    generate_button.pack(pady=10)

    global qr_label
    qr_label = tk.Label(root, bg="#f0f0f0")
    qr_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
