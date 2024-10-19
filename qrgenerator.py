import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import qrcode
from PIL import ImageTk, Image, ImageFilter
import os

# Create the motion blur effect for QR code
def apply_motion_blur(image):
    return image.filter(ImageFilter.GaussianBlur(radius=2))

def generate_qr_code():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)  # Adjusted box_size for balance
        qr.add_data(url)
        qr.make(fit=True)
        
        # Create the image and convert to RGB
        img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

        # Resize for better visibility
        img = img.resize((300, 300), Image.LANCZOS)

        # Save the QR code image directly on the Desktop
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "generated_qr_code.png")
        img.save(desktop_path, "PNG", quality=95)  # Save as PNG file with high quality

        # Optionally apply motion blur
        blurred_img = apply_motion_blur(img)
        tk_img = ImageTk.PhotoImage(blurred_img)

        qr_label.config(image=tk_img)
        qr_label.image = tk_img

        # Update message below QR code
        message_label.config(text="It is blurred, so we have saved the QR code on your Desktop.")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Button hover animation
def on_enter(e):
    generate_button.config(bg="#ff7f50", fg="white")

def on_leave(e):
    generate_button.config(bg="#ff4500", fg="white")

def main():
    root = tk.Tk()
    root.title("QR CODE GENERATOR _ARYAN-JOSHI")
    root.geometry("450x550")

    # Load and set the background image
    try:
        bg_image = Image.open("pictureofnepal.jfif")  # Image should be in the same directory as this script
        bg_image = bg_image.resize((450, 550), Image.LANCZOS)  # Resize to match window size
        bg_image_tk = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(root, image=bg_image_tk)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except FileNotFoundError:
        messagebox.showerror("Error", "Background image not found. Make sure 'pictureofnepal.jfif' is in the same directory.")

    # Add content over the image
    url_label = tk.Label(root, text="Enter URL:", font=("Helvetica", 14), fg="white", bg="#000000", padx=10, pady=5)
    url_label.place(relx=0.5, y=50, anchor="center")  # Center the label

    # Make URL entry larger and more attractive
    global url_entry
    style = ttk.Style()
    style.configure("TEntry", padding=10, font=("Helvetica", 14))

    url_entry = ttk.Entry(root, width=30, style="TEntry")
    url_entry.place(relx=0.5, y=100, anchor="center")  # Center the entry

    # Add a button with hover effect
    global generate_button
    generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code, bg="#ff4500", fg="white", font=("Helvetica", 14), relief="flat", padx=10, pady=5)
    generate_button.place(relx=0.5, y=160, anchor="center")  # Center the button

    generate_button.bind("<Enter>", on_enter)
    generate_button.bind("<Leave>", on_leave)

    # Placeholder for QR code
    global qr_label
    qr_label = tk.Label(root, bg="#ff8c00")  # Adjusted for better visibility
    qr_label.place(relx=0.5, y=400, anchor="center")  # Center the QR code

    # Message label directly below the QR code (adjusted position)
    global message_label
    message_label = tk.Label(root, text="", font=("Helvetica", 12), fg="white", bg="#111111")
    message_label.place(relx=0.5, y=220, anchor="center")  # Center the message slightly higher

    root.mainloop()

if __name__ == "__main__":
    main()
