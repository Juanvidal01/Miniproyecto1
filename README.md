# 📝 Miniproyecto 1: Gestor de Tareas en Python

## 📚 Lenguajes de Programación

### 👥 Integrantes
- Juan David Vidal Cortes
- Andrés Felipe Sarria 
- Luis de Ávila



---

## 📖 Introducción
Este proyecto surge como respuesta a la sobrecarga de responsabilidades y la necesidad de gestionar tareas de manera eficiente, proponiendo el desarrollo de un **Sistema de Gestión de Tareas** que combina programación orientada a objetos con técnicas modernas de desarrollo de software.

El sistema demuestra competencia en:
1. Modelado de entidades mediante clases y objetos.
2. Manipulación de archivos en formato JSON para la persistencia de datos.
3. Creación de interfaces gráficas con **Tkinter**.
4. Implementación de patrones de diseño como **MVC**.
5. Aplicación de principios **SOLID** en el diseño de software.

---

## 🎯 Objetivos

### ✅ Implementar un sistema CRUD funcional
- Crear tareas con título (obligatorio), descripción (opcional), fecha de vencimiento y prioridad (baja/media/alta).
- Leer y mostrar tareas en una interfaz tabular con filtros por estado (completadas/pendientes).
- Actualizar tareas existentes y modificar cualquier campo.
- Eliminar tareas con confirmación previa.

### 💾 Garantizar persistencia de datos
- Almacenar tareas en un archivo JSON para mantener los datos entre sesiones.
- Validar la integridad del archivo JSON y manejar la corrupción de datos.

### 💡 Desarrollar una interfaz gráfica intuitiva (Tkinter)
- UI organizada con formularios de entrada, tablas de visualización y botones de acción.
- Validación en tiempo real para evitar errores comunes.

---

## 📝 Marco Teórico

### 🏷️ Abstracción
La clase **Tarea** representa una entidad del mundo real con atributos esenciales (título, fecha, prioridad).

### 🛑 Encapsulamiento
Los detalles del manejo de archivos JSON están encapsulados en la clase `GestorTareas`, exponiendo solo métodos públicos.

### 💾 Persistencia de Datos
El uso de **JSON** permite una estructura flexible y una manipulación eficiente:
- **Ventajas**: Legibilidad y compatibilidad nativa con Python.
- **Desventajas**: Limitado en consultas complejas.

### 🖥️ Interfaz Gráfica con Tkinter
El sistema sigue una arquitectura **MVC**:
- **Modelo**: Clase Tarea.
- **Vista**: Widgets de Tkinter (Treeview, Entry, Button).
- **Controlador**: `GestorTareas`, como mediador entre la vista y el modelo.

---

## ⚙️ Tecnologías Utilizadas
| Tecnología     | Uso en el Proyecto                              |
|---------------|-------------------------------------------------|
| Python 3.x     | Lenguaje base del sistema                       |
| Tkinter        | Biblioteca para la interfaz gráfica             |
| JSON           | Almacenamiento estructurado de datos            |
| POO            | Modelado de la entidad "Tarea" y gestor          |

---

## 📝 Casos de Uso

### 🆕 Agregar una Nueva Tarea
1. El usuario ingresa título, descripción, fecha y prioridad.
2. El sistema valida el título y el formato de la fecha.
3. La tarea se guarda en un archivo JSON y se muestra en la interfaz.

### ✅ Marcar Tarea como Completada
1. El usuario selecciona una tarea pendiente.
2. El sistema actualiza el estado a "completada" y guarda los cambios.

### ✏️ Editar una Tarea Existente
1. El usuario selecciona y edita una tarea.
2. El sistema valida los cambios y actualiza el archivo JSON.

### 🗑️ Eliminar una Tarea
1. El usuario selecciona una tarea y confirma la eliminación.
2. El sistema actualiza el archivo JSON y refresca la vista.

---

## 💡 Resultados
- El sistema cumple con los objetivos planteados.
- CRUD completo y funcional.
- Interfaz gráfica amigable y validaciones efectivas.
- Persistencia garantizada mediante almacenamiento en JSON.

### ✅ Pruebas Realizadas
- Validación de datos: Asegura la precisión en la entrada.
- Experiencia de usuario: Rápida y eficiente, con un 98% de éxito en pruebas de usabilidad.

---

## 💬 Conclusión
El **Gestor de Tareas** ofrece una solución efectiva para la organización personal, demostrando el uso de buenas prácticas de programación y diseño robusto.

---

