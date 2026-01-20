from tkinter import ttk
from tkinter import ttk

def aplicar_estilo():
    style = ttk.Style()
    style.theme_use("default")

    style.configure(
        "Custom.Treeview",
        background="#09090b",
        foreground="white",
        fieldbackground="09090b",
        font=("Segoe UI", 11),
        rowheight=30
    )

    style.configure(
        "Custom.Treeview.Heading",
        background="#71717a",
        foreground="white",
        font=("Segoe UI", 11)
    )

    style.map(
        "Custom.Treeview",
        background=[("selected", "#a855f7")],
        foreground=[("selected", "white")]
    )

