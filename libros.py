import flet as ft
from db import crear_tabla_libros, insertar_libro, obtener_libros, eliminar_libro

def vista_libros(page):
    crear_tabla_libros()

    lista = ft.Column(scroll=ft.ScrollMode.AUTO)

    filtro = ft.TextField(
        label="Buscar por título o autor...",
        width=400,
        on_change=lambda e: cargar_libros(e.control.value),
        prefix_icon="search"
    )

    def cargar_libros(texto_busqueda=""):
        libros = obtener_libros()
        texto_busqueda = texto_busqueda.lower()
        lista.controls.clear()

        for libro in libros:
            id_libro, titulo, autor, anio = libro
            if texto_busqueda in titulo.lower() or texto_busqueda in autor.lower():
                fila = ft.Row([
                    ft.Text(f"{titulo} - {autor} ({anio})", expand=True),
                    ft.IconButton(
                        icon="delete",
                        tooltip="Eliminar",
                        on_click=lambda e, id_libro=id_libro: eliminar(id_libro)
                    )
                ])
                lista.controls.append(fila)
        page.update()

    def agregar(e):
        if titulo.value and autor.value and anio.value.isdigit():
            insertar_libro(titulo.value, autor.value, int(anio.value))
            titulo.value = ""
            autor.value = ""
            anio.value = ""
            filtro.value = ""
            cargar_libros()

            page.snack_bar = ft.SnackBar(
                content=ft.Text("Libro agregado con éxito."),
                bgcolor="green",
                behavior="floating"
            )
            page.snack_bar.open = True
            page.update()
        else:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Campos inválidos."),
                bgcolor="red",
                behavior="floating"
            )
            page.snack_bar.open = True
            page.update()

    def eliminar(id_libro):
        eliminar_libro(id_libro)
        cargar_libros(filtro.value)

    titulo = ft.TextField(label="Título", width=300)
    autor = ft.TextField(label="Autor", width=300)
    anio = ft.TextField(label="Año", width=150, keyboard_type=ft.KeyboardType.NUMBER)

    cargar_libros()

    # 🎯 Contenido principal envuelto en una tarjeta blanca con sombra
    contenido = ft.Container(
        content=ft.Column([
            ft.Text("Registro de Libros", size=20, weight=ft.FontWeight.BOLD),
            ft.Row([titulo, autor, anio, ft.ElevatedButton("Agregar", on_click=agregar)]),
            ft.Divider(),
            filtro,
            ft.Text("Libros en el sistema:", size=16),
            lista
        ], expand=True),
        bgcolor="rgba(255,255,255,0.95)",
        padding=20,
        border_radius=12,
        shadow=ft.BoxShadow(
            spread_radius=0.1,
            blur_radius=1,
            color="#FDFAFAB2",
            offset=ft.Offset(0, 2)
        )
    )

    # 🎨 Fondo suave específico para esta pestaña
    return ft.Container(
        bgcolor="#FFF5F5",
        padding=30,
        content=contenido,
        expand=True
    )
