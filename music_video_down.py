import tkinter as tk
from pytube import YouTube

windows = tk.Tk()
windows.title("YT Downloader")
windows.geometry("300x250")
windows.configure(bg="#141414")
windows.minsize(400, 300)

def url():
    print(str(urltext.get()))
    youtubeObject = YouTube(str(urltext.get()))
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        on = tk.Tk()
        on.title(" ")
        on.geometry("300x250")
        on.configure(bg="#141414")
        on.minsize(400, 300)
        on.attributes('-topmost', True)

        youtubeObject.download()
        tk.Label(on,
                 text="Descarga completada").pack()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

tk.Label(
    windows,
    text="Download YT",
    font=("Roboto", 20, "bold"),
    bg="#141414",
    fg="white"
).pack(pady=10, padx=10)

tk.Label(
    windows,
    text="Ingrese la url (youtube): ",
    font=("Roboto", 14),
    bg="#141414",
    fg="white"
).pack(pady=20)

urltext = tk.Entry(
    windows,
    bg="#141414",
    fg="#fff"
)
urltext.pack(padx=10, pady=10) 

tk.Button(
    windows,
    text="Descargar",
    font=("Roboto", 12),
    bg="#141414",
    fg="#fff",
    command=url
).pack(padx=10, pady=10)

windows.mainloop()
