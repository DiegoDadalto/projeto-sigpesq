import tkinter as tk
from tkinter import ttk
from pathlib import Path

PASTA_IMAGENS = Path(__file__).resolve().parent.parent / "imagens"

# JANELA DA APLICAÇÃO
janela = tk.Tk()
janela.title("SigPesq")
janela.geometry("1280x720")

# FUNDO ROXO (BEM-VINDE)
imagemFundo = tk.PhotoImage(file=PASTA_IMAGENS / "fundoTag.png")

fundoTagline = tk.Canvas(
    janela,
    width=600,
    height=720,
    highlightthickness=0
)

fundoTagline.create_image(
    0,
    0,
    image=imagemFundo,
    anchor="nw"
)

fundoTagline.create_text(
    300,
    280,
    text="BEM-VINDE!",
    font=("Montserrat", 48, "bold"),
    fill="white"
)

fundoTagline.create_line(
    100, 330,
    500, 330,
    fill="white",
    width=2
)

fundoTagline.create_text(
    300,
    370,
    text="Faça o cadastro para continuar",
    font=("Montserrat", 24),
    fill="white"
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


# CAMPOS DE ENTRADA DE INFORMAÇÕES

def criarCampo(hidden=""):
    if hidden == "hidden":
        nomeCampo = tk.Entry(
                camposForm,
                width=30,
                bg="white",
                fg="black",
                font=("Montserrat", 16),
                bd=2,
                show="●"
            )
    else:
        nomeCampo = tk.Entry(
            camposForm,
            width=30,
            bg="white",
            fg="black",
            font=("Montserrat", 16),
            bd=2
        )
    return nomeCampo

def placeholder(campo, texto):
    campo.insert(0, texto)
    campo.config(fg="gray")

    def remover(event):
        if campo.get() == texto:
            campo.delete(0, tk.END)
            campo.config(fg="black")

    def adicionar(event):
        if campo.get() == "":
            campo.insert(0, texto)
            campo.config(fg="gray")

    campo.bind("<FocusIn>", remover)
    campo.bind("<FocusOut>", adicionar)

def placeholderSenha(campo, texto):
    campo.insert(0, texto)
    campo.config(fg="gray", show="")

    def remover(event):
        if campo.get() == texto:
            campo.delete(0, tk.END)
            campo.config(fg="black", show="●")

    def adicionar(event):
        if campo.get() == "":
            campo.config(show="", fg="gray")
            campo.insert(0, texto)

    campo.bind("<FocusIn>", remover)
    campo.bind("<FocusOut>", adicionar)

def mascaraCPF(event):
    cpf = campoCPF.get().replace(".", "").replace("-", "")[:11]

    if len(cpf) > 9:
        cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    elif len(cpf) > 6:
        cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:]}"
    elif len(cpf) > 3:
        cpf = f"{cpf[:3]}.{cpf[3:]}"

    campoCPF.delete(0, tk.END)
    campoCPF.insert(0, cpf)
    campoCPF.icursor(tk.END)

campoNome = criarCampo()
placeholder(campoNome, "Nome")

estiloCategoria = ttk.Style()
estiloCategoria.theme_use("clam")

estiloCategoria.configure(
    "Categoria.TCombobox",
    font=("Montserrat", 16),
    foreground="black",
    background="white",
    fieldbackground="white",
    padding=5,
    border=2
)

estiloCategoria.map('Categoria.TCombobox',
    fieldbackground=[('readonly', 'white')],
    background=[('readonly', 'white')]
)

camposForm.option_add('*TCombobox*Listbox.background', 'white')
camposForm.option_add('*TCombobox*Listbox.foreground', 'black')
camposForm.option_add('*TCombobox*Listbox.font', ('Montserrat', 16))
camposForm.option_add('*TCombobox*font', ('Montserrat', 16))

campoCategoria = ttk.Combobox(
    camposForm,
    width=29,
    values=["Categoria", "Coordenador", "Bolsista", "Colaborador"],
    state="readonly",
    style="Categoria.TCombobox"
)
campoCategoria.current(0)

campoEmail = criarCampo()
placeholder(campoEmail, "E-mail institucional")

campoCPF = criarCampo()
placeholder(campoCPF, "CPF")
campoCPF.bind("<KeyRelease>", mascaraCPF)

campoSenha = criarCampo("hidden")
placeholderSenha(campoSenha, "Senha")

campoConfirma = criarCampo()
placeholder(campoConfirma, "Confirme a senha")


# IMAGENS



imagemUsuario = tk.PhotoImage(file=PASTA_IMAGENS / "user.png")
imagemSenha = tk.PhotoImage(file=PASTA_IMAGENS / "key-round.png")
imagemEmail = tk.PhotoImage(file=PASTA_IMAGENS / "mail.png")
imagemCPF = tk.PhotoImage(file=PASTA_IMAGENS / "id-card.png")
imagemConfirma = tk.PhotoImage(file=PASTA_IMAGENS / "shield-check.png")
imagemCategoria = tk.PhotoImage(file=PASTA_IMAGENS / "user-shield.png")

imagemUsuario = imagemUsuario.zoom(2, 2)
imagemSenha = imagemSenha.zoom(2, 2)
imagemEmail = imagemEmail.zoom(2, 2)
imagemCPF = imagemCPF.zoom(2, 2)
imagemConfirma = imagemConfirma.zoom(2, 2)
imagemCategoria = imagemCategoria.zoom(2, 2)

iconeUsuario = tk.Label(camposForm, image=imagemUsuario, bg=fundoCampos.cget("bg"))
iconeCategoria = tk.Label(camposForm, image=imagemCategoria, bg=fundoCampos.cget("bg"))
iconeEmail = tk.Label(camposForm, image=imagemEmail, bg=fundoCampos.cget("bg"))
iconeCPF = tk.Label(camposForm, image=imagemCPF, bg=fundoCampos.cget("bg"))
iconeSenha = tk.Label(camposForm, image=imagemSenha, bg=fundoCampos.cget("bg"))
iconeConfirma = tk.Label(camposForm, image=imagemConfirma, bg=fundoCampos.cget("bg"))






# ==================== EXIBIÇÃO ====================


# EXIBIÇÃO - PARTE ROXA
fundoTagline.pack_propagate(False)
fundoTagline.pack(side="left")


# EXIBIÇÃO - PARTE DO FORMULÁRIO
fundoCampos.pack_propagate(False)
fundoCampos.pack(
    side="right",
)

camposForm.pack(
    expand=True,
    anchor="center"
)
tituloForm.grid(row=0, column=1, sticky="w")

campoNome.grid(row=1, column=1, sticky="w", pady=5, ipady=7)
campoCategoria.grid(row=2, column=1, sticky="w", pady=5, ipady=7)
campoEmail.grid(row=3, column=1, sticky="w", pady=5, ipady=7)
campoCPF.grid(row=4, column=1, sticky="w", pady=5, ipady=7)
campoSenha.grid(row=5, column=1, sticky="w", pady=5, ipady=7)
campoConfirma.grid(row=6, column=1, sticky="w", pady=5, ipady=7)

iconeUsuario.grid(row=1, column=0, sticky="w", padx=(0, 15), pady=10, ipady=14)
iconeCategoria.grid(row=2, column=0, sticky="w", padx=(0, 15), pady=10, ipady=7)
iconeEmail.grid(row=3, column=0, sticky="w", padx=(0, 15), pady=10, ipady=7)
iconeCPF.grid(row=4, column=0, sticky="w", padx=(0, 15), pady=10, ipady=7)
iconeSenha.grid(row=5, column=0, sticky="w", padx=(0, 15), pady=10, ipady=7)
iconeConfirma.grid(row=6, column=0, sticky="w", padx=(0, 15), pady=10, ipady=7)

# FIM
janela.mainloop()