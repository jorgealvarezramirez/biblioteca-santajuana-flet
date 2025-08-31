import flet as ft
from login import login_view
from libros import vista_libros
from usuarios import vista_usuarios
from prestamos import vista_prestamos

def main(page: ft.Page):
    page.title = "Biblioteca Santa Juana Lestonnac"
    page.horizontal_alignment = "center"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.window_min_width = 800

    # 🎨 Tema personalizado
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#0B3D0B",
            primary_container="#A9D6A9",
            secondary="#8B0000",
            surface="#FFFFFF",
            background="#FFFFFF",
            error="#B00020",
            on_primary="#FFFFFF",
            on_secondary="#FFFFFF",
            on_surface="#000000",
            on_background="#000000"
        ),
        text_theme=ft.TextTheme(
            title_large=ft.TextStyle(weight=ft.FontWeight.BOLD, color="#8B0000"),
            body_medium=ft.TextStyle(color="#333333"),
        )
    )

    # 🔐 Mostrar pantalla de login
    def mostrar_login(e=None):
        page.controls.clear()
        login = login_view(page, cargar_aplicacion)
        page.add(ft.Container(login, alignment=ft.alignment.center))
        page.update()

    # ✅ Cargar la app después del login exitoso
    def cargar_aplicacion():
        header = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Image(src="escudo.png", width=60, height=60),
                    ft.Text(
                        "Biblioteca Santa Juana Lestonnac",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color="white",
                        expand=True,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Row([
                        ft.IconButton(
                            icon="logout",
                            tooltip="Cerrar sesión",
                            on_click=mostrar_login
                        ),
                        ft.Image(src="bandera.jpg", width=60, height=60),
                    ])
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#8B0000",
            padding=15,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=8,
                color="#757575",
                offset=ft.Offset(0, 3),
                blur_style=ft.ShadowBlurStyle.NORMAL
            ),
        )

        tabs = ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                ft.Tab(text="Libros", icon="book", content=ft.Container(vista_libros(page), padding=10)),
                ft.Tab(text="Usuarios", icon="people", content=ft.Container(vista_usuarios(page), padding=10)),
                ft.Tab(text="Préstamos", icon="list_alt", content=ft.Container(vista_prestamos(page), padding=10)),
            ],
            expand=True,
        )

        footer = ft.Container(
            content=ft.Text(
                "© 2025 Santa Juana Lestonnac · Desarrollado por Nickol Alvarez y Kevin Galvis - Grado 11B",
                size=12,
                color="#888888",
                text_align=ft.TextAlign.CENTER
            ),
            padding=15,
            alignment=ft.alignment.center,
        )

        layout = ft.Column([
            header,
            ft.Container(content=tabs, expand=True),
            footer
        ], expand=True)

        page.controls.clear()
        page.add(layout)
        page.update()

    # 🟢 Comenzar en pantalla de login
    mostrar_login()

ft.app(target=main, view=ft.WEB_BROWSER, port=8080)
