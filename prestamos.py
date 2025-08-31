import flet as ft
from db import (
    crear_tabla_prestamos, insertar_prestamo,
    obtener_prestamos, devolver_prestamo,
    obtener_usuarios, obtener_libros_disponibles
)

def vista_prestamos(page):
    crear_tabla_prestamos()

    # 🧾 Contenedor scrollable para la lista
    lista = ft.Container(
        content=ft.Column(scroll=ft.ScrollMode.AUTO),
        height=300,
        expand=False
    )

    def cargar_prestamos():
        lista.content.controls.clear()
        for prestamo in obtener_prestamos():
            id_prestamo, usuario, libro, fecha, devuelto = prestamo
            estado = "Devuelto" if devuelto else "En préstamo"
            fila = ft.Row([
                ft.Text(f"{libro} → {usuario} ({fecha}) - {estado}", expand=True),
                ft.IconButton(
                    icon="undo",
                    tooltip="Devolver",
                    on_click=lambda e, id_prestamo=id_prestamo: devolver(id_prestamo)
                ) if not devuelto else ft.Container()
            ])
            lista.content.controls.append(fila)
        page.update()

    def prestar(e):
        if usuario_dropdown.value and libro_dropdown.value:
            insertar_prestamo(int(usuario_dropdown.value), int(libro_dropdown.value))
            cargar_prestamos()
            cargar_libros_disponibles()
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Préstamo registrado."),
                bgcolor="green",
                behavior="floating"
            )
            page.snack_bar.open = True
            page.update()
        else:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Selecciona usuario y libro."),
                bgcolor="red",
                behavior="floating"
            )
            page.snack_bar.open = True
            page.update()

    def devolver(id_prestamo):
        devolver_prestamo(id_prestamo)
        cargar_prestamos()
        cargar_libros_disponibles()

    def cargar_usuarios():
        usuario_dropdown.options = []
        for u in obtener_usuarios():
            id_usuario, nombre, tipo = u
            usuario_dropdown.options.append(ft.dropdown.Option(str(id_usuario), f"{nombre} ({tipo})"))
        page.update()

    def cargar_libros_disponibles():
        libro_dropdown.options = []
        for l in obtener_libros_disponibles():
            id_libro, titulo, autor, anio = l
            libro_dropdown.options.append(ft.dropdown.Option(str(id_libro), f"{titulo} - {autor}"))
        page.update()

    usuario_dropdown = ft.Dropdown(label="Usuario", width=300)
    libro_dropdown = ft.Dropdown(label="Libro disponible", width=300)

    cargar_usuarios()
    cargar_libros_disponibles()
    cargar_prestamos()

    contenido = ft.Container(
        content=ft.Column([
            ft.Text("Préstamos de Libros", size=20, weight=ft.FontWeight.BOLD),
            ft.Row([usuario_dropdown, libro_dropdown, ft.ElevatedButton("Prestar", on_click=prestar)]),
            ft.Divider(),
            ft.Text("Historial de Préstamos:", size=16),
            lista  # ← ya es scrollable
        ], expand=True),
        bgcolor="rgba(255,255,255,0.95)",
        padding=20,
        border_radius=12,
        shadow=ft.BoxShadow(
            spread_radius=0.1,
            blur_radius=1,
            color="#88888888",
            offset=ft.Offset(0, 1)
        )
    )

    return ft.Container(
        bgcolor="#F5F8FF",
        padding=30,
        content=contenido,
        expand=True
    )
