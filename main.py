import os
import sys
import tkinter as tk
from tkinter import messagebox
from login_window import LoginWindow
from interfaz import InterfazTareas
from database import crear_tabla

def check_environment():
    """Verifica y activa el entorno virtual automáticamente"""
    if not hasattr(sys, 'real_prefix') and 'VIRTUAL_ENV' not in os.environ:
        venv_activate = os.path.join(os.path.dirname(__file__), 'venv', 'Scripts', 'activate_this.py')
        try:
            with open(venv_activate) as f:
                exec(f.read(), {'__file__': venv_activate})
            print("Entorno virtual activado automáticamente")
        except Exception as e:
            messagebox.showerror(
                "Error de Entorno",
                f"No se pudo activar el entorno virtual:\n{str(e)}\n\n"
                "Ejecuta manualmente desde CMD:\n"
                "venv\\Scripts\\activate.bat"
            )
            sys.exit(1)

def iniciar_aplicacion_principal(username):
    """Inicia la aplicación principal después del login"""
    root = tk.Tk()
    
    # Define el callback para cerrar sesión
    def logout_handler():
        root.destroy()  # Cierra la ventana actual
        mostrar_ventana_login()  # Vuelve a mostrar el login
    
    app = InterfazTareas(root, username, logout_handler)  # ✅ Pasa los 3 argumentos
    root.mainloop()

def mostrar_ventana_login():
    """Muestra la ventana de login"""
    login_root = tk.Tk()
    login_app = LoginWindow(login_root, iniciar_aplicacion_principal)
    login_root.mainloop()

if __name__ == "__main__":
    crear_tabla()  # Configuración inicial de la base de datos
    mostrar_ventana_login()  # Inicia con el login