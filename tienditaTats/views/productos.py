import reflex as rx
from tienditaTats.template import template
from tienditaTats.decorators.mainPage import mainPage
from tienditaTats.state import State

class ProductState(State):
    pass

@template(title="Productos", route='/products')
@mainPage(title='Productos', route='/products')
def productos() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.vstack(
                
            ),
            rx.box(

            )
        )
    )