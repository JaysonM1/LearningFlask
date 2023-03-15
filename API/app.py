import uuid
from flask import Flask, request
from db import items,stores

app = Flask(__name__)


##local host with /store will return the list of stores from above
@app.get("/store")
def get_stores():
    return list(stores.values())

@app.get("/store")
def get_all_items():
    return list(items.values())

@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uid4().hex
    new_store = {**store_data, "id":store_id}
    stores[store_id] = new_store
    return new_store, 201

@app.post("/item")
def create_item():
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        return {"message": "Store not found"}, 404
    
    
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    return item, 201

@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except:
        return {"message": "Store not found"}, 404

@app.get("/store/<string:store_id>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try: 
        return items[item_id]
    except:
        return {"message": "Item not found"}, 404