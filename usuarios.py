import flet as ft
from db import crear_tabla_usuarios, insertar_usuario, obtener_usuarios, eliminar_usuario

def vista_usuarios(page):
    crear_tabla_usuarios()
    lista = ft.Column(scroll=ft.ScrollMode.AUTO)

    def cargar_usuarios():
        lista.controls.clear()
        for usuario in obtener_usuarios():
            id_usuario, nombre, tipo = usuario
            fila = ft.Row([
                ft.Text(f"{nombre} - {tipo}", expand=True),
                ft.IconButton(
                    icon="delete",
                    tooltip="Eliminar",
                    on_click=lambda e, id_usuario=id_usuario: eliminar(id_usuario)
                )
            ])
            lista.controls.append(fila)
        page.update()

    def agregar(e):
        if nombre.value and tipo.value:
            insertar_usuario(nombre.value, tipo.value)
            nombre.value = ""
            tipo.value = ""
            cargar_usuarios()
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Usuario agregado con éxito."),
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

    def eliminar(id_usuario):
        eliminar_usuario(id_usuario)
        cargar_usuarios()

    nombre = ft.TextField(label="Nombre", width=300)
    tipo = ft.Dropdown(
        label="Tipo de usuario",
        options=[ft.dropdown.Option("Estudiante"), ft.dropdown.Option("Docente")],
        width=200
    )

    cargar_usuarios()

    contenido = ft.Container(
        content=ft.Column([
            ft.Text("Gestión de Usuarios", size=20, weight=ft.FontWeight.BOLD),
            ft.Row([nombre, tipo, ft.ElevatedButton("Agregar", on_click=agregar)]),
            ft.Divider(),
            ft.Text("Usuarios registrados:", size=16),
            lista
        ], expand=True),
        bgcolor="rgba(255,255,255,0.95)",
        padding=20,
        border_radius=12,
        shadow=ft.BoxShadow(
            spread_radius=0.5,
            blur_radius=6,
            color="#88888888",
            offset=ft.Offset(0, 2)
        )
    )

    return ft.Container(
        bgcolor="#F5FFF5",
        padding=30,
        content=contenido,
        expand=True
    )
