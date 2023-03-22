import uuid 
from flask import request 
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores

blp = Blueprint("stores", __name__, description = "Operations on stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
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
    def get(self):
        return list(stores.values())
    
    def post(self):
        store_data = request.get_json()
        if "name" not in store_data:
            abort(400, message = "Bad request. Ensure name is in JSON payload")
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message = f"Store already exists")
        store_id = uuid.uuid4().hex
        new_store = {**store_data, "id":store_id}
        stores[store_id] = new_store
        return new_store, 201

@blp.route("/store/<string:store_id>/item")
class StoreItems(MethodView):
    def get(self, store_id):
        for store in stores:
            if store["name"] == store_id:
                return {"items": store["items"]}
            abort(404, message = "Store not found.")