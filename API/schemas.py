from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Str(dump_only = True)
    name = fields.Str(required = True)
    price = fields.Float(required = True)
    
class ItemSchema(PlainItemSchema):
    store_id = fields.Str(required = True)
    store = fields.Nested(PlainItemSchema(), dump_only = True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Str()
    store_id = fields.Int()

    

class PlainStoreSchema(Schema):
    id = fields.Str(dump_only = True)
    name = fields.Str(required = True)

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only = True)

