import reflex as rx
from tienditaTats.components.NewsCard import NewsCard
from tienditaTats.template import template
from tienditaTats.decorators.mainPage import mainPage

@template(title='Inicio', route='/')
@mainPage(title='Inicio', route='/')
def Home() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Novedades",
            text_align="left"
        ),
        rx.hstack(
        NewsCard(),
        rx.spacer(),
        NewsCard(),
        rx.spacer(),
        NewsCard(),
        ),
        rx.heading(
            "Pedidos Personalizados"
        ),
        rx.hstack(
            rx.text("Ingresa aqui para solicitar tus pedidos personalizados"),
            rx.link(
                "Pedidos Personalizados",
                href="#personalizados"
            )
        )
    )
