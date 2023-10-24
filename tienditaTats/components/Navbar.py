import reflex as rx
from tienditaTats.components.SidebarMenuItems import SidebarMenuItems

def Navbar() -> rx.Component:
    return rx.hstack(
        rx.menu(
            SidebarMenuItems("Inicio", "/"),
            SidebarMenuItems("Productos", "/"),
            SidebarMenuItems("Pedidos Personalizados", "/"),
            SidebarMenuItems("Seguimiento", "/"),
            SidebarMenuItems("Mis Compras", "/"),
            rx.spacer(),
            SidebarMenuItems("Iniciar Sesión", "#"),
            SidebarMenuItems("Registrarse", "#"),
            SidebarMenuItems("Carro", "#"),
        ),
        background_color="#EBD3B5",
        width="100%"
    )
    