import reflex as rx

def SidebarMenuItems(text: str, link: str) -> rx.Component:
    return(
        rx.link(
            rx.menu_item(
                text,
            ),
            href=link,
            color = "#404040",
            background_color = "#D9D8A9",
            margin="0.7rem 0.5rem",
            padding="0.2rem",
            border_radius="1em",
            border="1px solid #C9F5D6"
        )
    )