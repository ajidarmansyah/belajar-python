import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
# init tkinter GUI

window = tk.Tk()
window.geometry("300x300")
window.title("My Appication")
window.configure(bg="white")

# Variable & Fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Selamat malam"
    showinfo(title="Sey Hello", message=pesan)


# main frame
main_frame = ttk.Frame(window)
main_frame.pack(padx=10,pady=10,fill='x',expand=True)

# titel nama depan
titel_nama_depan = ttk.Label(main_frame, text="Nama Depan: ")
titel_nama_depan.pack(padx=10,fill='x',expand=True)

# input nama depan
input_nama_depan = ttk.Entry(main_frame,textvariable=NAMA_DEPAN)
input_nama_depan.pack(padx=5,pady=10,fill='x',expand=True)

# titel nama belakang
titel_nama_belakang = ttk.Label(main_frame, text="Nama belakang: ")
titel_nama_belakang.pack(padx=10,fill='x',expand=True)

# input nama belakang
input_nama_belakang = ttk.Entry(main_frame,textvariable=NAMA_BELAKANG)
input_nama_belakang.pack(padx=5,pady=10,fill='x',expand=True)

# tombol
tombol = ttk.Button(main_frame, text="Sapa!", command=tombol_click)
tombol.pack(padx=10,pady=10,fill='x',expand=True)


window.mainloop()