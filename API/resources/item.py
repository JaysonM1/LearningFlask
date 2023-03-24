import uuid 
from flask import request 
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemSchema, ItemUpdateSchema
from models.item import ItemModel
from db import db
from sqlalchemy.exc import SQLAlchemyError
blp = Blueprint("Items", __name__, description = "Operations on items")

@blp.route("/item")
class Item(MethodView):

    @blp.response(200, ItemSchema)
    def get(self):
        return items.values()
    

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)

        try: 
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message = "An error occured while inserting the item")
        return item, 201
    


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try: 
            return items[item_id]
        except:
            abort(404, message = "Item not found.")

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemUpdateSchema)
    def put(self, item_id, item_data):
        try:
            item = items[item_id]
            item |= item_data
        except KeyError:
            abort(404, message = "Item not found")
    
    def delete(self, item_id):
        try: 
            del items[item_id]
            return {"message": "Item Deleted"}
        except:
            abort(404, message = "Item not found.")
