from flask_restx import Namespace, Resource, fields

api = Namespace("books", description="Books list operations")

book = api.model(
  "Book",
  {
    "id": fields.String(required=True, description="The book identifier"),
    "name": fields.String(required=True, description="The book name")
  }
)

BOOKS = [
  {"id": 2, "name": "Skyrim"}
]

@api.route('/')
class BookList(Resource):
  @api.marshal_with(book)
  def post(self):
    return BOOKS
