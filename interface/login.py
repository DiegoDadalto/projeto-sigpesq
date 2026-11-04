import tkinter as tk
from tkinter import ttk

# JANELA DA APLICAÇÃO
janela = tk.Tk()
janela.title("SigPesq")
janela.geometry("1280x720")

# FUNDO ROXO (BEM-VINDE)
fundoTagline = tk.Frame(
    janela,
    width=600,
    height=720,
    bg="MediumOrchid1",
    padx=10,
    pady=10
)
tagline = tk.Frame(
    fundoTagline,
    padx=10,
    pady=10,
    bg=fundoTagline.cget("bg")
)


# TAGLINE
taglineTitulo = tk.Label(
    tagline,
    text="BEM-VINDE!",
    font=("Montserrat", 48, "bold"),
    bg=fundoTagline.cget("bg")
)
separador = tk.Frame(
    tagline,
    height=2,
    bg="#000000"
)
taglineDesc = tk.Label(
    tagline,
    text="Faça o cadastro para continuar",
    font=("Montserrat", 24),
    bg=fundoTagline.cget("bg")
)


# FORMULÁRIO
fundoCampos = tk.Frame(
    janela,
    width=680,
    height=720,
    bg="misty rose"
)
camposForm = tk.Frame(
    fundoCampos,
    padx=10,
    pady=10,
    bg=fundoCampos.cget("bg")
)

# CRIE UMA CONTA!
tituloForm = tk.Label(
    camposForm,
    padx=10,
    pady=10,
    bg=fundoCampos.cget("bg"),
    text="Crie uma conta:",
    font=("Montserrat", 28)
)


# CAMPO: 






# ==================== EXIBIÇÃO ====================


# EXIBIÇÃO - PARTE ROXA
fundoTagline.pack_propagate(False)
fundoTagline.pack(side="left")

tagline.pack(
    expand=True,
    anchor="center"
)

taglineTitulo.pack()
separador.pack(fill="x")
taglineDesc.pack()


# EXIBIÇÃO - PARTE DO FORMULÁRIO
fundoCampos.pack_propagate(False)
fundoCampos.pack(
    side="right",
)

camposForm.pack(
    expand=True,
    anchor="center"
)
tituloForm.pack()

# FIM
janela.mainloop()