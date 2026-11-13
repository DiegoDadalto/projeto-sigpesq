import tkinter as tk
from tkinter import ttk
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PASTA_IMAGENS = Path(__file__).resolve().parent.parent / "imagens"

# JANELA DA APLICAÇÃO
class TelaLogin(tk.Frame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)

        self.controller = controller

        self.configure(bg="misty rose")

        self.criarImagens()
        self.criarElementos()
        self.exibirElementos()

    def criarImagens(self):
        # FUNDO ROXO (BEM-VINDE)
        self.imagemFundo = tk.PhotoImage(file=PASTA_IMAGENS / "fundoTag.png")

        self.imagemUsuario = tk.PhotoImage(file=PASTA_IMAGENS / "user.png").zoom(2, 2)
        self.imagemSenha = tk.PhotoImage(file=PASTA_IMAGENS / "key-round.png").zoom(2, 2)
        self.imagemEmail = tk.PhotoImage(file=PASTA_IMAGENS / "mail.png").zoom(2, 2)
        self.imagemCPF = tk.PhotoImage(file=PASTA_IMAGENS / "id-card.png").zoom(2, 2)
        self.imagemConfirma = tk.PhotoImage(file=PASTA_IMAGENS / "shield-check.png").zoom(2, 2)
        self.imagemCategoria = tk.PhotoImage(file=PASTA_IMAGENS / "user-shield.png").zoom(2, 2)

    def criarElementos(self):
        # FUNDO ROXO

        self.fundoTagline = tk.Canvas(
            self,
            width=600,
            height=720,
            highlightthickness=0
        )

        self.fundoTagline.create_image(
            0, 0,
            image=self.imagemFundo,
            anchor="nw"
        )

        self.fundoTagline.create_text(
            300, 280,
            text="BEM-VINDE!",
            font=("Montserrat", 48, "bold"),
            fill="white"
        )

        self.fundoTagline.create_line(
            100, 330,
            500, 330,
            fill="white",
            width=2
        )

        self.fundoTagline.create_text(
            300, 370,
            text="Faça o cadastro para continuar",
            font=("Montserrat", 24),
            fill="white"
        )

        # FUNDO DO FORMULÁRIO

        self.fundoCampos = tk.Frame(
            self,
            width=680,
            height=720,
            bg="misty rose"
        )

        self.camposForm = tk.Frame(
            self.fundoCampos,
            padx=10,
            pady=10,
            bg=self.fundoCampos.cget("bg")
        )

        # TÍTULO

        self.tituloForm = tk.Label(
            self.camposForm,
            padx=10,
            pady=10,
            bg=self.fundoCampos.cget("bg"),
            text="Crie uma conta:",
            font=("Montserrat", 28)
        )

        # CAMPOS DE ENTRADA

        self.campoNome = self.criarCampo()
        self.placeholder(self.campoNome, "Nome")

        # CATEGORIA

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

        estiloCategoria.map(
            "Categoria.TCombobox",
            fieldbackground=[("readonly", "white")],
            background=[("readonly", "white")]
        )

        self.camposForm.option_add(
            "*TCombobox*Listbox.background", "white"
        )

        self.camposForm.option_add(
            "*TCombobox*Listbox.foreground", "black"
        )

        self.camposForm.option_add(
            "*TCombobox*Listbox.font", ("Montserrat", 16)
        )

        self.camposForm.option_add(
            "*TCombobox*font", ("Montserrat", 16)
        )

        self.campoCategoria = ttk.Combobox(
            self.camposForm,
            width=29,
            values=[
                "Categoria",
                "Coordenador",
                "Bolsista",
                "Colaborador"
            ],
            state="readonly",
            style="Categoria.TCombobox"
        )

        self.campoCategoria.current(0)

        # EMAIL

        self.campoEmail = self.criarCampo()
        self.placeholder(self.campoEmail, "E-mail institucional")

        # CPF

        self.campoCPF = self.criarCampo()
        self.placeholder(self.campoCPF, "CPF")

        self.campoCPF.bind(
            "<KeyRelease>",
            self.mascaraCPF
        )

        # SENHA

        self.campoSenha = self.criarCampo("hidden")
        self.placeholderSenha(self.campoSenha, "Senha")

        # CONFIRMAR SENHA

        self.campoConfirma = self.criarCampo()
        self.placeholder(self.campoConfirma, "Confirme a senha")

        # ÍCONES

        self.iconeUsuario = tk.Label(
            self.camposForm,
            image=self.imagemUsuario,
            bg=self.fundoCampos.cget("bg")
        )

        self.iconeCategoria = tk.Label(
            self.camposForm,
            image=self.imagemCategoria,
            bg=self.fundoCampos.cget("bg")
        )

        self.iconeEmail = tk.Label(
            self.camposForm,
            image=self.imagemEmail,
            bg=self.fundoCampos.cget("bg")
        )

        self.iconeCPF = tk.Label(
            self.camposForm,
            image=self.imagemCPF,
            bg=self.fundoCampos.cget("bg")
        )

        self.iconeSenha = tk.Label(
            self.camposForm,
            image=self.imagemSenha,
            bg=self.fundoCampos.cget("bg")
        )

        self.iconeConfirma = tk.Label(
            self.camposForm,
            image=self.imagemConfirma,
            bg=self.fundoCampos.cget("bg")
        )

    # CAMPOS DE ENTRADA DE INFORMAÇÕES

    def criarCampo(self, hidden=""):
        if hidden == "hidden":
            nomeCampo = tk.Entry(
                self.camposForm,
                width=30,
                bg="white",
                fg="black",
                font=("Montserrat", 16),
                bd=2,
                show="●"
            )
        else:
            nomeCampo = tk.Entry(
                self.camposForm,
                width=30,
                bg="white",
                fg="black",
                font=("Montserrat", 16),
                bd=2
            )
        return nomeCampo



    def placeholder(self, campo, texto):
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



    def placeholderSenha(self, campo, texto):
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



    def mascaraCPF(self, event):
        cpf = (self.campoCPF.get().replace(".", "").replace("-", "")[:11])

        if len(cpf) > 9:
            cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

        elif len(cpf) > 6:
            cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:]}"

        elif len(cpf) > 3:
            cpf = f"{cpf[:3]}.{cpf[3:]}"

        self.campoCPF.delete(0, tk.END)
        self.campoCPF.insert(0, cpf)
        self.campoCPF.icursor(tk.END)



    # ==================== EXIBIÇÃO ====================
    def exibirElementos(self):
        # EXIBIÇÃO - PARTE ROXA
        self.fundoTagline.pack_propagate(False)
        self.fundoTagline.pack(side="left")


        # EXIBIÇÃO - PARTE DO FORMULÁRIO
        self.fundoCampos.pack_propagate(False)
        self.fundoCampos.pack(
            side="right",
        )

        self.camposForm.pack(
            expand=True,
            anchor="center"
        )
        self.tituloForm.grid(row=0, column=1, sticky="w")

        self.campoNome.grid(row=1, column=1, sticky="w", pady=5, ipady=7)
        self.campoCategoria.grid(row=2, column=1, sticky="w", pady=5, ipady=7)
        self.campoEmail.grid(row=3, column=1, sticky="w", pady=5, ipady=7)
        self.campoCPF.grid(row=4, column=1, sticky="w", pady=5, ipady=7)
        self.campoSenha.grid(row=5, column=1, sticky="w", pady=5, ipady=7)
        self.campoConfirma.grid(row=6, column=1, sticky="w", pady=5, ipady=7)

        self.iconeUsuario.grid(row=1, column=0, sticky="w", padx=(0, 15), pady=10, ipady=14)
        self.iconeCategoria.grid(row=2, column=0, sticky="w", padx=(0, 15), pady=10, ipady=7)
        self.iconeEmail.grid(row=3, column=0, sticky="w", padx=(0, 15), pady=10, ipady=7)
        self.iconeCPF.grid(row=4, column=0, sticky="w", padx=(0, 15), pady=10, ipady=7)
        self.iconeSenha.grid(row=5, column=0, sticky="w", padx=(0, 15), pady=10, ipady=7)
        self.iconeConfirma.grid(row=6, column=0, sticky="w", padx=(0, 15), pady=10, ipady=7)