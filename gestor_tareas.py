import json
from tarea import Tarea

class GestorTareas:
    def __init__(self, archivo="tareas.json"):
        self.archivo = archivo
        self.tareas = self._cargar()
    
    def _cargar(self):
        try:
            with open(self.archivo, 'r') as f:
                datos = json.load(f)
                return [Tarea(**tarea) for tarea in datos]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def guardar(self):
        with open(self.archivo, 'w') as f:
            json.dump([t.__dict__ for t in self.tareas], f, indent=2)
    
    def agregar(self, tarea):
        self.tareas.append(tarea)
        self.guardar()
    
    def eliminar(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
            self.guardar()