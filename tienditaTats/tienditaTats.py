"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
from tienditaTats.components.Navbar import Navbar
from tienditaTats.views.Home import Home

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.vstack(
        Navbar(),
        Home()
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
