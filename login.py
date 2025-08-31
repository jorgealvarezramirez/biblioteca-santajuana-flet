import flet as ft

# Credenciales válidas
USUARIO_VALIDO = "admin"
CONTRASENA_VALIDA = "biblioteca123"

def login_view(page, on_login_success):
    usuario = ft.TextField(label="Usuario", width=300)
    contrasena = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)

    def autenticar(e):
        if usuario.value == USUARIO_VALIDO and contrasena.value == CONTRASENA_VALIDA:
            on_login_success()
        else:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Credenciales incorrectas."),
                bgcolor="red",
                behavior="floating"
            )
            page.snack_bar.open = True
            page.update()

    # 🎓 Encabezado institucional
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
                ft.Image(src="bandera.jpg", width=60, height=60),
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

    # 🦶 Footer institucional
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

    # Formulario de login centrado
    login_form = ft.Column(
        alignment="center",
        horizontal_alignment="center",
        spacing=20,
        controls=[
            ft.Text("Inicio de Sesión", size=24, weight=ft.FontWeight.BOLD, color="#0B3D0B"),
            usuario,
            contrasena,
            ft.ElevatedButton("Ingresar", on_click=autenticar),
        ]
    )

    # Fondo con marca de agua y layout completo
    fondo = ft.Container(
        content=ft.Stack([
            ft.Image(
                src="portada.jpg",
                opacity=0.45,
                expand=True,
                fit=ft.ImageFit.COVER
            ),
            ft.Container(
                content=ft.Column([
                    header,
                    ft.Container(login_form, alignment=ft.alignment.center, expand=True),
                    footer
                ], expand=True),
                alignment=ft.alignment.center,
                expand=True
            )
        ]),
        expand=True
    )

    return fondo
