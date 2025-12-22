from fastapi import FastAPI

from order_app.infrastructure.composition_root import CompositionRoot
from order_app.infrastructure.persistence.sqlite.init_db import init_db
from order_app.infrastructure.web.fastapi.dependencies import get_composition_root

# from order_app.infrastructure.web.fastapi import composition_root
from order_app.infrastructure.web.fastapi.routes.user_router import (
    router as user_router,
)


def create_web_app(composition_root: CompositionRoot, testing: bool = False):
    app = FastAPI(title="Order Management App", version="0.1.0")
    app.dependency_overrides[get_composition_root] = lambda: composition_root
    if testing:
        app.testing = True
        init_db()
    app.include_router(user_router, prefix="/users")
    return app
