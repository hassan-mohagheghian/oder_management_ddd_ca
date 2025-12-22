from order_app.infrastructure.web.fastapi.composition_root import composition_root
from order_app.infrastructure.web.fastapi.fastapi_app_factory import create_web_app

app = create_web_app(composition_root=composition_root)
