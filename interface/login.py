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
tituloForm.grid(row=0, column=1, sticky="w")

campoNome.grid(row=1, column=1, sticky="w", pady=5, ipady=7)
campoCategoria.grid(row=2, column=1, sticky="w", pady=5, ipady=7)
campoEmail.grid(row=3, column=1, sticky="w", pady=5, ipady=7)
campoCPF.grid(row=4, column=1, sticky="w", pady=5, ipady=7)
campoSenha.grid(row=5, column=1, sticky="w", pady=5, ipady=7)
campoConfirma.grid(row=6, column=1, sticky="w", pady=5, ipady=7)

# FIM
janela.mainloop()