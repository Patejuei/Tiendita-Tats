import reflex as rx
from tienditaTats.components.NewsCard import NewsCard

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
        )
    )
