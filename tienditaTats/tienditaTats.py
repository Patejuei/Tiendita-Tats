"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
from tienditaTats.views import *
import reflex as rx


# Add state and page to the app.
app = rx.App()
app.compile()
