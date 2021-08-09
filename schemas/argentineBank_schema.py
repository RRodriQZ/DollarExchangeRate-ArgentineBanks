from marshmallow import Schema, fields, post_load
from model.argentineBank_model import ArgentineBank


class ArgentineBankSchema(Schema):
    """ArgentineBank Schema"""

    bank_name = fields.String(attribute="bank_name")
    time = fields.String(attribute="time")
    buy = fields.Float(attribute="buy")
    sell = fields.Float(attribute="sell")
    purchase_with_taxes = fields.Float(attribute="purchase_with_taxes")

    @post_load
    def create_argentine_bank(self, data, **kwargs):
        return ArgentineBank(**data)
