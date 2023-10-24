import reflex as rx
from tienditaTats.components.SidebarMenuItems import SidebarMenuItems

def Navbar() -> rx.Component:
    return rx.hstack(
        rx.menu(
            SidebarMenuItems("Inicio", "/"),
            SidebarMenuItems("Productos", "#productos"),
            SidebarMenuItems("Pedidos Personalizados", "#personalizados"),
            SidebarMenuItems("Seguimiento", "#seguimiento"),
            SidebarMenuItems("Mis Compras", "#compras"),
            rx.spacer(),
            SidebarMenuItems("Iniciar Sesión", "#login"),
            SidebarMenuItems("Registrarse", "#register"),
            SidebarMenuItems("Carro", "#carro"),
        ),
        background_color="#EBD3B5",
        width="100%"
    )
    