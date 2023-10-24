import reflex as rx

def NewsCard() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.image(
                src="https://placehold.co/350"
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Producto"
                    ),
                    rx.spacer(),
                    rx.button(
                        "Ver Producto"
                    ),
                ),
                rx.hstack(
                    rx.text(
                        "Precio"
                    ),
                    rx.spacer(),
                    rx.button(
                        "Añadir al Carro"
                    ),
                ),
                rx.text(
                    "Cantidad"
                )
            )
        ),
        padding = "2rem",
        background_color = "#D9D8A9",
    )