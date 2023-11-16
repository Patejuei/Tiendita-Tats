import reflex as rx
from tienditaTats.decorators.mainPage import mainPage
from tienditaTats.template import template
from tienditaTats.state import State

class LogInState(State):
    pass

@template(title='Iniciar Sesión', route='/login')
def login() -> rx.Component:
    return rx.center(
        rx.form(
            rx.vstack(
                
            )
        )
    )