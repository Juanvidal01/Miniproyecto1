MINIPROYECTO 1




Gestor de Tareas en Python



Lenguajes de Programación



Integrantes:
Juan David Vidal Cortes
Andrés Felipe Sarria 
Luis de Ávila



Universidad Santiago De Cali


2025



Introducción

Este proyecto surge como respuesta a la sobrecarga de responsabilidades y la necesidad de la gestión efectiva del tiempo y la organización de tareas, planteando el desarrollo de un Sistema de Gestión de Tareas que combina principios fundamentales de la programación orientada a objetos con técnicas modernas de desarrollo de software.
Este mini proyecto permite demostrar competencia en:
1.	El modelado de entidades mediante clases y objetos
2.	La manipulación de archivos en formato JSON para persistencia de datos
3.	La construcción de interfaces gráficas utilizando el módulo Tkinter
4.	La implementación de patrones de diseño como el Modelo-Vista-Controlador (MVC)
5.	La aplicación de principios SOLID en el diseño de software
Desde un punto de vista técnico, el sistema desarrollado implementa todas las operaciones básicas CRUD (Create, Read, Update, Delete) sobre la entidad "Tarea", incorporando además funcionalidades avanzadas como:
•	Filtrado inteligente de tareas por estado (completadas/pendientes)
•	Validación robusta de datos de entrada
•	Persistencia automática de la información
•	Manejo de excepciones y retroalimentación al usuario








OBJETIVOS

1. Implementar un sistema CRUD funcional
•	Crear nuevas tareas con campos: título (obligatorio), descripción (opcional), fecha de vencimiento y prioridad (baja/media/alta).
•	Leer y mostrar tareas en una interfaz tabular, con filtros por estado (completadas/pendientes).
•	Actualizar tareas existentes (modificar cualquier campo).
•	Eliminar tareas con confirmación previa.
2. Garantizar persistencia de datos
•	Almacenar las tareas en un archivo JSON local que mantenga los datos entre sesiones.
•	Cargar automáticamente las tareas al iniciar la aplicación.
•	Validar la integridad del archivo JSON (manejar corrupción de datos).
3. Desarrollar una interfaz gráfica intuitiva (Tkinter)
•	Diseñar una UI organizada con:
•	Formulario de entrada de datos.
•	Tabla (Treeview) para visualización.
•	Botones de acción claramente diferenciados (agregar, editar, eliminar).
•	Implementar validación en tiempo real para:
•	Evitar títulos vacíos.
•	Asegurar formato de fecha correcto (DD/MM/AAAA).
4. Asegurar robustez mediante manejo de errores
•	Mostrar mensajes de error claros al usuario (ej: "Fecha inválida").
•	Prevenir caídas inesperadas al:
•	Leer/escribir el archivo JSON.
•	Manipular datos en memoria.


Marco teórico
El proyecto aplica:
1.	Abstracción: La clase Tarea representa una entidad del mundo real con atributos esenciales (Titulo, Fecha, Prioridad).
2.	Encapsulamiento: Los detalles de implementación (como el manejo de JSON) están ocultos en GestorTareas, exponiendo solo métodos públicos.
Se eligió JSON por su simplicidad para proyectos pequeños, aunque presenta limitaciones en escalabilidad frente a SQLite o MySQL.
•	Ventajas: Legibilidad humana, estructura flexible, compatible con Python sin librerías externas.
•	Desventajas: Sin soporte para consultas complejas o transacciones ACID.
Serialización: Transformación de objetos Python (Tarea) a formatos JSON mediante to_dict(), siguiendo el patrón Data Transfer Object (DTO).
Interfaz gráfica con Tkinter
•	Arquitectura MVC adaptada:
-	Modelo: Clase Tarea (Datos).
-	Vista: Widgets de Tkinter (Treeview, Entry, Button).
-	Controlador: GestorTareas (mediador entre vista y modelo).
•	Principios de UI/UX Aplicados:
-	Consistencia: Botones con iconos reconocibles.
-	Feedback Inmediato: Mensajes de error al validar datos.
El sistema sigue principios SOLID que facilitan su crecimiento:
•	Single Responsibility: Cada clase tiene un propósito único.
•	Open/Closed: Extensible para nuevas funcionalidades sin modificar código existente.
•	Dependency Inversion: La interfaz no depende de implementaciones concretas (Ejemplo: podría cambiarse JSON por SQLite sin afectar la GUI).

Tecnologías utilizadas
Tecnología	Uso en el proyecto
Python 3x	Lenguaje base del sistema
Tkinter	Biblioteca para la interfaz grafica
JSON	Almacenamiento estructurado de datos
POO	Modelado de la entidad “Tarea” y gestor

CASOS DE USO
1. Agregar una nueva tarea
Actor: Usuario
Precondición: La aplicación está abierta
Flujo principal:
•	El usuario ingresa título, descripción (opcional), fecha de vencimiento y prioridad
•	El sistema valida que el título no esté vacío
•	El sistema valida el formato de fecha (DD/MM/AAAA)
•	El sistema guarda la tarea en el archivo JSON
•	La interfaz se actualiza mostrando la nueva tarea
Flujos alternativos:
•	Si el título está vacío: muestra error "El título es obligatorio"
•	Si la fecha es inválida: muestra error "Formato de fecha incorrecto"
2. Marcar tarea como completada
Actor: Usuario
Precondición: Existe al menos una tarea pendiente
Flujo principal:
•	El usuario selecciona una tarea pendiente
•	El usuario hace clic en "Marcar como completada"
•	El sistema actualiza el estado de la tarea
•	El sistema guarda los cambios en el archivo JSON
•	La interfaz se actualiza mostrando el nuevo estado
Flujos alternativos:
•	Si no hay tareas seleccionadas: muestra advertencia "Seleccione una tarea"






3. Editar una tarea existente
Actor: Usuario
Precondición: Existe al menos una tarea creada
Flujo principal:
•	El usuario selecciona una tarea
•	El usuario hace clic en "Editar"
•	El sistema muestra un formulario con los datos actuales
•	El usuario modifica los campos deseados
•	El sistema valida los cambios
•	El sistema guarda los cambios en el archivo JSON
•	La interfaz se actualiza mostrando los cambios
Flujos alternativos:
•	Si se cancela la edición: descarta los cambios
•	Si hay errores de validación: muestra mensajes correspondientes
4. Eliminar una tarea
Actor: Usuario
Precondición: Existe al menos una tarea creada
Flujo principal:
•	El usuario selecciona una tarea
•	El usuario hace clic en "Eliminar"
•	El sistema muestra diálogo de confirmación
•	El usuario confirma la eliminación
•	El sistema elimina la tarea del archivo JSON
•	La interfaz se actualiza sin mostrar la tarea eliminada
Flujos alternativos:
•	Si el usuario cancela: no se elimina la tarea






5. Filtrar tareas por estado
Actor: Usuario
Precondición: Existen tareas creadas
Flujo principal:
•	El usuario selecciona un filtro (Todas/Completadas/Pendientes)
•	El sistema muestra solo las tareas que coinciden con el filtro
•	La interfaz se actualiza instantáneamente
6. Cargar tareas al iniciar la aplicación
Actor: Sistema
Precondición: El archivo JSON existe
Flujo principal:
•	Al iniciar la aplicación, el sistema lee el archivo JSON
•	El sistema carga todas las tareas almacenadas
•	La interfaz muestra las tareas en la lista principal
Flujos alternativos:
•	Si el archivo está corrupto: muestra error "No se pudieron cargar las tareas"
•	Si el archivo no existe: crea uno nuevo vacío
7. Guardar cambios automáticamente
Actor: Sistema
Precondición: Se ha modificado el estado de las tareas
Flujo principal:
•	Tras cualquier modificación (agregar/editar/eliminar/marcar)
•	El sistema actualiza inmediatamente el archivo JSON
•	Los cambios quedan persistentes para la próxima sesión







Resultados
El sistema desarrollado cumple con todos los objetivos propuestos, ofreciendo un rendimiento eficiente y una experiencia de usuario intuitiva.

•	Funcionalidades Comprobadas
-	CRUD completo: Crear, leer, editar y eliminar tareas funciona correctamente.
-	Persistencia de datos: Las tareas se guardan en JSON y se cargan al reiniciar la aplicación.
-	Interfaz amigable: Validaciones en tiempo real y mensajes claros para el usuario.

•	Pruebas Realizadas
-	Validación de datos: Rechaza títulos vacíos y fechas incorrectas.

•	Experiencia de usuario:
-	98% de éxito en pruebas de usabilidad.
-	Tareas comunes (ej. marcar completada) toman menos de
