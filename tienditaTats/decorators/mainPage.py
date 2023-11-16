DECORATED_PAGES = []

def mainPage(
        route : str | None = None,
        title : str | None = None,
        image : str | None = None
):
    def decorator(render_fn):
        kwargs = {}
        if route:
            kwargs['route'] = route
        if title:
            kwargs['title'] = title
        if image:
            kwargs['image'] = image
        
        DECORATED_PAGES.append((render_fn, kwargs))

        return render_fn
    return decorator

def get_main_pages()->list[dict]:
    return sorted(
        [mainPages for render_fn, mainPages in DECORATED_PAGES],
        key= lambda x: x["route"],
    )
