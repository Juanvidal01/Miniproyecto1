import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import time
import os
from tarea import Tarea
from gestor_tareas import GestorTareas


class InterfazTareas:
    def __init__(self, root, username,  logout_callback):  # Acepta los parámetros correctos
        self.root = root
        self.username = username
        self.logout_callback =logout_callback
        self.root.title(f"Gestor de Tareas - {username}")
        self.root.geometry("900x600")
        self.gestor = GestorTareas()
        self._setup_ui()
        self._cargar_tareas()

    def _setup_ui(self):
        """Configura la interfaz gráfica"""
        self._configurar_estilos()
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Treeview (Tabla de tareas)
        self.tree = ttk.Treeview(main_frame, columns=("Título", "Descripción", "Fecha", "Prioridad", "Estado"))
        self._configurar_treeview()
        
        # Scrollbars
        vsb = ttk.Scrollbar(main_frame, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(main_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        # Layout
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        
        # Frame de botones
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(btn_frame, text="➕ Agregar", command=self._mostrar_formulario).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="✏️ Editar", command=self._editar_tarea).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="🗑️ Eliminar", command=self._eliminar_tarea).pack(side=tk.LEFT, padx=5)

    def _configurar_estilos(self):
        """Configura los estilos visuales"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configuración de colores
        self.style.configure('TButton', 
                           font=('Arial', 10),
                           padding=6,
                           foreground='white',
                           background='#4CAF50')
        
        self.style.map('TButton',
                      foreground=[('active', 'white')],
                      background=[('active', '#45a049')])

    def _configurar_treeview(self):
        """Configura las columnas del Treeview"""
        columns = {
            "#0": {"text": "ID", "width": 50},
            "Título": {"width": 150},
            "Descripción": {"width": 200},
            "Fecha": {"width": 100},
            "Prioridad": {"width": 80},
            "Estado": {"width": 80}
        }
        
        for col, config in columns.items():
            self.tree.heading(col, text=config.get("text", col))
            self.tree.column(col, width=config["width"], stretch=tk.NO)

    def _mostrar_formulario(self, tarea=None):
        """Muestra el formulario para agregar/editar tareas"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Editar Tarea" if tarea else "Nueva Tarea")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Variables del formulario
        titulo_var = tk.StringVar(value=tarea.titulo if tarea else "")
        desc_var = tk.StringVar(value=tarea.descripcion if tarea else "")
        fecha_var = tk.StringVar(value=tarea.fecha if (tarea and tarea.fecha) else "")
        prioridad_var = tk.StringVar(value=tarea.prioridad if tarea else "media")
        completada_var = tk.BooleanVar(value=tarea.completada if tarea else False)
        
        # Widgets del formulario
        ttk.Label(dialog, text="Título*:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(dialog, textvariable=titulo_var, width=30).grid(row=0, column=1, pady=5)
        
        ttk.Label(dialog, text="Descripción:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Entry(dialog, textvariable=desc_var, width=30).grid(row=1, column=1, pady=5)
        
        # Selector de fecha mejorado (sin tkcalendar)
        ttk.Label(dialog, text="Fecha (DD/MM/AAAA):").grid(row=2, column=0, sticky=tk.W, pady=5)
        ttk.Entry(dialog, textvariable=fecha_var, width=15).grid(row=2, column=1, sticky=tk.W, pady=5)
        
        ttk.Label(dialog, text="Prioridad:").grid(row=3, column=0, sticky=tk.W, pady=5)
        ttk.Combobox(dialog, 
                    textvariable=prioridad_var,
                    values=["baja", "media", "alta"],
                    state="readonly").grid(row=3, column=1, sticky=tk.W, pady=5)
        
        ttk.Checkbutton(dialog, 
                       text="Completada",
                       variable=completada_var).grid(row=4, column=1, sticky=tk.W, pady=5)
        
        # Botones
        btn_frame = ttk.Frame(dialog)
        btn_frame.grid(row=5, columnspan=2, pady=10)
        
        ttk.Button(btn_frame, 
                 text="Guardar",
                 command=lambda: self._guardar_tarea(
                     titulo_var.get(),
                     desc_var.get(),
                     fecha_var.get(),
                     prioridad_var.get(),
                     completada_var.get(),
                     tarea,
                     dialog)
                 ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(btn_frame, 
                 text="Cancelar",
                 command=dialog.destroy).pack(side=tk.LEFT, padx=5)

    def _validar_fecha(self, fecha_str):
        """Valida el formato de fecha DD/MM/AAAA"""
        try:
            datetime.strptime(fecha_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def _guardar_tarea(self, titulo, descripcion, fecha, prioridad, completada, tarea=None, dialog=None):
        """Guarda una tarea nueva o editada"""
        titulo = titulo.strip()
        if not titulo:
            messagebox.showerror("Error", "El título es obligatorio", parent=dialog)
            return
        
        # Validar fecha si se proporcionó
        if fecha and not self._validar_fecha(fecha):
            messagebox.showerror("Error", "Formato de fecha inválido. Use DD/MM/AAAA", parent=dialog)
            return
        
        try:
            nueva_tarea = Tarea(
                titulo=titulo,
                descripcion=descripcion,
                fecha=fecha if fecha else None,
                prioridad=prioridad,
                completada=completada
            )
            
            if tarea:  # Edición
                indice = self.gestor.tareas.index(tarea)
                self.gestor.tareas[indice] = nueva_tarea
            else:  # Nueva tarea
                self.gestor.agregar(nueva_tarea)
            
            self.gestor.guardar()
            self._cargar_tareas()
            
            if dialog:
                dialog.destroy()
                
            messagebox.showinfo("Éxito", "Tarea guardada correctamente", parent=self.root)
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar:\n{str(e)}", parent=dialog)

    def _cargar_tareas(self):
        """Carga las tareas en el Treeview"""
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        for idx, tarea in enumerate(self.gestor.tareas):
            estado = "✅ Completada" if tarea.completada else "⏳ Pendiente"
            self.tree.insert("", "end", text=str(idx), values=(
                tarea.titulo,
                tarea.descripcion,
                tarea.fecha if tarea.fecha else "-",
                tarea.prioridad.capitalize(),
                estado
            ))

    def _editar_tarea(self):
        """Abre el formulario para editar una tarea"""
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para editar", parent=self.root)
            return
        
        indice = int(self.tree.item(seleccion[0])["text"])
        tarea = self.gestor.tareas[indice]
        self._mostrar_formulario(tarea)

    def _eliminar_tarea(self):
        """Elimina la tarea seleccionada"""
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar", parent=self.root)
            return
        
        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar esta tarea?", parent=self.root):
            indice = int(self.tree.item(seleccion[0])["text"])
            self.gestor.eliminar(indice)
            self._cargar_tareas()
            messagebox.showinfo("Éxito", "Tarea eliminada", parent=self.root)


def _mejorar_interfaz(self):
    # Configuración de grid para mejor responsividad
    self.root.grid_rowconfigure(0, weight=1)
    self.root.grid_columnconfigure(0, weight=1)
    
    # Tooltips para botones
    from tkinter import ToolTip  # Necesitarás pip install tkinter-tooltip
    botones = [
        ("➕ Agregar", "Crear nueva tarea"),
        ("✏️ Editar", "Modificar tarea seleccionada"),
        ("🗑️ Eliminar", "Eliminar tarea seleccionada")
    ]
    
    for btn_text, tooltip in botones:
        btn = ttk.Button(self.btn_frame, text=btn_text)
        btn.pack(side=tk.LEFT, padx=5)
        ToolTip(btn, msg=tooltip, delay=0.5)

def _cerrar_sesion(self):
    if messagebox.askyesno("Confirmar," "Cerrar sesion"):
        self.root.destroy()
        self.logout_callback()