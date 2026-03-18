import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
import base64

# Ana pencere
window = tk.Tk()
window.title("Secret Notes")
window.minsize(width=400, height=800)

# Görsel
img = Image.open("Top Secret Logo.png")
tk_img = ImageTk.PhotoImage(img)
Gorsel = tk.Label(window, image=tk_img)
Gorsel.pack()

# Başlık
tk.Label(window, text="Enter Your Title", fg="black", padx=10, pady=10).pack()
entry_baslik = tk.Entry(window, width=40)
entry_baslik.pack()

# Sır
tk.Label(window, text="Enter Your Secret", fg="black", padx=10, pady=10).pack()
text_sir = tk.Text(window, width=30, height=15)
text_sir.pack()

# Anahtar
tk.Label(window, text="Enter Master Key", fg="black", padx=10, pady=10).pack()
entry_key = tk.Entry(window, width=40)
entry_key.pack()

# Kaydet ve şifrele
def Kaydetme_ve_Şifreleme():
    baslik = entry_baslik.get().strip()
    sir = text_sir.get("1.0", "end").strip()
    anahtar = entry_key.get().strip()

    if not baslik or not sir or not anahtar:
        messagebox.showerror("Hata", "Lütfen tüm alanları doldurun!")
        return

    # Fernet key oluştur
    key_bytes = base64.urlsafe_b64encode(anahtar.encode().ljust(32)[:32])
    fernet = Fernet(key_bytes)

    # Sır şifrele
    sifreli_sir_bytes = fernet.encrypt(sir.encode())
    sifreli_sir_str = sifreli_sir_bytes.decode()

    # Dosyaya yaz: sadece başlık + şifreli sır
    with open("Secret notes.txt", "a") as f:
        f.write(baslik + "\n")
        f.write(sifreli_sir_str + "\n")

    # Entry ve Text’leri temizle
    entry_baslik.delete(0, tk.END)
    text_sir.delete("1.0", "end")
    entry_key.delete(0, tk.END)

    messagebox.showinfo("Başarılı", "Başlık ve şifreli sır kaydedildi!")

# Şifreyi çöz
def cozum():
    # Text’ten şifreli sır al
    sifreli_sir = text_sir.get("1.0", "end").strip()
    anahtar = entry_key.get().strip()

    if not sifreli_sir or not anahtar:
        messagebox.showerror("Hata", "Lütfen hem şifreli sır hem anahtarı girin!")
        return

    try:
        # Fernet objesi oluştur
        key_bytes = base64.urlsafe_b64encode(anahtar.encode().ljust(32)[:32])
        fernet = Fernet(key_bytes)

        # Şifre çöz
        orijinal_sir = fernet.decrypt(sifreli_sir.encode()).decode()
        text_sir.delete("1.0", "end")
        text_sir.insert("1.0", orijinal_sir)
        messagebox.showinfo("Başarılı", "Sır çözüldü!")
    except:
        messagebox.showerror("Hata", "Anahtar yanlış veya şifreli sır çözülmedi!")

# Butonlar
tk.Button(window, text="Save & Encrypt", command=Kaydetme_ve_Şifreleme, padx=10, pady=10).pack(pady=5)
tk.Button(window, text="Decrypt", command=cozum, padx=10, pady=10).pack(pady=5)

window.mainloop()