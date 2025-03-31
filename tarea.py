class Tarea:
    def __init__(self, titulo, descripcion="", fecha=None, prioridad="media", completada=False):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = fecha  # Formato: "DD/MM/AAAA" o None
        self.prioridad = prioridad
        self.completada = completada