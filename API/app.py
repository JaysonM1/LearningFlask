from flask import Flask

app = Flask(__name__)
from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

##local host with /store will return the list of stores from above
@app.get("/store")
def get_stores():
    return {"stores": stores}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"],"items":[]}
    stores.append(new_store)
    return stores, 201
