import reflex as rx
from tienditaTats.decorators.mainPage import get_main_pages

def Navbar() -> rx.Component:
    return rx.hstack(
        rx.menu(
            *[
                navbarItems(text=page.get('title', page['route'].strip('/').capitalize()),
                                 route=page['route'])
                                 for page in get_main_pages()
            ],
            rx.spacer(),
            navbarItems("Iniciar Sesión", "/login"),
            navbarItems("Registrarse", "#register"),
            navbarItems("Carro", "#carro"),
        ),
        background_color="#EBD3B5",
        width="100%"
    )

def navbarItems(text : str, route : str) -> rx.Component:
    return rx.link(
            rx.menu_item(
                text,
            ),
            href=route,
            color = "#404040",
            background_color = "#D9D8A9",
            margin="0.7rem 0.5rem",
            padding="0.2rem",
            border_radius="1em",
            border="1px solid #C9F5D6",
        )