import tkinter as tk
from tkinter import ttk, messagebox
from database import registrar_usuario, verificar_login

class LoginWindow:
    def __init__(self, root, login_callback, register_callback=None):
        self.root = root
        self.login_callback = login_callback
        self.register_callback = register_callback
        self.root.title("Login - Gestor de Tareas")
        self.root.geometry("300x200")
        
        # Variables para almacenar entrada
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        
        # Marco principal
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        # Etiquetas y campos de entrada
        ttk.Label(main_frame, text="Usuario:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.username).grid(row=0, column=1, pady=5, padx=5)
        
        ttk.Label(main_frame, text="Contraseña:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.password, show="*").grid(row=1, column=1, pady=5, padx=5)
        
        # Botones
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=2, columnspan=2, pady=15)
        
        ttk.Button(btn_frame, text="Iniciar Sesión", command=self._login).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Registrar", command=self._register).pack(side=tk.LEFT, padx=5)
    
    def _login(self):
        """Maneja el intento de inicio de sesión"""
        username = self.username.get()
        password = self.password.get()
        
        if verificar_login(username, password):
            self.root.destroy()
            self.login_callback(username)  # Usamos el callback proporcionado
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
    
    def _register(self):
        """Maneja el registro de nuevos usuarios"""
        username = self.username.get()
        password = self.password.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Usuario y contraseña son obligatorios")
            return
            
        if registrar_usuario(username, password):
            messagebox.showinfo("Éxito", "Usuario registrado correctamente")
            if self.register_callback:  # Si hay callback de registro
                self.register_callback(username)
        else:
            messagebox.showerror("Error", "El usuario ya existe")