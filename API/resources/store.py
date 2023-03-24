import uuid 
from flask import request 
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import StoreSchema
from models import StoreModel
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("stores", __name__, description = "Operations on stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(201, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except:
            abort(404, message = "Store not found.")
    

    def delete(self, store_id):
        try: 
            del stores[store_id]
            return {"message": "Store Deleted"}
        except:
            abort(404, message = "Store not found.")


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many = True))
    def get(self):
        return list(stores.values())
    

    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, store_data):
        store = StoreModel(store_data)

        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message = "Integrity error")
        except SQLAlchemyError:
            abort(500, message = "An error occured while creating the store")

@blp.route("/store/<string:store_id>/item")
class StoreItems(MethodView):
    def get(self, store_id):
        for store in stores:
            if store["name"] == store_id:
                return {"items": store["items"]}
            abort(404, message = "Store not found.")