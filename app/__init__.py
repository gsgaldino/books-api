from flask_restx import Api

from .books import api as books_api

api = Api(title="Books API", version="1.0", description="Simple books API",)

api.add_namespace(books_api)
